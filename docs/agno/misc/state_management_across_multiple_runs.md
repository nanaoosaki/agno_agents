---
title: State Management Across Multiple Runs
category: misc
source_lines: 23591-23607
line_count: 16
---

# State Management Across Multiple Runs
Source: https://docs.agno.com/examples/concepts/state/05-session-state-full-example



This example demonstrates how to build a stateful agent that can manage its state across multiple runs.

## Code

```python cookbook/agent_concepts/state/shopping_list.py
from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat


