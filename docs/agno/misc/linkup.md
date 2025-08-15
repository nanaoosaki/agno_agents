---
title: Linkup
category: misc
source_lines: 77623-77674
line_count: 51
---

# Linkup
Source: https://docs.agno.com/tools/toolkits/search/linkup

The toolkit enables an Agent to search the web using the Linkup API

**LinkupTools** enable an Agent to search the web using the Linkup API, the World's best search for AI Apps.

## Prerequisites

The following examples requires the [linkup-sdk](https://github.com/LinkupPlatform/linkup-python-sdk) library and an API key from [Linkup](https://www.linkup.so).

```shell
pip install -U linkup-sdk
```

```shell
export LINKUP_API_KEY=***
```

## Example

The following agent will search the web for the latest news in French politics and print the response.

```python cookbook/tools/linkup_tools.py
from agno.agent import Agent
from agno.tools.linkup import LinkupTools

agent = Agent(tools=[LinkupTools()], show_tool_calls=True)
agent.print_response("What's the latest news in French politics?", markdown=True)
```

## Toolkit Functions

| Function                 | Description                                                                                                                                         |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `web_search_with_linkup` | Searches the web for a query using Linkup API. Takes a query string and optional depth/output\_type parameters. Returns search results as a string. |

## Toolkit Parameters

| Parameter     | Type                                        | Default           | Description                                                                                                                                                                                                       |
| ------------- | ------------------------------------------- | ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `api_key`     | `Optional[str]`                             | `None`            | API key for authentication. If not provided, will check LINKUP\_API\_KEY environment variable.                                                                                                                    |
| `depth`       | `Literal["standard", "deep"]`               | `"standard"`      | Depth of the search. Use 'standard' for fast and affordable web search or 'deep' for comprehensive, in-depth web search.                                                                                          |
| `output_type` | `Literal["sourcedAnswer", "searchResults"]` | `"searchResults"` | Type of output. 'sourcedAnswer' provides a comprehensive natural language answer to the query along with citations to the source material. 'searchResults' returns the raw search context data without synthesis. |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/linkup.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/linkup_tools.py)


