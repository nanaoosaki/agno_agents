---
title: User Control Flows
category: misc
source_lines: 2672-2739
line_count: 67
---

# User Control Flows
Source: https://docs.agno.com/agents/user-control-flow

Learn how to control the flow of an agent's execution in Agno. This is also called "Human in the Loop".

User control flows in Agno enable you to implement "Human in the Loop" patterns, where human oversight and input are required during agent execution. This is crucial for:

* Validating sensitive operations
* Reviewing tool calls before execution
* Gathering user input for decision-making
* Managing external tool execution

## Types of User Control Flows

Agno supports four main types of user control flows:

1. **User Confirmation**: Require explicit user approval before executing tool calls
2. **User Input**: Gather specific information from users during execution
3. **Dynamic User Input**: Have the agent collect user input as it needs it
4. **External Tool Execution**: Execute tools outside of the agent's control

## Pausing Agent Execution

User control flows interrupt the agent's execution and require human oversight. The run can then be continued by calling the `continue_run` method.

For example:

```python
agent.run("Perform sensitive operation")

if agent.is_paused:
    # The agent will pause while human input is provided
    # ... perform other tasks

    # The user can then continue the run
    response = agent.continue_run()
    # or response = await agent.acontinue_run()
```

The `continue_run` method continues with the state of the agent at the time of the pause.  You can also pass the `run_response` of a specific run to the `continue_run` method, or the `run_id`.

## User Confirmation

User confirmation allows you to pause execution and require explicit user approval before proceeding with tool calls. This is useful for:

* Sensitive operations
* API calls that modify data
* Actions with significant consequences

The following example shows how to implement user confirmation.

```python
from agno.tools import tool
from agno.agent import Agent
from agno.models.openai import OpenAIChat

@tool(requires_confirmation=True)
def sensitive_operation(data: str) -> str:
    """Perform a sensitive operation that requires confirmation."""
    # Implementation here
    return "Operation completed"

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[sensitive_operation],
)

