---
title: Intermediate Steps
category: misc
source_lines: 20743-20805
line_count: 62
---

# Intermediate Steps
Source: https://docs.agno.com/examples/concepts/others/intermediate_steps



This example shows how to use intermediate steps in an agent.

## Code

```python cookbook/agent_concepts/other/intermediate_steps.py
from typing import Iterator
from agno.agent import Agent, RunResponse
from agno.models.openai import OpenAIChat
from agno.tools.yfinance import YFinanceTools
from rich.pretty import pprint

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True)],
    markdown=True,
    show_tool_calls=True,
)

run_stream: Iterator[RunResponse] = agent.run(
    "What is the stock price of NVDA", stream=True, stream_intermediate_steps=True
)
for chunk in run_stream:
    pprint(chunk.to_dict())
    print("---" * 20)
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
    pip install -U openai agno yfinance rich
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/agent_concepts/other/intermediate_steps.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/other/intermediate_steps.py
      ```
    </CodeGroup>
  </Step>
</Steps>


