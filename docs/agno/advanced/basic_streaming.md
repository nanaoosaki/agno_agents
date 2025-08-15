---
title: Basic Streaming
category: advanced
source_lines: 39084-39099
line_count: 15
---

# Basic Streaming
Source: https://docs.agno.com/examples/models/azure/openai/basic_stream



## Code

```python cookbook/models/azure/openai/basic_stream.py
from typing import Iterator  # noqa

from agno.agent import Agent, RunResponse  # noqa
from agno.models.azure import AzureOpenAI

agent = Agent(model=AzureOpenAI(id="gpt-4o"), markdown=True)

