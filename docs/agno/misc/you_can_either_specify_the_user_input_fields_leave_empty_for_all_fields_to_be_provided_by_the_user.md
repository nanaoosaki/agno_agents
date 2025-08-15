---
title: You can either specify the user_input_fields leave empty for all fields to be provided by the user
category: misc
source_lines: 31784-31868
line_count: 84
---

# You can either specify the user_input_fields leave empty for all fields to be provided by the user
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

agent.run("Send an email with the subject 'Hello' and the body 'Hello, world!'")
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

    run_response = agent.continue_run()
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
      python cookbook/agent_concepts/user_control_flows/user_input_required.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/user_control_flows/user_input_required.py
      ```
    </CodeGroup>
  </Step>
</Steps>

## Key Features

* Uses `@tool(requires_user_input=True)` to mark tools that need user input
* Can specify which fields require user input using `user_input_fields`
* Implements a dynamic form-like interface for collecting user input
* Handles both user-provided and agent-provided values

## Use Cases

* Collecting required parameters for operations


