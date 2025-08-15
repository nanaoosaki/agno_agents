---
title: Instructions via Function
category: misc
source_lines: 20681-20743
line_count: 62
---

# Instructions via Function
Source: https://docs.agno.com/examples/concepts/others/instructions_via_function



This example shows how to pass a function as instructions to an agent.

## Code

```python cookbook/agent_concepts/other/instructions_via_function.py
from typing import List
from agno.agent import Agent


def get_instructions(agent: Agent) -> List[str]:
    return [
        f"Your name is {agent.name}!",
        "Talk in haiku's!",
        "Use poetry to answer questions.",
    ]


agent = Agent(
    name="AgentX",
    instructions=get_instructions,
    markdown=True,
    show_tool_calls=True,
)
agent.print_response("Who are you?", stream=True)
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
      python cookbook/agent_concepts/other/instructions_via_function.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/other/instructions_via_function.py
      ```
    </CodeGroup>
  </Step>
</Steps>


