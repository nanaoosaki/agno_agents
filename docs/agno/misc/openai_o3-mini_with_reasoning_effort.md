---
title: OpenAI o3-mini with reasoning effort
category: misc
source_lines: 22446-22508
line_count: 62
---

# OpenAI o3-mini with reasoning effort
Source: https://docs.agno.com/examples/concepts/reasoning/models/openai/reasoning-effort



## Code

```python cookbook/reasoning/models/openai/reasoning_effort.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.yfinance import YFinanceTools

agent = Agent(
    model=OpenAIChat(id="o3-mini", reasoning_effort="high"),
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
    export OPENAI_API_KEY=xxx
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
        python cookbook/reasoning/models/openai/reasoning_effort.py
      ```

      ```bash Windows
        python cookbook/reasoning/models/openai/reasoning_effort.py
      ```
    </CodeGroup>
  </Step>
</Steps>


