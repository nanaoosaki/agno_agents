---
title: OpenBB Tools
category: tools
source_lines: 29353-29404
line_count: 51
---

# OpenBB Tools
Source: https://docs.agno.com/examples/concepts/tools/others/openbb



## Code

```python cookbook/tools/openbb_tools.py
from agno.agent import Agent
from agno.tools.openbb import OpenBBTools

agent = Agent(
    tools=[OpenBBTools()],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("Get the latest stock price for AAPL")
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export OPENBB_PAT=xxx
    export OPENAI_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U openbb openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/tools/openbb_tools.py
      ```

      ```bash Windows
      python cookbook/tools/openbb_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


