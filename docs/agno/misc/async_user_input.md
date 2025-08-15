---
title: Async User Input
category: misc
source_lines: 31868-31974
line_count: 106
---

# Async User Input
Source: https://docs.agno.com/examples/concepts/user-control-flows/05-user-input-required-async

This example demonstrates how to implement asynchronous user input collection, allowing for non-blocking execution while gathering user information.

## Code

```python cookbook/agent_concepts/user_control_flows/user_input_required_async.py
import asyncio
from typing import List

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools import tool
from agno.tools.function import UserInputField
from agno.utils import pprint

@tool(requires_user_input=True, user_input_fields=["to_address"])
async def send_email(subject: str, body: str, to_address: str) -> str:
    """
    Send an email.

    Args:
        subject (str): The subject of the email.
        body (str): The body of the email.
        to_address (str): The address to send the email to.
    """
    return f"Sent email to {to_address} with subject {subject} and body {body}"

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[send_email],
    markdown=True,
)

asyncio.run(
    agent.arun("Send an email with the subject 'Hello' and the body 'Hello, world!'")
)
if agent.is_paused:
    for tool in agent.run_response.tools_requiring_user_input:
        input_schema: List[UserInputField] = tool.user_input_schema

        for field in input_schema:
            # Display field information to the user
            print(f"\nField: {field.name}")
            print(f"Description: {field.description}")
            print(f"Type: {field.field_type}")

            # Get user input
            if field.value is None:
                user_value = input(f"Please enter a value for {field.name}: ")
                # Update the field value
                field.value = user_value
            else:
                print(f"Value: {field.value}")


    run_response = asyncio.run(agent.acontinue_run())
    pprint.pprint_run_response(run_response)
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export OPENAI_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U agno openai
    ```
  </Step>

  <Step title="Run Example">
    <CodeGroup>
      ```bash Mac
      python cookbook/agent_concepts/user_control_flows/user_input_required_async.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/user_control_flows/user_input_required_async.py
      ```
    </CodeGroup>
  </Step>
</Steps>

## Key Features

* Uses `agent.arun()` for asynchronous agent execution
* Implements `agent.acontinue_run()` for async continuation
* Maintains the same user input flow as synchronous version
* Demonstrates how to handle async execution with user input collection

## Use Cases

* Non-blocking user input collection
* High-performance applications requiring async execution
* Web applications with form-like interactions
* Long-running operations with user input


