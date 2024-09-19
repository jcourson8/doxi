# doxi/cli.py

import asyncio
import argparse
import os
from .core import doxiScraper

def main():
    parser = argparse.ArgumentParser(
        description='doxi - A tool to scrape documentation and convert it to markdown.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('--api_key', help='Your API key for r.jina.ai.')
    parser.add_argument('--url', required=True, help='Documentation URL to scrape.')
    parser.add_argument('--output_dir', default='.', help='Directory to save the output.')
    parser.add_argument('--max_requests_per_minute', type=int, default=200, help='Max number of requests per minute.')
    parser.add_argument('--max_concurrent_requests', type=int, default=2, help='Max number of concurrent requests.')

    args = parser.parse_args()

    # Try to get API key from argument or environment variable
    api_key = args.api_key or os.environ.get('JINA_READER_KEY')

    # If API key is not provided, adjust rate limits and notify the user
    if not api_key:
        print("No API key provided. Falling back to unauthenticated mode with reduced rate limits.\n")
        print("For faster performance, get a free API key from https://jina.ai/reader/ and provide it using '--api_key' or set the 'JINA_READER_KEY' environment variable.\n")
        # Override max_requests_per_minute to 20
        args.max_requests_per_minute = 20

    scraper = doxiScraper(
        api_key=api_key,
        max_requests_per_minute=args.max_requests_per_minute,
        max_concurrent_requests=args.max_concurrent_requests
    )

    asyncio.run(scraper.run([args.url], args.output_dir))
