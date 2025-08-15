---
title: Datetime Instructions
category: misc
source_lines: 20276-20330
line_count: 54
---

# Datetime Instructions
Source: https://docs.agno.com/examples/concepts/others/datetime_instructions



This example shows how to add the current date and time to the instructions of an agent.

## Code

```python cookbook/agent_concepts/other/datetime_instructions.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    add_datetime_to_instructions=True,
    timezone_identifier="Etc/UTC",
)
agent.print_response(
    "What is the current date and time? What is the current time in NYC?"
)
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

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/agent_concepts/other/datetime_instructions.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/other/datetime_instructions.py
      ```
    </CodeGroup>
  </Step>
</Steps>


