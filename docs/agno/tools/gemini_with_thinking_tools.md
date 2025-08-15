---
title: Gemini with Thinking Tools
category: tools
source_lines: 22902-22970
line_count: 68
---

# Gemini with Thinking Tools
Source: https://docs.agno.com/examples/concepts/reasoning/tools/gemini-thinking-tools



## Code

```python cookbook/reasoning/tools/gemini_finance_agent.py

from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.thinking import ThinkingTools
from agno.tools.yfinance import YFinanceTools

thinking_agent = Agent(
    model=Gemini(id="gemini-2.0-flash"),
    tools=[
        ThinkingTools(add_instructions=True),
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            company_info=True,
            company_news=True,
        ),
    ],
    instructions="Use tables where possible",
    show_tool_calls=True,
    markdown=True,
    stream_intermediate_steps=True,
)
thinking_agent.print_response(
    "Write a report comparing NVDA to TSLA in detail", stream=True, show_reasoning=True
)


```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export GOOGLE_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U google-genai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/reasoning/tools/gemini_finance_agent.py
      ```

      ```bash Windows
      python cookbook/reasoning/tools/gemini_finance_agent.py
      ```
    </CodeGroup>
  </Step>
</Steps>


