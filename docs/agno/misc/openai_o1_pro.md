---
title: OpenAI o1 pro
category: misc
source_lines: 22334-22385
line_count: 51
---

# OpenAI o1 pro
Source: https://docs.agno.com/examples/concepts/reasoning/models/openai/o1-pro



## Code

```python cookbook/reasoning/models/openai/o1_pro.py
from agno.agent import Agent
from agno.models.openai import OpenAIResponses

agent = Agent(model=OpenAIResponses(id="o1-pro"))
agent.print_response(
    "Solve the trolley problem. Evaluate multiple ethical frameworks. "
    "Include an ASCII diagram of your solution.",
    stream=True,
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
        python cookbook/reasoning/models/openai/o1_pro.py
      ```

      ```bash Windows
        python cookbook/reasoning/models/openai/o1_pro.py
      ```
    </CodeGroup>
  </Step>
</Steps>


