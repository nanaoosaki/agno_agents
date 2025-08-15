---
title: Team Example
category: misc
source_lines: 71125-71190
line_count: 65
---

# Team Example

Create a list of tools, and assign them to your Team with `set_tools`

```python add_team_tool_post_initialization.py
import random

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.team.team import Team
from agno.tools import tool
from agno.tools.calculator import CalculatorTools


agent1 = Agent(
    name="Stock Searcher",
    model=OpenAIChat("gpt-4o"),
)

agent2 = Agent(
    name="Company Info Searcher",
    model=OpenAIChat("gpt-4o"),
)

team = Team(
    name="Stock Research Team",
    mode="route",
    model=OpenAIChat("gpt-4o"),
    members=[agent1, agent2],
    tools=[CalculatorTools()],
    markdown=True,
    show_members_responses=True,
)


@tool
def get_stock_price(stock_symbol: str) -> str:
    """Get the current stock price of a stock."""
    return f"The current stock price of {stock_symbol} is {random.randint(100, 1000)}."

@tool
def get_stock_availability(stock_symbol: str) -> str:
    """Get the current availability of a stock."""
    return f"The current stock available of {stock_symbol} is {random.randint(100, 1000)}."


team.set_tools([get_stock_price, get_stock_availability])

team.print_response("What is the current stock price of NVDA?", stream=True)
team.print_response("How much stock NVDA stock is available?", stream=True)

```

<Tip>
  The `add_tool` method allows you to dynamically extend an Agent's or a Team's capabilities. This is particularly useful when you want to add tools based on user input or other runtime conditions.
  The `set_tool` method allows you to override an Agent's or a Team's capabilities. Note that this will remove any existing tools previously assigned to your Agent or Team.
</Tip>

## Related Documentation

* [Tool Decorator](/tools/tool-decorator) - Learn how to create custom tools
* [Available Toolkits](/tools/toolkits) - Explore pre-built toolkits
* [Selecting Tools](/tools/selecting-tools) - Learn how to filter tools in toolkits


