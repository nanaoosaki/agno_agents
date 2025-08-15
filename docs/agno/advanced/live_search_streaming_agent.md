---
title: Live Search Streaming Agent
category: advanced
source_lines: 49375-49427
line_count: 52
---

# Live Search Streaming Agent
Source: https://docs.agno.com/examples/models/xai/live_search_agent_stream



## Code

```python cookbook/models/xai/live_search_agent_stream.py
from agno.agent import Agent
from agno.models.xai import xAI

agent = Agent(
    model=xAI(
        id="grok-3",
        search_parameters={
            "mode": "on",
            "max_search_results": 20,
            "return_citations": True,
        },
    ),
    markdown=True,
)
agent.print_response(
    "Provide me a digest of world news in the last 24 hours.", stream=True
)
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
    pip install -U openai agno
    ```
  </Step>

  <Step title="Run Agent">
    ```bash
    python cookbook/models/xai/live_search_agent_stream.py
    ```
  </Step>
</Steps>


