---
title: Basic Async
category: misc
source_lines: 11116-11135
line_count: 19
---

# Basic Async
Source: https://docs.agno.com/examples/concepts/async/basic



## Code

```python cookbook/agent_concepts/async/basic.py
import asyncio

from agno.agent import Agent
from agno.models.openai import OpenAIChat

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="You help people with their health and fitness goals.",
    instructions=["Recipes should be under 5 ingredients"],
    markdown=True,
)
