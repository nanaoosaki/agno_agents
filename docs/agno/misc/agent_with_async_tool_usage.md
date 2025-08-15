---
title: Agent with Async Tool Usage
category: misc
source_lines: 42858-42914
line_count: 56
---

# Agent with Async Tool Usage
Source: https://docs.agno.com/examples/models/ibm/async_tool_use



## Code

```python cookbook/models/ibm/watsonx/async_tool_use.py
import asyncio

from agno.agent import Agent
from agno.models.ibm import WatsonX
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=WatsonX(id="meta-llama/llama-3-3-70b-instruct"),
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
    export IBM_WATSONX_API_KEY=xxx
    export IBM_WATSONX_PROJECT_ID=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U ibm-watsonx-ai duckduckgo-search agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/models/ibm/watsonx/async_tool_use.py
      ```

      ```bash Windows
      python cookbook\models\ibm\watsonx\async_tool_use.py
      ```
    </CodeGroup>
  </Step>
</Steps>


