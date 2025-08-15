---
title: Agent with Streaming
category: advanced
source_lines: 48407-48455
line_count: 48
---

# Agent with Streaming
Source: https://docs.agno.com/examples/models/vllm/basic_stream



## Code

```python cookbook/models/vllm/basic_stream.py
from agno.agent import Agent
from agno.models.vllm import vLLM

agent = Agent(
    model=vLLM(id="Qwen/Qwen2.5-7B-Instruct", top_k=20, enable_thinking=False),
    markdown=True,
)
agent.print_response("Share a 2 sentence horror story", stream=True)
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
    vllm serve Qwen/Qwen2.5-7B-Instruct \
        --enable-auto-tool-choice \
        --tool-call-parser hermes \
        --dtype float16 \
        --max-model-len 8192 \
        --gpu-memory-utilization 0.9
    ```
  </Step>

  <Step title="Run Agent">
    ```bash
    python cookbook/models/vllm/basic_stream.py
    ```
  </Step>
</Steps>


