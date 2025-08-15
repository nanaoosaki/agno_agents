---
title: State in Instructions
category: misc
source_lines: 23297-23355
line_count: 58
---

# State in Instructions
Source: https://docs.agno.com/examples/concepts/state/02-state-in-prompt



This example demonstrates how to inject `session_state` variables directly into the agent’s instructions using `add_state_in_messages`.

## Code

```python cookbook/agent_concepts/state/state_in_prompt.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    # Initialize the session state with a variable
    session_state={"user_name": "John"},
    # You can use variables from the session state in the instructions
    instructions="Users name is {user_name}",
    show_tool_calls=True,
    add_state_in_messages=True,
    markdown=True,
)

agent.print_response("What is my name?", stream=True)
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
    pip install -U openai agno
    ```
  </Step>

  <Step title="Run Example">
    <CodeGroup>
      ```bash Mac
      python cookbook/agent_concepts/state/state_in_prompt.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/state/state_in_prompt.py
      ```
    </CodeGroup>
  </Step>
</Steps>


