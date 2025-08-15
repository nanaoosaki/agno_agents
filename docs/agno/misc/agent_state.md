---
title: Agent State
category: misc
source_lines: 34061-34085
line_count: 24
---

# Agent State
Source: https://docs.agno.com/examples/getting-started/agent-state



This example shows how to create an agent that maintains state across interactions. It demonstrates a simple counter mechanism, but this pattern can be extended to more complex state management like maintaining conversation context, user preferences, or tracking multi-step processes.

Example prompts to try:

* "Increment the counter 3 times and tell me the final count"
* "What's our current count? Add 2 more to it"
* "Let's increment the counter 5 times, but tell me each step"
* "Add 4 to our count and remind me where we started"
* "Increase the counter twice and summarize our journey"

## Code

```python agent_state.py
from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat


