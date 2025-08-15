---
title: Async Agent with Tools
category: tools
source_lines: 48791-48841
line_count: 50
---

# Async Agent with Tools
Source: https://docs.agno.com/examples/models/xai/async_tool_use



## Code

```python cookbook/models/xai/async_tool_use.py
"""Run `pip install duckduckgo-search` to install dependencies."""

import asyncio

from agno.agent import Agent
from agno.models.xai import xAI
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=xAI(id="grok-3"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)
asyncio.run(agent.aprint_response("Whats happening in France?", stream=True))
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export XAI_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U openai duckduckgo-search agno
    ```
  </Step>

  <Step title="Run Agent">
    ```bash
    python cookbook/models/xai/async_tool_use.py
    ```
  </Step>
</Steps>


