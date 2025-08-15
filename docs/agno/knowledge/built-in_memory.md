---
title: Built-in Memory
category: knowledge
source_lines: 16489-16510
line_count: 21
---

# Built-in Memory
Source: https://docs.agno.com/examples/concepts/memory/00-built-in-memory



## Code

```python cookbook/agent_concepts/memory/00_builtin_memory.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from rich.pretty import pprint

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    # Set add_history_to_messages=true to add the previous chat history to the messages sent to the Model.
    add_history_to_messages=True,
    # Number of historical responses to add to the messages.
    num_history_responses=3,
    description="You are a helpful assistant that always responds in a polite, upbeat and positive manner.",
)

