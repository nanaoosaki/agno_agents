---
title: Cerebras
category: misc
source_lines: 63776-63811
line_count: 35
---

# Cerebras
Source: https://docs.agno.com/models/cerebras

Learn how to use Cerebras models in Agno.

[Cerebras Inference](https://inference-docs.cerebras.ai/introduction) provides high-speed, low-latency AI model inference powered by Cerebras Wafer-Scale Engines and CS-3 systems. Agno integrates directly with the Cerebras Python SDK, allowing you to use state-of-the-art Llama models with a simple interface.

## Prerequisites

To use Cerebras with Agno, you need to:

1. **Install the required packages:**
   ```shell
   pip install cerebras-cloud-sdk
   ```

2. **Set your API key:**
   The Cerebras SDK expects your API key to be available as an environment variable:
   ```shell
   export CEREBRAS_API_KEY=your_api_key_here
   ```

## Basic Usage

Here's how to use a Cerebras model with Agno:

```python
from agno.agent import Agent
from agno.models.cerebras import Cerebras

agent = Agent(
    model=Cerebras(id="llama-4-scout-17b-16e-instruct"),
    markdown=True,
)

