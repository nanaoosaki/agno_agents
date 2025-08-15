---
title: Streaming Basic Agent
category: advanced
source_lines: 42969-42983
line_count: 14
---

# Streaming Basic Agent
Source: https://docs.agno.com/examples/models/ibm/basic_stream



## Code

```python cookbook/models/ibm/watsonx/basic_stream.py
from typing import Iterator
from agno.agent import Agent, RunResponse
from agno.models.ibm import WatsonX

agent = Agent(model=WatsonX(id="ibm/granite-20b-code-instruct"), markdown=True)

