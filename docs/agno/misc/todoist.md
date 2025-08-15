---
title: Todoist
category: misc
source_lines: 76807-76867
line_count: 60
---

# Todoist
Source: https://docs.agno.com/tools/toolkits/others/todoist



**TodoistTools** enables an Agent to interact with [Todoist](https://www.todoist.com/).

## Prerequisites

The following example requires the `todoist-api-python` library. and a Todoist API token which can be obtained from the [Todoist Developer Portal](https://app.todoist.com/app/settings/integrations/developer).

```shell
pip install todoist-api-python
```

```shell
export TODOIST_API_TOKEN=***
```

## Example

The following agent will create a new task in Todoist.

```python cookbook/tools/todoist.py
"""
Example showing how to use the Todoist Tools with Agno

Requirements:
- Sign up/login to Todoist and get a Todoist API Token (get from https://app.todoist.com/app/settings/integrations/developer)
- pip install todoist-api-python

Usage:
- Set the following environment variables:
    export TODOIST_API_TOKEN="your_api_token"

- Or provide them when creating the TodoistTools instance
"""

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.todoist import TodoistTools

todoist_agent = Agent(
    name="Todoist Agent",
    role="Manage your todoist tasks",
    instructions=[
        "When given a task, create a todoist task for it.",
        "When given a list of tasks, create a todoist task for each one.",
        "When given a task to update, update the todoist task.",
        "When given a task to delete, delete the todoist task.",
        "When given a task to get, get the todoist task.",
    ],
    agent_id="todoist-agent",
    model=OpenAIChat(id="gpt-4o"),
    tools=[TodoistTools()],
    markdown=True,
    debug_mode=True,
    show_tool_calls=True,
)

