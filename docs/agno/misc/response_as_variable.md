---
title: Response as Variable
category: misc
source_lines: 20859-20893
line_count: 34
---

# Response as Variable
Source: https://docs.agno.com/examples/concepts/others/response_as_variable



This example shows how to use the response of an agent as a variable.

## Code

```python cookbook/agent_concepts/other/response_as_variable.py
from typing import Iterator
from rich.pretty import pprint
from agno.agent import Agent, RunResponse
from agno.models.openai import OpenAIChat
from agno.tools.yfinance import YFinanceTools

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            company_info=True,
            company_news=True,
        )
    ],
    instructions=["Use tables where possible"],
    show_tool_calls=True,
    markdown=True,
)

run_response: RunResponse = agent.run("What is the stock price of NVDA")
pprint(run_response)

