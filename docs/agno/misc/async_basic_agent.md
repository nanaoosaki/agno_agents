---
title: Async Basic Agent
category: misc
source_lines: 48887-48902
line_count: 15
---

# Async Basic Agent
Source: https://docs.agno.com/examples/models/xai/basic_async



## Code

```python cookbook/models/xai/basic_async.py
import asyncio

from agno.agent import Agent, RunResponse
from agno.models.xai import xAI

agent = Agent(model=xAI(id="grok-3"), markdown=True)

