---
title: Agent with Tools
category: tools
source_lines: 49561-49607
line_count: 46
---

# Agent with Tools
Source: https://docs.agno.com/examples/models/xai/tool_use



## Code

```python cookbook/models/xai/tool_use.py
from agno.agent import Agent
from agno.models.xai import xAI
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=xAI(id="grok-beta"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("Whats happening in France?", stream=True)
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
    python cookbook/models/xai/tool_use.py
    ```
  </Step>
</Steps>


