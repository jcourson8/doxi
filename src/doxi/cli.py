import argparse
import os
import sys
from .utils import Text
from .core import DoxiScraper
from .logging import setup_logger

logger = setup_logger(__name__)

def doxi_scrape(
    url,
    api_key=None,
    output_dir=".",
    max_requests_per_minute=None,
    max_concurrent_requests=None,
    flat=False,
    force=False,
):
    """
    Scrape documentation and convert it to markdown.

    Args:
        url (str): Documentation URL to scrape.
        api_key (str, optional): Your API key for r.jina.ai.
            If not provided, will look for JINA_READER_KEY environment variable.
        output_dir (str, optional): Directory to save the output.
            Defaults to current directory.
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
        logger.warning(
            "No API key provided. Falling back to unauthenticated mode with reduced rate limits. "
            "For faster performance, get a free API key from https://jina.ai/reader/ "
            "and provide it using '--api_key' or set the 'JINA_READER_KEY' environment variable."
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

def doxi_compress(input_dir, output_file):
    """
    Compress the scraped documentation into a single file.

    Args:
        input_dir (str): Directory containing the scraped documentation.
        output_file (str): The output compressed file path.
    """
    import shutil

    shutil.make_archive(output_file.replace('.zip', ''), 'zip', input_dir)
    print(f"Compressed {input_dir} into {output_file}")

def main():
    parser = argparse.ArgumentParser(
        description="Doxi - A tool to scrape documentation and convert it to markdown."
    )

    # Create subparsers for subcommands
    subparsers = parser.add_subparsers(dest='subcommand', help='Available subcommands')

    # Define the 'compress' subcommand
    compress_parser = subparsers.add_parser('compress', help='Compress the scraped documentation into a single file.')
    compress_parser.add_argument('--input_dir', required=True, help='Directory containing the scraped documentation.')
    compress_parser.add_argument('--output_file', required=True, help='The output compressed file path.')

    # Define the default command (scrape) as a subcommand named 'scrape'
    scrape_parser = subparsers.add_parser('scrape', help='Scrape documentation and convert it to markdown.')
    scrape_parser.add_argument('url', help='Documentation URL to scrape.')
    scrape_parser.add_argument('--api_key', default=None, help='Your API key for r.jina.ai.')
    scrape_parser.add_argument('--output_dir', default='.', help='Directory to save the output.')
    scrape_parser.add_argument('--max_requests_per_minute', type=int, default=None, help='Max number of requests per minute.')
    scrape_parser.add_argument('--max_concurrent_requests', type=int, default=None, help='Max number of concurrent requests.')
    scrape_parser.add_argument('--flat', action='store_true', help='Save all files into one folder without subdirectories.')
    scrape_parser.add_argument('--force', action='store_true', help='Force re-download of files even if they already exist.')

    # Check if a subcommand was provided; if not, default to 'scrape'
    if len(sys.argv) > 1 and sys.argv[1] not in ['compress', 'scrape', '-h', '--help']:
        # Insert 'scrape' as the subcommand
        sys.argv.insert(1, 'scrape')

    # Parse the arguments
    args = parser.parse_args()

    # Handle subcommands
    if args.subcommand == 'compress':
        # Call the compress function
        doxi_compress(args.input_dir, args.output_file)
    elif args.subcommand == 'scrape':
        # Call the scrape function
        doxi_scrape(
            url=args.url,
            api_key=args.api_key,
            output_dir=args.output_dir,
            max_requests_per_minute=args.max_requests_per_minute,
            max_concurrent_requests=args.max_concurrent_requests,
            flat=args.flat,
            force=args.force,
        )
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == '__main__':
    main()