---
title: Webex Tools
category: tools
source_lines: 30797-30822
line_count: 25
---

# Webex Tools
Source: https://docs.agno.com/examples/concepts/tools/social/webex



## Code

```python cookbook/tools/webex_tools.py
from agno.agent import Agent
from agno.tools.webex import WebexTools

agent = Agent(
    name="Webex Assistant",
    tools=[WebexTools()],
    description="You are a Webex assistant that can send messages and manage spaces.",
    instructions=[
        "You can help users by:",
        "- Listing available Webex spaces",
        "- Sending messages to spaces",
        "Always confirm the space exists before sending messages.",
    ],
    show_tool_calls=True,
    markdown=True,
)

