---
title: Running your Agent
category: core
source_lines: 1513-1534
line_count: 21
---

# Running your Agent
Source: https://docs.agno.com/agents/run

Learn how to run an agent and get the response.

The `Agent.run()` function runs the agent and generates a response, either as a `RunResponse` object or a stream of `RunResponse` objects.

Many of our examples use `agent.print_response()` which is a helper utility to print the response in the terminal. It uses `agent.run()` under the hood.

## Running your Agent

Here's how to run your agent. The response is captured in the `response`.

```python
from typing import Iterator
from agno.agent import Agent, RunResponse
from agno.models.openai import OpenAIChat
from agno.utils.pprint import pprint_run_response

agent = Agent(model=OpenAIChat(id="gpt-4o-mini"))

