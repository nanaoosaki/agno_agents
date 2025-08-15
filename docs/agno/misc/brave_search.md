---
title: Brave Search
category: misc
source_lines: 77315-77371
line_count: 56
---

# Brave Search
Source: https://docs.agno.com/tools/toolkits/search/bravesearch



**BraveSearch** enables an Agent to search the web for information using the Brave search engine.

## Prerequisites

The following examples requires the `brave-search` library.

```shell
pip install -U brave-search
```

```shell
export BRAVE_API_KEY=***
```

## Example

```python cookbook/tools/bravesearch_tools.py
from agno.agent import Agent
from agno.tools.bravesearch import BraveSearchTools

agent = Agent(
    tools=[BraveSearchTools()],
    description="You are a news agent that helps users find the latest news.",
    instructions=[
        "Given a topic by the user, respond with 4 latest news items about that topic."
    ],
    show_tool_calls=True,
)
agent.print_response("AI Agents", markdown=True)

```

## Toolkit Params

| Parameter           | Type  | Default | Description                                         |
| ------------------- | ----- | ------- | --------------------------------------------------- |
| `fixed_max_results` | `int` | `None`  | Optional fixed maximum number of results to return. |
| `fixed_language`    | `str` | `None`  | Optional fixed language for the requests.           |

## Toolkit Functions

| Function       | Description                                                                                                                                                                                                                                                                                                                                                      |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `brave_search` | Searches Brave for a specified query. Parameters include `query` for the search term, `max_results` for the maximum number of results (default is 5),`country` for the geographic region (default is "US") of the search results and `language` for the language of the search results (default is "en"). Returns the search results as a JSON formatted string. |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/bravesearch.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/bravesearch_tools.py)


