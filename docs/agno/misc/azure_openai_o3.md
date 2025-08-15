---
title: Azure OpenAI o3
category: misc
source_lines: 21994-22057
line_count: 63
---

# Azure OpenAI o3
Source: https://docs.agno.com/examples/concepts/reasoning/models/azure-openai/o3-tools



## Code

```python ccookbook/reasoning/models/azure_openai/o3_mini_with_tools.py
from agno.agent import Agent
from agno.models.azure.openai_chat import AzureOpenAI
from agno.tools.yfinance import YFinanceTools

agent = Agent(
    model=AzureOpenAI(id="o3"),
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
    export AZURE_OPENAI_API_KEY=xxx
    export AZURE_OPENAI_ENDPOINT=xxx
    export AZURE_DEPLOYMENT=xxx
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
      python ccookbook/reasoning/models/azure_openai/o3_mini_with_tools.py
      ```

      ```bash Windows
      python ccookbook/reasoning/models/azure_openai/o3_mini_with_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


