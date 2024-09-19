# doxi

**doxi** is a command-line tool designed to scrape documentation from websites and convert it into markdown files. It organizes the content into structured folders based on the URLs, making it easier to navigate and use the scraped documentation.

## Features

- Scrape documentation websites by parsing their `sitemap.xml`.
- Fetch markdown versions of pages using the `r.jina.ai` API.
- Organize content into folders based on the first path segment of URLs.
- Combine individual markdown files into a single file per group.
- Control rate limits and concurrency to respect target sites and APIs.

## Installation

### Prerequisites

- Python 3.7 or higher
- An API key from [r.jina.ai](https://r.jina.ai/)
- `uv` installed. If not, install it via:

  ```bash
  pip install uv
