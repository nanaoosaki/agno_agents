---
title: Live Search Agent
category: misc
source_lines: 49325-49375
line_count: 50
---

# Live Search Agent
Source: https://docs.agno.com/examples/models/xai/live_search_agent



## Code

```python cookbook/models/xai/live_search_agent.py
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
agent.print_response("Provide me a digest of world news in the last 24 hours.")
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
    python cookbook/models/xai/live_search_agent.py
    ```
  </Step>
</Steps>


