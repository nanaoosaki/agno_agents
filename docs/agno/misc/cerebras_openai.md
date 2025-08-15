---
title: Cerebras OpenAI
category: misc
source_lines: 63853-63884
line_count: 31
---

# Cerebras OpenAI
Source: https://docs.agno.com/models/cerebras_openai

Learn how to use Cerebras OpenAI with Agno.

## OpenAI-Compatible Integration

Cerebras can also be used via an OpenAI-compatible interface, making it easy to integrate with tools and libraries that expect the OpenAI API.

### Using the OpenAI-Compatible Class

The `CerebrasOpenAI` class provides an OpenAI-style interface for Cerebras models:

First, install openai:

```shell
pip install openai
```

```python
from agno.agent import Agent
from agno.models.cerebras import CerebrasOpenAI

agent = Agent(
    model=CerebrasOpenAI(
        id="llama-4-scout-17b-16e-instruct",  # Model ID to use
        # base_url="https://api.cerebras.ai", # Optional: default endpoint for Cerebras
    ),
    markdown=True,
)

