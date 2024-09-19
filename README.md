# Doxi - Documentation Scraper

**doxi** is a command-line tool designed to scrape documentation from websites and convert it into markdown files. It organizes the content into structured folders based on the URLs, making it easier to navigate and use the scraped documentation.

## Features

- Scrape documentation websites by parsing their `sitemap.xml`.
- Fetch markdown versions of pages using the `r.jina.ai` API.
- Organize content into folders based on the first unique path segment of URLs.
- Combine individual markdown files into a single file per group.
- Control rate limits and concurrency to respect target sites and APIs.

## Installation

```bash
pip install git+https://github.com/jcourson8/doxi.git
```
## Usage

```
dox <url> [options]
```

### Arguments

- `url`: The URL of the documentation you want to scrape (required).

### Options

- `--api_key`: Your API key for r.jina.ai. If not provided, the tool will look for the `JINA_READER_KEY` environment variable, or fall back to unauthenticated mode with reduced rate limits.
- `--output_dir`: Directory to save the output (default: current directory).
- `--max_requests_per_minute`: Maximum number of requests per minute (default: 200 with API key, 20 without).
- `--max_concurrent_requests`: Maximum number of concurrent requests (default: 2).
- `--flat`: Save all files into one folder without subdirectories.
- `--force`: Force re-download of files even if they already exist.

### Examples

1. Basic usage:
   ```
   dox https://docs.example.com
   ```

2. Specify an output directory:
   ```
   dox https://docs.example.com --output_dir ./my_docs
   ```

3. Specify an api key:
    ```
    dox https://docs.example.com --api_key your_api_key 
    # or
    JINA_READER_KEY=your_api_key dox https://docs.example.com
    ```

4. Save all files in a flat structure:
   ```
   dox https://docs.example.com --flat
   ```

## API Key

For faster performance, it's recommended to use an API key from Jina AI Reader. You can obtain a free API key from https://jina.ai/reader/ (). 

To use the API key, you can either:
1. Pass it as an argument: `--api_key your_api_key`
2. Set it as an environment variable: `export JINA_READER_KEY=your_api_key`

If no API key is provided, the tool will fall back to unauthenticated mode with reduced rate limits.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```