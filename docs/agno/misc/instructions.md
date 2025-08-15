---
title: Instructions
category: misc
source_lines: 20634-20681
line_count: 47
---

# Instructions
Source: https://docs.agno.com/examples/concepts/others/instructions



This example shows how to provide specific instructions to an agent.

## Code

```python cookbook/agent_concepts/other/instructions.py
from agno.agent import Agent

agent = Agent(instructions="Share a 2 sentence story about")
agent.print_response("Love in the year 12000.")
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
      python cookbook/agent_concepts/other/instructions.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/other/instructions.py
      ```
    </CodeGroup>
  </Step>
</Steps>


