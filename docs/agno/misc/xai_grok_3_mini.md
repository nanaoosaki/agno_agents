---
title: xAI Grok 3 Mini
category: misc
source_lines: 22508-22569
line_count: 61
---

# xAI Grok 3 Mini
Source: https://docs.agno.com/examples/concepts/reasoning/models/xai/reasoning-effort



## Code

```python cookbook/reasoning/models/xai/reasoning_effort.py
from agno.agent import Agent
from agno.models.xai import xAI
from agno.tools.yfinance import YFinanceTools

agent = Agent(
    model=xAI(id="grok-3-mini-fast", reasoning_effort="high"),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            company_info=True,
            company_news=True,
        )
    ],
    instructions="Use tables to display data.",
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("Write a report comparing NVDA to TSLA", stream=True)

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
    <CodeGroup>
      ```bash Mac
      python cookbook/reasoning/models/xai/reasoning_effort.py
      ```

      ```bash Windows
      python cookbook/reasoning/models/xai/reasoning_effort.py
      ```
    </CodeGroup>
  </Step>
</Steps>


