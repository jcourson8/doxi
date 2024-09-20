import asyncio
import aiohttp
import os
import urllib.parse
import ssl
import certifi
from tqdm import tqdm
from .utils import sanitize_filename, create_folder
from .utils import Text
from .errors import DoxiError, InvalidURLError, RateLimitExceededError, PaymentRequiredError
from .link_extractor import LinkExtractor
from .logging import setup_logger

class DoxiScraper:
    def __init__(
        self,
        api_key,
        max_requests_per_minute=200,
        max_concurrent_requests=2,
        flat=False,
        force=False,
    ):
        self.logger = setup_logger(__name__)
        self.api_key = api_key
        self.max_requests_per_minute = max_requests_per_minute
        self.max_concurrent_requests = max_concurrent_requests
        self.flat = flat
        self.force = force

    async def fetch(self, session: aiohttp.ClientSession, url: str) -> str:
        """Fetch the markdown content of the page using r.jina.ai API."""
        headers = (
            {
                "Authorization": f"Bearer {self.api_key}",
            }
            if self.api_key
            else None
        )
        api_url = f"https://r.jina.ai/{urllib.parse.quote(url)}"

        try:
            async with session.get(api_url, headers=headers) as response:
                if response.status == 429:
                    raise RateLimitExceededError("Rate limit exceeded")
                if response.status == 402:
                    raise PaymentRequiredError("Payment required")
                if response.status == 422:
                    raise InvalidURLError(f"Invalid URL: {url}")
                response.raise_for_status()
                text = await response.text()
                if not text:
                    self.logger.error(f"No content returned for {url}")
                    return None
                return text
        except asyncio.CancelledError:
            # Allow the task to be canceled
            raise
        except (RateLimitExceededError, PaymentRequiredError, InvalidURLError) as e:
            # Re-raise critical exceptions to be handled upstream
            raise e
        except Exception as e:
            self.logger.error(f"Failed to fetch {url}: {e}")
            return None

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
                if not content:
                    self.logger.error(f"No content returned for {link}")
                else:
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(content)
                await asyncio.sleep(rate_limit_interval)  # Wait to adhere to rate limit
            except asyncio.CancelledError:
                # Allow the task to be canceled
                raise
            except (RateLimitExceededError, PaymentRequiredError) as e:
                # Re-raise to propagate and stop processing
                raise e
            except InvalidURLError as e:
                self.logger.warning(f"Invalid URL encountered: {e}")
            except Exception as e:
                self.logger.error(f"Failed to fetch {link}: {e}")
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
        self.logger.info(f"Extracting navigation links from {url}")
        extractor = LinkExtractor(url)
        nav_links = extractor.extract_links()
        if not nav_links:
            self.logger.warning(f"No links found for {url}")
            return

        self.logger.info(f"Found {len(nav_links)} links.")

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
            self.logger.info(f"Skipping {len(links_skipped)} files that already exist.")
        if links_to_process:
            self.logger.info(f"Processing {len(links_to_process)} files.")

        if not links_to_process:
            self.logger.info("All documentation files already exist. Nothing to do.")
            return  # Exit the function

        # Create SSL context using certifi
        ssl_context = ssl.create_default_context(cafile=certifi.where())
        connector = aiohttp.TCPConnector(ssl=ssl_context)

        # Create a progress bar
        pbar = tqdm(total=len(links_to_process), desc=f"Processing {url}")

        async with aiohttp.ClientSession(connector=connector) as session:
            tasks = []
            for link, file_path in links_to_process:
                task = asyncio.create_task(
                    self.process_link(
                        session, link, file_path, sem, rate_limit_interval, pbar
                    )
                )
                tasks.append(task)

            pending = set(tasks)
            try:
                while pending:
                    done, pending = await asyncio.wait(
                        pending, return_when=asyncio.FIRST_EXCEPTION
                    )
                    for task in done:
                        exc = task.exception()
                        if exc:
                            if isinstance(exc, (RateLimitExceededError, PaymentRequiredError)):
                                for p in pending:
                                    p.cancel()
                                await asyncio.gather(*pending, return_exceptions=True)
                                raise exc
                            else:
                                # Log other exceptions but continue
                                self.logger.error(f"Task failed with exception: {exc}")
            finally:
                pbar.close()

    async def run(self, documentation_urls, output_dir="."):
        sem = asyncio.Semaphore(self.max_concurrent_requests)
        rate_limit_interval = 60 / self.max_requests_per_minute

        tasks = []
        for url in documentation_urls:
            if not url.startswith("http://") and not url.startswith("https://"):
                url = "http://" + url
                
            task = asyncio.create_task(
                self.process_documentation_site(
                    url, sem, rate_limit_interval, output_dir
                )
            )
            tasks.append(task)

        try:
            await asyncio.gather(*tasks)
        except (RateLimitExceededError, PaymentRequiredError) as e:
            self.logger.error(f"Scraper stopped due to error: {e}")
            # Optionally, cancel all tasks if not already canceled
            for task in tasks:
                task.cancel()
            await asyncio.gather(*tasks, return_exceptions=True)
        except Exception as e:
            self.logger.error(f"An unexpected error occurred: {e}")
