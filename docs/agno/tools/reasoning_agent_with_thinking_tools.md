---
title: Reasoning Agent with Thinking Tools
category: tools
source_lines: 23157-23227
line_count: 70
---

# Reasoning Agent with Thinking Tools
Source: https://docs.agno.com/examples/concepts/reasoning/tools/thinking-tools



## Code

```python cookbook/reasoning/tools/claude_thinking_tools.py
from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.tools.thinking import ThinkingTools
from agno.tools.yfinance import YFinanceTools

reasoning_agent = Agent(
    model=Claude(id="claude-3-7-sonnet-latest"),
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
    markdown=True,
)

if __name__ == "__main__":
    reasoning_agent.print_response(
        "Write a report on NVDA. Only the report, no other text.",
        stream=True,
        show_full_reasoning=True,
        stream_intermediate_steps=True,
    )


```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export ANTHROPIC_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U anthropic agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/reasoning/tools/claude_thinking_tools.py
      ```

      ```bash Windows
      python cookbook/reasoning/tools/claude_thinking_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


