---
title: Location Instructions
category: misc
source_lines: 20805-20859
line_count: 54
---

# Location Instructions
Source: https://docs.agno.com/examples/concepts/others/location_instructions

Add the current location to the instructions of an agent.

This example shows how to add the current location to the instructions of an agent.

## Code

```python cookbook/agent_concepts/other/location_instructions.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    add_location_to_instructions=True,
)
agent.print_response(
    "What is current news about my city?"
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
      python cookbook/agent_concepts/other/location_instructions.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/other/location_instructions.py
      ```
    </CodeGroup>
  </Step>
</Steps>


