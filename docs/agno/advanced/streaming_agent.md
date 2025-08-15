---
title: Streaming Agent
category: advanced
source_lines: 48985-48999
line_count: 14
---

# Streaming Agent
Source: https://docs.agno.com/examples/models/xai/basic_stream



## Code

```python cookbook/models/xai/basic_stream.py
from typing import Iterator
from agno.agent import Agent, RunResponse
from agno.models.xai import xAI

agent = Agent(model=xAI(id="grok-3"), markdown=True)

