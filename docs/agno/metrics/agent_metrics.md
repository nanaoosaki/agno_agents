---
title: Agent Metrics
category: metrics
source_lines: 20196-20225
line_count: 29
---

# Agent Metrics
Source: https://docs.agno.com/examples/concepts/others/agent_metrics



This example shows how to get the metrics of an agent run.

## Code

```python cookbook/agent_concepts/other/agent_metrics.py
from typing import Iterator
from agno.agent import Agent, RunResponse
from agno.models.openai import OpenAIChat
from agno.tools.yfinance import YFinanceTools
from agno.utils.pprint import pprint_run_response
from rich.pretty import pprint

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True)],
    markdown=True,
    show_tool_calls=True,
)

run_stream: Iterator[RunResponse] = agent.run(
    "What is the stock price of NVDA", stream=True
)
pprint_run_response(run_stream, markdown=True)

