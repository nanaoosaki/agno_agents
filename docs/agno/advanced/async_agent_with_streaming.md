---
title: Async Agent with Streaming
category: advanced
source_lines: 48305-48352
line_count: 47
---

# Async Agent with Streaming
Source: https://docs.agno.com/examples/models/vllm/async_basic_stream



## Code

```python cookbook/models/vllm/async_basic_stream.py
import asyncio

from agno.agent import Agent
from agno.models.vllm import vLLM

agent = Agent(model=vLLM(id="Qwen/Qwen2.5-7B-Instruct"), markdown=True)
asyncio.run(agent.aprint_response("Share a 2 sentence horror story", stream=True))
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
    python cookbook/models/vllm/async_basic_stream.py
    ```
  </Step>
</Steps>


