---
title: YFinance Tools
category: tools
source_lines: 29599-29649
line_count: 50
---

# YFinance Tools
Source: https://docs.agno.com/examples/concepts/tools/others/yfinance



## Code

```python cookbook/tools/yfinance_tools.py
from agno.agent import Agent
from agno.tools.yfinance import YFinanceTools

agent = Agent(
    tools=[YFinanceTools()],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("Get the current stock price and recent history for AAPL")
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
    pip install -U yfinance openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/tools/yfinance_tools.py
      ```

      ```bash Windows
      python cookbook/tools/yfinance_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


