---
title: Luma Labs Tools
category: tools
source_lines: 29201-29252
line_count: 51
---

# Luma Labs Tools
Source: https://docs.agno.com/examples/concepts/tools/others/lumalabs



## Code

```python cookbook/tools/lumalabs_tools.py
from agno.agent import Agent
from agno.tools.lumalabs import LumaLabsTools

agent = Agent(
    tools=[LumaLabsTools()],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("Generate a 3D model of a futuristic city")
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export LUMALABS_API_KEY=xxx
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
      python cookbook/tools/lumalabs_tools.py
      ```

      ```bash Windows
      python cookbook/tools/lumalabs_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


