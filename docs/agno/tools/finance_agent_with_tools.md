---
title: Finance Agent with Tools
category: tools
source_lines: 43494-43523
line_count: 29
---

# Finance Agent with Tools
Source: https://docs.agno.com/examples/models/langdb/tool_use



This example demonstrates tool usage with [LangDB AI Gateway](https://langdb.ai/).

For detailed integration instructions, see the [LangDB Agno documentation](https://docs.langdb.ai/getting-started/working-with-agent-frameworks/working-with-agno).

## Code

```python cookbook/models/langdb/finance_agent.py
from agno.agent import Agent
from agno.models.langdb import LangDB
from agno.tools.yfinance import YFinanceTools

agent = Agent(
    model=LangDB(id="gpt-4o-mini"),
    tools=[
        YFinanceTools(
            stock_price=True, analyst_recommendations=True, stock_fundamentals=True
        )
    ],
    show_tool_calls=True,
    description="You are an investment analyst that researches stocks and helps users make informed decisions.",
    instructions=["Use tables to display data where possible."],
    markdown=True,
)

