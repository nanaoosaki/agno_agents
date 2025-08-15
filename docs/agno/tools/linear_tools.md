---
title: Linear Tools
category: tools
source_lines: 29148-29201
line_count: 53
---

# Linear Tools
Source: https://docs.agno.com/examples/concepts/tools/others/linear



## Code

```python cookbook/tools/linear_tools.py
from agno.agent import Agent
from agno.tools.linear import LinearTools

agent = Agent(
    tools=[LinearTools()],
    show_tool_calls=True,
    markdown=True,
)

agent.print_response("Show me all active issues")
agent.print_response("Create a new high priority task for the engineering team")
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your Linear API key">
    ```bash
    export LINEAR_API_KEY=xxx
    export OPENAI_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U linear-sdk openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/tools/linear_tools.py
      ```

      ```bash Windows
      python cookbook/tools/linear_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


