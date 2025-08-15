---
title: Code Generation
category: misc
source_lines: 48455-48505
line_count: 50
---

# Code Generation
Source: https://docs.agno.com/examples/models/vllm/code_generation



## Code

```python cookbook/models/vllm/code_generation.py
from agno.agent import Agent
from agno.models.vllm import vLLM

agent = Agent(
    model=vLLM(id="deepseek-ai/deepseek-coder-6.7b-instruct"),
    description="You are an expert Python developer.",
    markdown=True,
)

agent.print_response(
    """Write a Python function that returns the nth Fibonacci number 
    using dynamic programming."""
)
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Install Libraries">
    ```bash
    pip install -U agno openai vllm
    ```
  </Step>

  <Step title="Start vLLM server">
    ```bash
    vllm serve deepseek-ai/deepseek-coder-6.7b-instruct \
        --dtype float32 \
        --tool-call-parser pythonic
    ```
  </Step>

  <Step title="Run Agent">
    ```bash
    python cookbook/models/vllm/code_generation.py
    ```
  </Step>
</Steps>


