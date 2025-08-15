---
title: Oxylabs
category: misc
source_lines: 79662-79741
line_count: 79
---

# Oxylabs
Source: https://docs.agno.com/tools/toolkits/web_scrape/oxylabs



OxylabsTools provide Agents with access to Oxylabs' powerful web scraping capabilities, including SERP, Amazon product data, and universal web scraping endpoints.

## Prerequisites

```shell
pip install -U oxylabs-sdk
```

Set your credentials as environment variables (recommended):

```shell
export OXYLABS_USERNAME=your_oxylabs_username
export OXYLABS_PASSWORD=your_oxylabs_password
```

## Examples

### iPhone Reviews

```python
from agno.agent import Agent
from agno.tools.oxylabs import OxylabsTools

agent = Agent(
    tools=[OxylabsTools()],
    markdown=True,
    show_tool_calls=True,
)

agent.print_response("""
Search for 'latest iPhone reviews' and provide a summary of the top 3 results. 
""")
```

### Amazon Product Search

```python
from agno.agent import Agent
from agno.tools.oxylabs import OxylabsTools

agent = Agent(
    tools=[OxylabsTools()],
    markdown=True,
    show_tool_calls=True,
)

agent.print_response(
    "Let's search for an Amazon product with ASIN code 'B07FZ8S74R' ",
 )
```

## Toolkit Params

| Parameter  | Type  | Default | Description                                                                             |
| ---------- | ----- | ------- | --------------------------------------------------------------------------------------- |
| `username` | `str` | `None`  | Oxylabs dashboard username. If not provided, it defaults to `OXYLABS_USERNAME` env var. |
| `password` | `str` | `None`  | Oxylabs dashboard password. If not provided, it defaults to `OXYLABS_PASSWORD` env var. |

## Toolkit Functions

| Function                 | Description                                                                                            |
| ------------------------ | ------------------------------------------------------------------------------------------------------ |
| `search_google`          | Performs a Google SERP search. Accepts all the standard Oxylabs params (e.g. `query`, `geo_location`). |
| `get_amazon_product`     | Retrieves the details of Amazon product(s). Accepts ASIN code or full product URL.                     |
| `search_amazon_products` | Searches for Amazon product(s) using a search term.                                                    |
| `scrape_website`         | Scrapes a webpage URL.                                                                                 |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/oxylabs.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/oxylabs_tools.py)
* View [Oxylabs MCP Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/mcp/oxylabs.py)


