---
title: Composio
category: misc
source_lines: 75006-75055
line_count: 49
---

# Composio
Source: https://docs.agno.com/tools/toolkits/others/composio



[**ComposioTools**](https://docs.composio.dev/framework/phidata) enable an Agent to work with tools like Gmail, Salesforce, Github, etc.

## Prerequisites

The following example requires the `composio-agno` library.

```shell
pip install composio-agno
composio add github # Login into Github
```

## Example

The following agent will use Github Tool from Composio Toolkit to star a repo.

```python cookbook/tools/composio_tools.py
from agno.agent import Agent
from composio_agno import Action, ComposioToolSet


toolset = ComposioToolSet()
composio_tools = toolset.get_tools(
  actions=[Action.GITHUB_STAR_A_REPOSITORY_FOR_THE_AUTHENTICATED_USER]
)

agent = Agent(tools=composio_tools, show_tool_calls=True)
agent.print_response("Can you star agno-agi/agno repo?")
```

## Toolkit Params

The following parameters are used when calling the GitHub star repository action:

| Parameter | Type  | Default | Description                          |
| --------- | ----- | ------- | ------------------------------------ |
| `owner`   | `str` | -       | The owner of the repository to star. |
| `repo`    | `str` | -       | The name of the repository to star.  |

## Toolkit Functions

Composio Toolkit provides 1000+ functions to connect to different software tools.
Open this [link](https://composio.dev/tools) to view the complete list of functions.


