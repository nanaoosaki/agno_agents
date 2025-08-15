---
title: Tool Call Limit
category: misc
source_lines: 73046-73068
line_count: 22
---

# Tool Call Limit
Source: https://docs.agno.com/tools/tool_call_limit

Learn to limit the number of tool calls an agent can make.

Limiting the number of tool calls an Agent can make is useful to prevent loops and have better control over costs and performance.

Doing this is very simple with Agno. You just need to pass the `tool_call_limit` parameter when initializing your Agent or Team.

## Example

```python
from agno.agent import Agent
from agno.models.openai.chat import OpenAIChat
from agno.tools.yfinance import YFinanceTools

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[YFinanceTools(company_news=True, cache_results=True)],
    tool_call_limit=1, # The Agent will not perform more than one tool call.
)

