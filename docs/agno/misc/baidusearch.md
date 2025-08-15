---
title: BaiduSearch
category: misc
source_lines: 77258-77315
line_count: 57
---

# BaiduSearch
Source: https://docs.agno.com/tools/toolkits/search/baidusearch



**BaiduSearch** enables an Agent to search the web for information using the Baidu search engine.

## Prerequisites

The following example requires the `baidusearch` library. To install BaiduSearch, run the following command:

```shell
pip install -U baidusearch
```

## Example

```python cookbook/tools/baidusearch_tools.py
from agno.agent import Agent
from agno.tools.baidusearch import BaiduSearchTools

agent = Agent(
    tools=[BaiduSearchTools()],
    description="You are a search agent that helps users find the most relevant information using Baidu.",
    instructions=[
        "Given a topic by the user, respond with the 3 most relevant search results about that topic.",
        "Search for 5 results and select the top 3 unique items.",
        "Search in both English and Chinese.",
    ],
    show_tool_calls=True,
)

agent.print_response("What are the latest advancements in AI?", markdown=True)
```

## Toolkit Params

| Parameter           | Type  | Default | Description                                                                                          |
| ------------------- | ----- | ------- | ---------------------------------------------------------------------------------------------------- |
| `fixed_max_results` | `int` | -       | Sets a fixed number of maximum results to return. No default is provided, must be specified if used. |
| `fixed_language`    | `str` | -       | Set the fixed language for the results.                                                              |
| `headers`           | `Any` | -       | Headers to be used in the search request.                                                            |
| `proxy`             | `str` | -       | Specifies a single proxy address as a string to be used for the HTTP requests.                       |
| `timeout`           | `int` | `10`    | Sets the timeout for HTTP requests, in seconds.                                                      |

## Toolkit Functions

| Function       | Description                                    |
| -------------- | ---------------------------------------------- |
| `baidu_search` | Use this function to search Baidu for a query. |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/baidusearch.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/baidusearch_tools.py)


