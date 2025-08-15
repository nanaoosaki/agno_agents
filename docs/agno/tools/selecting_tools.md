---
title: Selecting tools
category: tools
source_lines: 72856-72910
line_count: 54
---

# Selecting tools
Source: https://docs.agno.com/tools/selecting-tools



You can specify which tools to include or exclude from a `Toolkit` by using the `include_tools` and `exclude_tools` parameters. This can be very useful to limit the number of tools that are available to an Agent.

For example, here's how to include only the `get_latest_emails` tool in the `GmailTools` toolkit:

```python
agent = Agent(
    tools=[GmailTools(include_tools=["get_latest_emails"])],
)
```

Similarly, here's how to exclude the `create_draft_email` tool from the `GmailTools` toolkit:

```python
agent = Agent(
    tools=[GmailTools(exclude_tools=["create_draft_email"])],
)
```

## Example

Here's an example of how to use the `include_tools` and `exclude_tools` parameters to limit the number of tools that are available to an Agent:

```python include_exclude_tools.py

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.calculator import CalculatorTools
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[
        CalculatorTools(
            enable_all=True,
            exclude_tools=["exponentiate", "factorial", "is_prime", "square_root"],
        ),
        DuckDuckGoTools(include_tools=["duckduckgo_search"]),
    ],
    show_tool_calls=True,
    markdown=True,
)

agent.print_response(
    "Search the web for a difficult sum that can be done with normal arithmetic and solve it.",
)
```


