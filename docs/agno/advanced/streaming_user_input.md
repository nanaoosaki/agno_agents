---
title: Streaming User Input
category: advanced
source_lines: 31974-32078
line_count: 104
---

# Streaming User Input
Source: https://docs.agno.com/examples/concepts/user-control-flows/06-user-input-required-stream

This example demonstrates how to implement streaming user input collection, allowing for real-time interaction and response streaming while gathering user information.

## Code

```python cookbook/agent_concepts/user_control_flows/user_input_required_stream.py
from typing import List

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools import tool
from agno.tools.function import UserInputField
from agno.utils import pprint

@tool(requires_user_input=True, user_input_fields=["to_address"])
def send_email(subject: str, body: str, to_address: str) -> str:
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

for run_response in agent.run(
    "Send an email with the subject 'Hello' and the body 'Hello, world!'", stream=True
):
    if run_response.is_paused:
        for tool in run_response.tools_requiring_user_input:
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

        run_response = agent.continue_run(stream=True)
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
      python cookbook/agent_concepts/user_control_flows/user_input_required_stream.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/user_control_flows/user_input_required_stream.py
      ```
    </CodeGroup>
  </Step>
</Steps>

## Key Features

* Uses `agent.run(stream=True)` for streaming responses
* Implements streaming continuation with `agent.continue_run(stream=True)`
* Maintains real-time interaction with user input collection
* Demonstrates how to handle streaming responses with user input

## Use Cases

* Real-time user interaction
* Streaming applications requiring user input
* Interactive form-like interfaces
* Progressive response generation with user input


