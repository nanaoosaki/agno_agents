---
title: Crawl4AI
category: misc
source_lines: 79415-79460
line_count: 45
---

# Crawl4AI
Source: https://docs.agno.com/tools/toolkits/web_scrape/crawl4ai



**Crawl4aiTools** enable an Agent to perform web crawling and scraping tasks using the Crawl4ai library.

## Prerequisites

The following example requires the `crawl4ai` library.

```shell
pip install -U crawl4ai
```

## Example

The following agent will scrape the content from the [https://github.com/agno-agi/agno](https://github.com/agno-agi/agno) webpage:

```python cookbook/tools/crawl4ai_tools.py
from agno.agent import Agent
from agno.tools.crawl4ai import Crawl4aiTools

agent = Agent(tools=[Crawl4aiTools(max_length=None)], show_tool_calls=True)
agent.print_response("Tell me about https://github.com/agno-agi/agno.")
```

## Toolkit Params

| Parameter    | Type  | Default | Description                                                               |
| ------------ | ----- | ------- | ------------------------------------------------------------------------- |
| `max_length` | `int` | `1000`  | Specifies the maximum length of the text from the webpage to be returned. |

## Toolkit Functions

| Function      | Description                                                                                                                                                                                                      |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `web_crawler` | Crawls a website using crawl4ai's WebCrawler. Parameters include 'url' for the URL to crawl and an optional 'max\_length' to limit the length of extracted content. The default value for 'max\_length' is 1000. |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/crawl4ai.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/crawl4ai_tools.py)


