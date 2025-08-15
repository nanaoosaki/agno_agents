---
title: We use a while loop to continue the running until the agent is satisfied with the user input
category: misc
source_lines: 32141-32210
line_count: 69
---

# We use a while loop to continue the running until the agent is satisfied with the user input
while run_response.is_paused:
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
            else:
                print(f"Value: {field.value}")
                user_value = field.value

            # Update the field value
            field.value = user_value

    run_response = agent.continue_run(run_response=run_response)
    if not run_response.is_paused:
        pprint.pprint_run_response(run_response)
        break
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
      python cookbook/agent_concepts/user_control_flows/agentic_user_input.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/user_control_flows/agentic_user_input.py
      ```
    </CodeGroup>
  </Step>
</Steps>

## Key Features

* Uses `UserControlFlowTools` for dynamic user input collection
* Implements a toolkit with multiple tools that may require user input
* Handles multiple rounds of user input collection
* Demonstrates how to continue agent execution after each input round

## Use Cases

* Dynamic form-like interactions


