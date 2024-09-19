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
            self._from_navigation,
            self._from_custom_logic,
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
            urls = [loc.text for loc in soup.find_all("loc")]
            self.logger.info(f"Found {len(urls)} links from sitemap")
            return urls
        except requests.exceptions.RequestException:
            self.logger.info("Sitemap not found or inaccessible")
            return []

    def _from_navigation(self):
        try:
            response = requests.get(self.base_url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "html.parser")
            links = []
            for a_tag in soup.find_all("a", href=True):
                href = a_tag['href']
                full_url = urllib.parse.urljoin(self.base_url, href)
                if full_url.startswith(self.base_url):
                    links.append(full_url)
            links = list(set(links))  # Remove duplicates
            self.logger.info(f"Found {len(links)} links from navigation")
            return links
        except requests.exceptions.RequestException:
            self.logger.info("Failed to extract links from navigation")
            return []

    def _from_custom_logic(self):
        parsed_url = urllib.parse.urlparse(self.base_url)
        if "github.io" in parsed_url.netloc:
            return self._extract_github_io_links()
        return []

    def _extract_github_io_links(self):
        # Custom logic for github.io sites
        try:
            response = requests.get(self.base_url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "html.parser")
            # Assume that documentation pages are linked in the sidebar or main content
            content = soup.find('div', {'class': 'sidebar'}) or soup.find('div', {'class': 'content'})
            if not content:
                return []
            links = []
            for a_tag in content.find_all("a", href=True):
                href = a_tag['href']
                full_url = urllib.parse.urljoin(self.base_url, href)
                if full_url.startswith(self.base_url):
                    links.append(full_url)
            links = list(set(links))
            self.logger.info(f"Found {len(links)} links from custom GitHub.io logic")
            return links
        except requests.exceptions.RequestException:
            self.logger.info("Failed to extract links from custom GitHub.io logic")
            return []
