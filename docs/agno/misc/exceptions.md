---
title: Exceptions
category: misc
source_lines: 71283-71333
line_count: 50
---

# Exceptions
Source: https://docs.agno.com/tools/exceptions



If after a tool call we need to "retry" the model with a different set of instructions or stop the agent, we can raise one of the following exceptions:

* `RetryAgentRun`: Use this exception when you want to retry the agent run with a different set of instructions.
* `StopAgentRun`: Use this exception when you want to stop the agent run.
* `AgentRunException`: A generic exception that can be used to retry the tool call.

This example shows how to use the `RetryAgentRun` exception to retry the agent with additional instructions.

```python retry_in_tool_call.py
from agno.agent import Agent
from agno.exceptions import RetryAgentRun
from agno.models.openai import OpenAIChat
from agno.utils.log import logger


def add_item(agent: Agent, item: str) -> str:
    """Add an item to the shopping list."""
    agent.session_state["shopping_list"].append(item)
    len_shopping_list = len(agent.session_state["shopping_list"])
    if len_shopping_list < 3:
        raise RetryAgentRun(
            f"Shopping list is: {agent.session_state['shopping_list']}. Minimum 3 items in the shopping list. "
            + f"Add {3 - len_shopping_list} more items.",
        )

    logger.info(f"The shopping list is now: {agent.session_state.get('shopping_list')}")
    return f"The shopping list is now: {agent.session_state.get('shopping_list')}"


agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    # Initialize the session state with empty shopping list
    session_state={"shopping_list": []},
    tools=[add_item],
    markdown=True,
)
agent.print_response("Add milk", stream=True)
print(f"Final session state: {agent.session_state}")
```

<Tip>
  Make sure to set `AGNO_DEBUG=True` to see the debug logs.
</Tip>


