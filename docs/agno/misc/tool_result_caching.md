---
title: Tool Result Caching
category: misc
source_lines: 71190-71227
line_count: 37
---

# Tool Result Caching
Source: https://docs.agno.com/tools/caching



Tool result caching is designed to avoid unnecessary recomputation by storing the results of function calls on disk.
This is useful during development and testing to speed up the development process, avoid rate limiting, and reduce costs.

This is supported for all Agno Toolkits

## Example

Pass `cache_results=True` to the Toolkit constructor to enable caching for that Toolkit.

```python cache_tool_calls.py
import asyncio

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[DuckDuckGoTools(cache_results=True), YFinanceTools(cache_results=True)],
    show_tool_calls=True,
)

asyncio.run(
    agent.aprint_response(
        "What is the current stock price of AAPL and latest news on 'Apple'?",
        markdown=True,
    )
)
```


