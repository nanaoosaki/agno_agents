---
title: Basic Agent
category: misc
source_lines: 48841-48854
line_count: 13
---

# Basic Agent
Source: https://docs.agno.com/examples/models/xai/basic



## Code

```python cookbook/models/xai/basic.py
from agno.agent import Agent, RunResponse
from agno.models.xai import xAI

agent = Agent(model=xAI(id="grok-3"), markdown=True)

