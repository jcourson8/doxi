import asyncio
import aiohttp
import os
import requests
import urllib.parse
import ssl
import certifi
from bs4 import BeautifulSoup
from .utils import sanitize_filename, create_folder
from tqdm import tqdm
from .utils import Text
from .errors import RateLimitExceededError, PaymentRequiredError


class DoxiScraper:
    def __init__(
        self,
        api_key,
        max_requests_per_minute=200,
        max_concurrent_requests=2,
        flat=False,
        force=False,
    ):
        self.api_key = api_key
        self.max_requests_per_minute = max_requests_per_minute
        self.max_concurrent_requests = max_concurrent_requests
        self.flat = flat
        self.force = force

    def get_links_from_sitemap(self, url):
        sitemap_url = urllib.parse.urljoin(url, "sitemap.xml")
        try:
            response = requests.get(sitemap_url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "xml")
            urls = [loc.text for loc in soup.find_all("loc")]
            return urls
        except requests.exceptions.RequestException as e:
            print(Text.Red + "Unable to fetch sitemap", Text.Reset)
            exit()

    async def fetch(self, session: aiohttp.ClientSession, url: str) -> str:
        """Fetch the markdown content of the page using r.jina.ai API."""
        headers = (
            {
                "Authorization": f"Bearer {self.api_key}",
            }
            if self.api_key
            else None
        )
        # Prepare the r.jina.ai API endpoint
        api_url = f"https://r.jina.ai/{urllib.parse.quote(url)}"
        try:
            async with session.get(api_url, headers=headers) as response:
                if response.status == 429:
                    # Raise custom exception for rate limit
                    raise RateLimitExceededError(
                        f"{Text.Bold}Rate limit exceeded when fetching {url}. This may be due to one of the following reasons:{Text.Reset}\n"
                        "  1. If using an API key: The rate limit options may be incorrectly set for your key.\n"
                        "  2. If not using an API key: You may have reached the rate limit in a previous CLI call.\n\n"
                        f"{Text.Bold}Suggested actions:{Text.Reset}\n"
                        "  - If using an API key: Verify and adjust your rate limit settings.\n"
                        "  - If not using an API key: Wait approximately one minute before trying again.\n"
                        "  - Consider upgrading to an API key for higher rate limits."
                    )
                if response.status == 402:
                    raise PaymentRequiredError(
                        f"{Text.Bold}Unable to fetch {url} due to insufficient credits. Please consider one of the following options:{Text.Reset}\n"
                        "  1. Upgrade your current plan\n"
                        "  2. Use a different API key with available credits\n"
                        "  3. Remove the API key to use the free tier (note: this will result in lower rate limits)"
                    )

                response.raise_for_status()
                return await response.text()
        except aiohttp.ClientResponseError as e:
            if e.status == 429:
                raise RateLimitExceededError(f"Rate limit exceeded when fetching {url}")
            else:
                raise e

    async def process_link(
        self,
        session: aiohttp.ClientSession,
        link: str,
        file_path: str,
        sem: asyncio.Semaphore,
        rate_limit_interval: float,
        pbar,
    ):
        """Process an individual link."""
        async with sem:
            try:
                content = await self.fetch(session, link)
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
                await asyncio.sleep(rate_limit_interval)  # Wait to adhere to rate limit
            except RateLimitExceededError:
                raise
            except PaymentRequiredError:
                raise
            except Exception as e:
                print(f"Failed to fetch {link}: {e}")
                raise
            finally:
                pbar.update(1)

    async def process_documentation_site(
        self,
        url: str,
        sem: asyncio.Semaphore,
        rate_limit_interval: float,
        output_dir: str = ".",
    ):
        """Process an entire documentation site."""
        print(f"Extracting navigation links from {url}")
        nav_links = self.get_links_from_sitemap(url)
        print(f"Found {len(nav_links)} links in sitemap.")

        # Remove duplicate links
        nav_links = list(set(nav_links))

        # Create base folder for this documentation site
        parsed_url = urllib.parse.urlparse(url)
        base_folder_name = os.path.join(output_dir, parsed_url.netloc)
        create_folder(base_folder_name)

        # Prepare lists for links to process and links to skip
        links_to_process = []
        links_skipped = []

        for link in nav_links:
            # Determine the file path where the file would be saved
            parsed_link_url = urllib.parse.urlparse(link)
            path_segments = parsed_link_url.path.strip("/").split("/")
            if self.flat:
                # Create a filename by joining path segments with hyphens
                if path_segments and path_segments[-1]:
                    file_name = "-".join(path_segments) + ".md"
                else:
                    file_name = "-".join(path_segments + ["index"]) + ".md"
                file_name = sanitize_filename(file_name)
                file_path = os.path.join(base_folder_name, file_name)
            else:
                # Create subdirectories matching the URL path
                sub_dirs = (
                    os.path.join(*path_segments[:-1]) if len(path_segments) > 1 else ""
                )
                save_path = os.path.join(base_folder_name, sub_dirs)
                create_folder(save_path)
                # Use the last segment as the filename
                file_name = (
                    sanitize_filename(
                        path_segments[-1] if path_segments[-1] else "index"
                    )
                    + ".md"
                )
                file_path = os.path.join(save_path, file_name)

            # Check if the file already exists
            if os.path.isfile(file_path) and not self.force:
                links_skipped.append(link)
            else:
                links_to_process.append((link, file_path))

        # Inform the user about skipped files
        if links_skipped:
            print(f"Skipping {len(links_skipped)} files that already exist.")
        if links_to_process:
            print(f"Processing {len(links_to_process)} files.")

        if not links_to_process:
            print("All documentation files already exist. Nothing to do.")
            return  # Exit the function

        # Create SSL context using certifi
        ssl_context = ssl.create_default_context(cafile=certifi.where())
        connector = aiohttp.TCPConnector(ssl=ssl_context)

        # Create a progress bar
        pbar = tqdm(total=len(links_to_process), desc=f"Processing {url}")

        async with aiohttp.ClientSession(connector=connector) as session:
            tasks = []
            for link, file_path in links_to_process:
                # Wrap the coroutine in a Task object
                task = asyncio.create_task(
                    self.process_link(
                        session, link, file_path, sem, rate_limit_interval, pbar
                    )
                )
                tasks.append(task)

            try:
                await asyncio.gather(*tasks)
            except (RateLimitExceededError, PaymentRequiredError) as e:
                # Cancel all pending tasks
                for task in tasks:
                    task.cancel()
                # Wait for tasks to cancel
                await asyncio.gather(*tasks, return_exceptions=True)
                # Re-raise the exception to stop further processing
                raise e
            finally:
                pbar.close()

    async def run(self, documentation_urls, output_dir="."):
        sem = asyncio.Semaphore(self.max_concurrent_requests)
        rate_limit_interval = 60 / self.max_requests_per_minute

        tasks = []
        for url in documentation_urls:
            task = asyncio.create_task(
                self.process_documentation_site(
                    url, sem, rate_limit_interval, output_dir
                )
            )
            tasks.append(task)

        try:
            await asyncio.gather(*tasks)
        except RateLimitExceededError as e:
            print(str(e))
        except PaymentRequiredError as e:
            print(str(e))
        except Exception as e:
            pass
            print(f"An unexpected error occurred: {e}")
