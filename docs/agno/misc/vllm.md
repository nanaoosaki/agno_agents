---
title: vLLM
category: misc
source_lines: 65506-65589
line_count: 83
---

# vLLM
Source: https://docs.agno.com/models/vllm



[vLLM](https://docs.vllm.ai/en/latest/) is a fast and easy-to-use library for LLM inference and serving, designed for high-throughput and memory-efficient LLM serving.

## Prerequisites

Install vLLM and start serving a model:

```bash install vLLM
pip install vllm
```

```bash start vLLM server
vllm serve Qwen/Qwen2.5-7B-Instruct \
    --enable-auto-tool-choice \
    --tool-call-parser hermes \
    --dtype float16 \
    --max-model-len 8192 \
    --gpu-memory-utilization 0.9
```

This spins up the vLLM server with an OpenAI-compatible API.

<Note>
  The default vLLM server URL is `http://localhost:8000/`
</Note>

## Example

Basic Agent

<CodeGroup>
  ```python agent.py
  from agno.agent import Agent
  from agno.models.vllm import vLLM

  agent = Agent(
      model=vLLM(
          id="meta-llama/Llama-3.1-8B-Instruct", 
          base_url="http://localhost:8000/",
      ),
      markdown=True
  )

  agent.print_response("Share a 2 sentence horror story.")
  ```
</CodeGroup>

## Advanced Usage

### With Tools

vLLM models work seamlessly with Agno tools:

```python with_tools.py
from agno.agent import Agent
from agno.models.vllm import vLLM
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=vLLM(id="meta-llama/Llama-3.1-8B-Instruct"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True
)

agent.print_response("What's the latest news about AI?")
```

<Note> View more examples [here](../examples/models/vllm). </Note>

For the full list of supported models, see the [vLLM documentation](https://docs.vllm.ai/en/latest/models/supported_models.html).

## Params

<Snippet file="model-vllm-params.mdx" />

`vLLM` is a subclass of the [Model](/reference/models/model) class and has access to the same params.


