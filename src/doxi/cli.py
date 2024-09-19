import fire
import os
from .utils import Text
from .core import DoxiScraper


def doxi(
    url: str,
    api_key: str = None,
    output_dir: str = ".",
    max_requests_per_minute: int = None,
    max_concurrent_requests: int = None,
    flat=False,
    force=False,
):
    """
    Scrape documentation and convert it to markdown.

    Args:
        url (str): Documentation URL to scrape.
        api_key (str, optional): Your API key for r.jina.ai. If not provided, will look for JINA_READER_KEY environment variable.
        output_dir (str, optional): Directory to save the output. Defaults to current directory.
        max_requests_per_minute (int, optional): Max number of requests per minute.
        max_concurrent_requests (int, optional): Max number of concurrent requests.
        flat (bool, optional): Save all files into one folder without subdirectories.
        force (bool, optional): Force re-download of files even if they already exist.
    """
    # Try to get API key from argument or environment variable
    api_key = api_key or os.environ.get("JINA_READER_KEY")

    # Set default rate limits based on whether API key is provided
    if not api_key:
        max_requests_per_minute = max_requests_per_minute or 20
        max_concurrent_requests = max_concurrent_requests or 2
        print(f"{Text.Yellow}{Text.Bold}warning{Text.Reset}: ", end="")
        print(
            f"{Text.Bold}No API key provided. Falling back to unauthenticated mode with reduced rate limits. For faster performance, get a free API key from https://jina.ai/reader/ and provide it using '--api_key' or set the 'JINA_READER_KEY' environment variable.{Text.Reset}"
        )
    else:
        max_requests_per_minute = max_requests_per_minute or 200
        max_concurrent_requests = max_concurrent_requests or 2

    scraper = DoxiScraper(
        api_key=api_key,
        max_requests_per_minute=max_requests_per_minute,
        max_concurrent_requests=max_concurrent_requests,
        flat=flat,
        force=force,
    )

    import asyncio

    asyncio.run(scraper.run([url], output_dir))

def cli():
    fire.Fire(doxi)