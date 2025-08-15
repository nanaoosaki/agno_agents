---
title: Async Agent
category: misc
source_lines: 48258-48305
line_count: 47
---

# Async Agent
Source: https://docs.agno.com/examples/models/vllm/async_basic



## Code

```python cookbook/models/vllm/async_basic.py
import asyncio

from agno.agent import Agent
from agno.models.vllm import vLLM

agent = Agent(model=vLLM(id="Qwen/Qwen2.5-7B-Instruct"), markdown=True)
asyncio.run(agent.aprint_response("Share a 2 sentence horror story"))
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Install libraries">
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
    python cookbook/models/vllm/async_basic.py
    ```
  </Step>
</Steps>


