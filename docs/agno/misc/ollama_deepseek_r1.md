---
title: Ollama DeepSeek R1
category: misc
source_lines: 22278-22334
line_count: 56
---

# Ollama DeepSeek R1
Source: https://docs.agno.com/examples/concepts/reasoning/models/ollama/ollama-basic



## Code

```python cookbook/reasoning/models/ollama/reasoning_model_deepseek.py
from agno.agent import Agent
from agno.models.ollama.chat import Ollama

agent = Agent(
    model=Ollama(id="llama3.2:latest"),
    reasoning_model=Ollama(id="deepseek-r1:14b", max_tokens=4096),
)
agent.print_response(
    "Solve the trolley problem. Evaluate multiple ethical frameworks. "
    "Include an ASCII diagram of your solution.",
    stream=True,
)

```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Install Ollama">
    Follow the [installation guide](https://github.com/ollama/ollama?tab=readme-ov-file#macos) and run:

    ```bash
    ollama pull llama3.2:latest
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U ollama agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/reasoning/models/ollama/reasoning_model_deepseek.py
      ```

      ```bash Windows
      python cookbook/reasoning/models/ollama/reasoning_model_deepseek.py
      ```
    </CodeGroup>
  </Step>
</Steps>


