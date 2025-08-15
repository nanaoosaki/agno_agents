---
title: DuckDuckGo Search
category: misc
source_lines: 29958-29972
line_count: 14
---

# DuckDuckGo Search
Source: https://docs.agno.com/examples/concepts/tools/search/duckduckgo



## Code

```python cookbook/tools/duckduckgo_tools.py
from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(tools=[DuckDuckGoTools()], show_tool_calls=True)
agent.print_response("Whats happening in France?", markdown=True)

