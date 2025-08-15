---
title: Handle confirmation
category: misc
source_lines: 2742-2800
line_count: 58
---

# Handle confirmation
if agent.is_paused:
    for tool in agent.run_response.tools_requiring_confirmation:
        # Get user confirmation
        print(f"Tool {tool.tool_name}({tool.tool_args}) requires confirmation")
        confirmed = input(f"Confirm? (y/n): ").lower() == "y"
        tool.confirmed = confirmed

  # Continue execution
  response = agent.continue_run()
```

You can also specify which tools in a toolkit require confirmation.

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools import tool
from agno.tools.yfinance import YFinanceTools
from agno.utils import pprint

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[YFinanceTools(requires_confirmation_tools=["get_current_stock_price"])],
)

agent.run("What is the current stock price of Apple?")
if agent.is_paused:
    for tool in agent.run_response.tools_requiring_confirmation:
        print(f"Tool {tool.tool_name}({tool.tool_args}) requires confirmation")
        confirmed = input(f"Confirm? (y/n): ").lower() == "y"

        if message == "n":
            tool.confirmed = False
        else:
            # We update the tools in place
            tool.confirmed = True

    run_response = agent.continue_run()
    pprint.pprint_run_response(run_response)
```

## User Input

User input flows allow you to gather specific information from users during execution. This is useful for:

* Collecting required parameters
* Getting user preferences
* Gathering missing information

In the example below, we require all the input for the `send_email` tool from the user.

```python
from typing import List
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.function import UserInputField

