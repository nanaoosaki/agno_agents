---
title: Spider
category: misc
source_lines: 79809-79857
line_count: 48
---

# Spider
Source: https://docs.agno.com/tools/toolkits/web_scrape/spider



**SpiderTools** is an open source web Scraper & Crawler that returns LLM-ready data. To start using Spider, you need an API key from the [Spider dashboard](https://spider.cloud).

## Prerequisites

The following example requires the `spider-client` library.

```shell
pip install -U spider-client
```

## Example

The following agent will run a search query to get the latest news in USA and scrape the first search result. The agent will return the scraped data in markdown format.

```python cookbook/tools/spider_tools.py
from agno.agent import Agent
from agno.tools.spider import SpiderTools

agent = Agent(tools=[SpiderTools()])
agent.print_response('Can you scrape the first search result from a search on "news in USA"?', markdown=True)
```

## Toolkit Params

| Parameter     | Type  | Default | Description                                    |
| ------------- | ----- | ------- | ---------------------------------------------- |
| `max_results` | `int` | -       | The maximum number of search results to return |
| `url`         | `str` | -       | The url to be scraped or crawled               |

## Toolkit Functions

| Function | Description                           |
| -------- | ------------------------------------- |
| `search` | Searches the web for the given query. |
| `scrape` | Scrapes the given url.                |
| `crawl`  | Crawls the given url.                 |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/spider.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/spider_tools.py)


