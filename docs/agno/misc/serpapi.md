---
title: Serpapi
category: misc
source_lines: 77778-77829
line_count: 51
---

# Serpapi
Source: https://docs.agno.com/tools/toolkits/search/serpapi



**SerpApiTools** enable an Agent to search Google and YouTube for a query.

## Prerequisites

The following example requires the `google-search-results` library and an API key from [SerpApi](https://serpapi.com/).

```shell
pip install -U google-search-results
```

```shell
export SERP_API_KEY=***
```

## Example

The following agent will search Google for the query: "Whats happening in the USA" and share results.

```python cookbook/tools/serpapi_tools.py
from agno.agent import Agent
from agno.tools.serpapi import SerpApiTools

agent = Agent(tools=[SerpApiTools()])
agent.print_response("Whats happening in the USA?", markdown=True)
```

## Toolkit Params

| Parameter        | Type   | Default | Description                                                 |
| ---------------- | ------ | ------- | ----------------------------------------------------------- |
| `api_key`        | `str`  | -       | API key for authentication purposes.                        |
| `search_youtube` | `bool` | `False` | Enables the functionality to search for content on YouTube. |

## Toolkit Functions

| Function         | Description                                |
| ---------------- | ------------------------------------------ |
| `search_google`  | This function searches Google for a query. |
| `search_youtube` | Searches YouTube for a query.              |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/serpapi.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/serpapi_tools.py)


