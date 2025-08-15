---
title: Groq DeepSeek R1
category: misc
source_lines: 22173-22225
line_count: 52
---

# Groq DeepSeek R1
Source: https://docs.agno.com/examples/concepts/reasoning/models/groq/groq-basic



## Code

```python cookbook/reasoning/models/groq/9_11_or_9_9.py
from agno.agent import Agent
from agno.models.groq import Groq

agent = Agent(
    model=Groq(
        id="deepseek-r1-distill-llama-70b", temperature=0.6, max_tokens=1024, top_p=0.95
    ),
    markdown=True,
)
agent.print_response("9.11 and 9.9 -- which is bigger?", stream=True)

```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export GROQ_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U groq agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/reasoning/models/groq/9_11_or_9_9.py
      ```

      ```bash Windows
      python cookbook/reasoning/models/groq/9_11_or_9_9.py
      ```
    </CodeGroup>
  </Step>
</Steps>


