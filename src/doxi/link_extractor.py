# link_extractor.py

import requests
from bs4 import BeautifulSoup
import urllib.parse
from .logging import setup_logger

class LinkExtractor:
    def __init__(self, base_url):
        self.logger = setup_logger(__name__)
        self.base_url = base_url

    def extract_links(self):
        # Try different strategies to extract links
        extractors = [
            self._from_sitemap,
            self._from_all_links
        ]
        for extractor in extractors:
            links = extractor()
            if links:
                return links
        return []

    def _from_sitemap(self):
        sitemap_url = urllib.parse.urljoin(self.base_url, "sitemap.xml")
        try:
            response = requests.get(sitemap_url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "xml")
            urls = [self.strip_fragment(loc.text) for loc in soup.find_all("loc")]
            self.logger.info(f"Found {len(urls)} links from sitemap")
            return urls
        except requests.exceptions.RequestException:
            self.logger.info("Sitemap not found or inaccessible")
            return []

    def _from_all_links(self):
        try:
            response = requests.get(self.base_url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "html.parser")
            
            links = []
            for a_tag in soup.find_all("a", href=True):
                href = a_tag['href']
                full_url = urllib.parse.urljoin(self.base_url, href)
                full_url = self.strip_fragment(full_url)
                if full_url.startswith(self.base_url):
                    links.append(full_url)

            links = list(set(links))  # Remove duplicates
            self.logger.info(f"Found {len(links)} links matching the base URL")
            return links
        
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Failed to extract links: {str(e)}")
            return []

    @staticmethod
    def strip_fragment(url):
        """
        Strip the fragment identifier from a URL.
        """
        parsed = urllib.parse.urlparse(url)
        return urllib.parse.urlunparse(parsed._replace(fragment=''))