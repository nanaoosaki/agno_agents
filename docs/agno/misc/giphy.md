---
title: Giphy
category: misc
source_lines: 75724-75776
line_count: 52
---

# Giphy
Source: https://docs.agno.com/tools/toolkits/others/giphy



**GiphyTools** enables an Agent to search for GIFs on GIPHY.

## Prerequisites

```shell
export GIPHY_API_KEY=***
```

## Example

The following agent will search GIPHY for a GIF appropriate for a birthday message.

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.giphy import GiphyTools


gif_agent = Agent(
    name="Gif Generator Agent",
    model=OpenAIChat(id="gpt-4o"),
    tools=[GiphyTools()],
    description="You are an AI agent that can generate gifs using Giphy.",
)

gif_agent.print_response("I want a gif to send to a friend for their birthday.")
```

## Toolkit Params

| Parameter | Type  | Default | Description                                       |
| --------- | ----- | ------- | ------------------------------------------------- |
| `api_key` | `str` | `None`  | If you want to manually supply the GIPHY API key. |
| `limit`   | `int` | `1`     | The number of GIFs to return in a search.         |

## Toolkit Functions

| Function      | Description                                         |
| ------------- | --------------------------------------------------- |
| `search_gifs` | Searches GIPHY for a GIF based on the query string. |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/giphy.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/giphy_tools.py)


