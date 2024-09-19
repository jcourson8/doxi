import asyncio
import argparse
import os

from .utils import Text
from .core import DoxiScraper

def main():
    parser = argparse.ArgumentParser(
        description='Dox - A tool to scrape documentation and convert it to markdown.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('url', help='Documentation URL to scrape.')
    parser.add_argument('--api_key', help='Your API key for r.jina.ai. If not provided, will look for JINA_READER_KEY environment variable.')
    parser.add_argument('--output_dir', default='.', help='Directory to save the output.')
    parser.add_argument('--max_requests_per_minute', type=int, help='Max number of requests per minute.')
    parser.add_argument('--max_concurrent_requests', type=int, help='Max number of concurrent requests.')
    parser.add_argument('--flat', action='store_true', help='Save all files into one folder without subdirectories.')
    parser.add_argument('--force', action='store_true', help='Force re-download of files even if they already exist.')

    args = parser.parse_args()

    # Try to get API key from argument or environment variable
    api_key = args.api_key or os.environ.get('JINA_READER_KEY')

    # Set default rate limits based on whether API key is provided
    if not api_key:
        if args.max_requests_per_minute is None:
            args.max_requests_per_minute = 20
        if args.max_concurrent_requests is None:
            args.max_concurrent_requests = 2
        print(f"{Text.Yellow}{Text.Bold}warning{Text.Reset}: ", end='')
        print(f"{Text.Bold}No API key provided. Falling back to unauthenticated mode with reduced rate limits. For faster performance, get a free API key from https://jina.ai/reader/ and provide it using '--api_key' or set the 'JINA_READER_KEY' environment variable.{Text.Reset}") 
    else:
        if args.max_requests_per_minute is None:
            args.max_requests_per_minute = 200
        if args.max_concurrent_requests is None:
            args.max_concurrent_requests = 2

    scraper = DoxiScraper(
        api_key=api_key,
        max_requests_per_minute=args.max_requests_per_minute,
        max_concurrent_requests=args.max_concurrent_requests,
        flat=args.flat,
        force=args.force
    )

    asyncio.run(scraper.run([args.url], args.output_dir))
