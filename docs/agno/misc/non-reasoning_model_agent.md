---
title: Non-Reasoning Model Agent
category: misc
source_lines: 21802-21831
line_count: 29
---

# Non-Reasoning Model Agent
Source: https://docs.agno.com/examples/concepts/reasoning/agents/non-reasoning-model



This example demonstrates how it works when you pass a non-reasoning model as a reasoning model.
It defaults to using the default OpenAI reasoning model.
We recommend using the appropriate reasoning model or passing `reasoning=True` to use the default Chain-of-Thought reasoning.

## Code

```python cookbook/reasoning/agents/default_chain_of_thought.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat

reasoning_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    reasoning_model=OpenAIChat(
        id="gpt-4o", max_tokens=1200
    ),  # Should default to manual COT because it is not a native reasoning model
    markdown=True,
)
reasoning_agent.print_response(
    "Give me steps to write a python script for fibonacci series",
    stream=True,
    show_full_reasoning=True,
)


