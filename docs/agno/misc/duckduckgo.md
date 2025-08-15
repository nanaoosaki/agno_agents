---
title: DuckDuckGo
category: misc
source_lines: 77371-77421
line_count: 50
---

# DuckDuckGo
Source: https://docs.agno.com/tools/toolkits/search/duckduckgo



**DuckDuckGo** enables an Agent to search the web for information.

## Prerequisites

The following example requires the `duckduckgo-search` library. To install DuckDuckGo, run the following command:

```shell
pip install -U duckduckgo-search
```

## Example

```python cookbook/tools/duckduckgo.py
from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(tools=[DuckDuckGoTools()], show_tool_calls=True)
agent.print_response("Whats happening in France?", markdown=True)
```

## Toolkit Params

| Parameter           | Type   | Default | Description                                                                                          |
| ------------------- | ------ | ------- | ---------------------------------------------------------------------------------------------------- |
| `search`            | `bool` | `True`  | Enables the use of the `duckduckgo_search` function to search DuckDuckGo for a query.                |
| `news`              | `bool` | `True`  | Enables the use of the `duckduckgo_news` function to fetch the latest news via DuckDuckGo.           |
| `fixed_max_results` | `int`  | -       | Sets a fixed number of maximum results to return. No default is provided, must be specified if used. |
| `headers`           | `Any`  | -       | Accepts any type of header values to be sent with HTTP requests.                                     |
| `proxy`             | `str`  | -       | Specifies a single proxy address as a string to be used for the HTTP requests.                       |
| `proxies`           | `Any`  | -       | Accepts a dictionary of proxies to be used for HTTP requests.                                        |
| `timeout`           | `int`  | `10`    | Sets the timeout for HTTP requests, in seconds.                                                      |

## Toolkit Functions

| Function            | Description                                               |
| ------------------- | --------------------------------------------------------- |
| `duckduckgo_search` | Use this function to search DuckDuckGo for a query.       |
| `duckduckgo_news`   | Use this function to get the latest news from DuckDuckGo. |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/duckduckgo.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/duckduckgo_tools.py)


