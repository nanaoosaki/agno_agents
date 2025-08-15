---
title: Agent with Reasoning Effort
category: misc
source_lines: 46832-46885
line_count: 53
---

# Agent with Reasoning Effort
Source: https://docs.agno.com/examples/models/openai/chat/reasoning_effort



## Code

```python cookbook/reasoning/models/openai/reasoning_effort.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.yfinance import YFinanceTools

agent = Agent(
    model=OpenAIChat(id="o3-mini", reasoning_effort="high"),
    tools=[YFinanceTools(enable_all=True)],
    show_tool_calls=True,
    markdown=True,
)

agent.print_response("Write a report on the NVDA, is it a good buy?", stream=True)
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
    pip install -U openai yfinance agno
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


