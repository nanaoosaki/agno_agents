---
title: Firecrawl
category: misc
source_lines: 79460-79520
line_count: 60
---

# Firecrawl
Source: https://docs.agno.com/tools/toolkits/web_scrape/firecrawl

Use Firecrawl with Agno to scrape and crawl the web.

**FirecrawlTools** enable an Agent to perform web crawling and scraping tasks.

## Prerequisites

The following example requires the `firecrawl-py` library and an API key which can be obtained from [Firecrawl](https://firecrawl.dev).

```shell
pip install -U firecrawl-py
```

```shell
export FIRECRAWL_API_KEY=***
```

## Example

The following agent will scrape the content from [https://finance.yahoo.com/](https://finance.yahoo.com/) and return a summary of the content:

```python cookbook/tools/firecrawl_tools.py
from agno.agent import Agent
from agno.tools.firecrawl import FirecrawlTools

agent = Agent(tools=[FirecrawlTools(scrape=False, crawl=True)], show_tool_calls=True, markdown=True)
agent.print_response("Summarize this https://finance.yahoo.com/")
```

## Toolkit Params

| Parameter       | Type             | Default | Description                                                                                           |
| --------------- | ---------------- | ------- | ----------------------------------------------------------------------------------------------------- |
| `api_key`       | `str`            | `None`  | Optional API key for authentication purposes. Falls back to FIRECRAWL\_API\_KEY environment variable. |
| `formats`       | `List[str]`      | `None`  | Optional list of formats to be used for the operation.                                                |
| `limit`         | `int`            | `10`    | Maximum number of items to retrieve. The default value is 10.                                         |
| `poll_interval` | `int`            | `30`    | Interval in seconds between polling for results.                                                      |
| `scrape`        | `bool`           | `True`  | Enables the scraping functionality. Default is True.                                                  |
| `crawl`         | `bool`           | `False` | Enables the crawling functionality. Default is False.                                                 |
| `mapping`       | `bool`           | `False` | Enables the website mapping functionality.                                                            |
| `search`        | `bool`           | `False` | Enables the web search functionality.                                                                 |
| `search_params` | `Dict[str, Any]` | `None`  | Optional parameters for search operations.                                                            |

## Toolkit Functions

| Function         | Description                                                                                                                                                                                                                                             |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `scrape_website` | Scrapes a website using Firecrawl. Parameters include `url` to specify the URL to scrape. The function supports optional formats if specified. Returns the results of the scraping in JSON format.                                                      |
| `crawl_website`  | Crawls a website using Firecrawl. Parameters include `url` to specify the URL to crawl, and an optional `limit` to define the maximum number of pages to crawl. The function supports optional formats and returns the crawling results in JSON format. |
| `map_website`    | Maps a website structure using Firecrawl. Parameters include `url` to specify the URL to map. Returns the mapping results in JSON format.                                                                                                               |
| `search`         | Performs a web search using Firecrawl. Parameters include `query` for the search term and optional `limit` for maximum results. Returns search results in JSON format.                                                                                  |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/firecrawl.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/firecrawl_tools.py)


