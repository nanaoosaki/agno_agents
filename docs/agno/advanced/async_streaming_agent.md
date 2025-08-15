---
title: Async Streaming Agent
category: advanced
source_lines: 48935-48951
line_count: 16
---

# Async Streaming Agent
Source: https://docs.agno.com/examples/models/xai/basic_async_stream



## Code

```python cookbook/models/xai/basic_async_stream.py
import asyncio
from typing import Iterator

from agno.agent import Agent, RunResponseEvent
from agno.models.xai import xAI

agent = Agent(model=xAI(id="grok-3"), markdown=True)

