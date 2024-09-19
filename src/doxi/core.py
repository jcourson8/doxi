import asyncio
import aiohttp
import os
import requests
import urllib.parse
import logging
import ssl
import certifi
from bs4 import BeautifulSoup
from .utils import sanitize_filename, group_links_by_first_non_common_path_segment, create_folder
from tqdm import tqdm

logging.basicConfig(level=logging.INFO)

class doxiScraper:
    def __init__(self, api_key, max_requests_per_minute=200, max_concurrent_requests=2):
        self.api_key = api_key
        self.max_requests_per_minute = max_requests_per_minute
        self.max_concurrent_requests = max_concurrent_requests

    def get_links_from_sitemap(self, url):
        sitemap_url = urllib.parse.urljoin(url, 'sitemap.xml')
        try:
            response = requests.get(sitemap_url, timeout=10)
            response.raise_for_status()
            logging.info(f"Sitemap found at {sitemap_url}")
            soup = BeautifulSoup(response.content, 'xml')
            urls = [loc.text for loc in soup.find_all('loc')]
            return urls
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching sitemap: {e}")
            return []

    async def fetch(self, session: aiohttp.ClientSession, url: str) -> str:
        """Fetch the markdown content of the page using r.jina.ai API."""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
        } if self.api_key else None
        # Prepare the r.jina.ai API endpoint
        api_url = f"https://r.jina.ai/{urllib.parse.quote(url)}"
        async with session.get(api_url, headers=headers) as response:
            response.raise_for_status()
            return await response.text()

    async def process_link(self, session: aiohttp.ClientSession, link: str, save_path: str, sem: asyncio.Semaphore, rate_limit_interval: float, pbar):
        """Process an individual link."""
        # Create a valid file name from the link
        file_name = sanitize_filename(link) + ".md"
        file_path = os.path.join(save_path, file_name)

        # Check if the file already exists
        if os.path.isfile(file_path):
            print(f"File {file_name} already exists. Skipping download.")
            pbar.update(1)
            return  # Skip if already downloaded

        async with sem:
            try:
                content = await self.fetch(session, link)
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
                await asyncio.sleep(rate_limit_interval)  # Wait to adhere to rate limit
            except Exception as e:
                print(f"Failed to fetch {link}: {e}")
            finally:
                pbar.update(1)

    async def process_documentation_site(self, url: str, sem: asyncio.Semaphore, rate_limit_interval: float, output_dir: str = '.'):
        """Process an entire documentation site."""
        print(f"Extracting navigation links from {url}")
        nav_links = self.get_links_from_sitemap(url)
        print(f"Found {len(nav_links)} links.")

        # Remove duplicate links
        nav_links = list(set(nav_links))

        # Group links based on the first non-common path segment
        grouped_links = group_links_by_first_non_common_path_segment(nav_links)

        # Create base folder for this documentation site
        parsed_url = urllib.parse.urlparse(url)
        base_folder_name = os.path.join(output_dir, parsed_url.netloc)
        create_folder(base_folder_name)

        # Create SSL context using certifi
        ssl_context = ssl.create_default_context(cafile=certifi.where())
        connector = aiohttp.TCPConnector(ssl=ssl_context)

        # Create a progress bar
        pbar = tqdm(total=len(nav_links), desc=f"Processing {url}")

        async with aiohttp.ClientSession(connector=connector) as session:
            tasks = []
            for group_name, group_links in grouped_links.items():
                group_folder = os.path.join(base_folder_name, group_name)
                create_folder(group_folder)
                for link in group_links:
                    tasks.append(self.process_link(session, link, group_folder, sem, rate_limit_interval, pbar))

            # Run tasks with asyncio.gather
            await asyncio.gather(*tasks)

        pbar.close()

        # After processing all links, concatenate the files per group
        for group_name, group_links in grouped_links.items():
            group_folder = os.path.join(base_folder_name, group_name)
            concat_file_path = os.path.join(group_folder, f"{group_name}_combined.md")
            with open(concat_file_path, "w", encoding="utf-8") as outfile:
                for link in group_links:
                    file_name = sanitize_filename(link) + ".md"
                    file_path = os.path.join(group_folder, file_name)
                    if os.path.isfile(file_path):
                        with open(file_path, "r", encoding="utf-8") as infile:
                            outfile.write(infile.read())
                            outfile.write("\n\n")  # Add spacing between files

    async def run(self, documentation_urls, output_dir='.'):
        sem = asyncio.Semaphore(self.max_concurrent_requests)  # Control max concurrent requests
        rate_limit_interval = 60 / self.max_requests_per_minute  # Time between requests

        tasks = []
        for url in documentation_urls:
            tasks.append(self.process_documentation_site(url, sem, rate_limit_interval, output_dir))

        await asyncio.gather(*tasks)
