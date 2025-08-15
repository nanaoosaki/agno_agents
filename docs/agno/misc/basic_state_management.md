---
title: Basic State Management
category: misc
source_lines: 23227-23247
line_count: 20
---

# Basic State Management
Source: https://docs.agno.com/examples/concepts/state/01-session-state



This is a basic agent state management example which shows how to manage and update agent state by maintaining a dynamic shopping list.

## Code

```python cookbook/agent_concepts/state/session_state.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat


def add_item(agent: Agent, item: str) -> str:
    """Add an item to the shopping list."""
    agent.session_state["shopping_list"].append(item)
    return f"The shopping list is now {agent.session_state['shopping_list']}"


