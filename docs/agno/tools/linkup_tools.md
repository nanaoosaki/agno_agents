---
title: Linkup Tools
category: tools
source_lines: 30164-30205
line_count: 41
---

# Linkup Tools
Source: https://docs.agno.com/examples/concepts/tools/search/linkup



## Code

```python cookbook/tools/linkup_tools.py
from agno.agent import Agent
from agno.tools.linkup import LinkupTools

agent = Agent(tools=[LinkupTools()], show_tool_calls=True)
agent.print_response("What's the latest news in French politics?", markdown=True)
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export LINKUP_API_KEY=xxx
    export OPENAI_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U linkup-sdk openai agno
    ```
  </Step>

  <Step title="Run Agent">
    ```bash
    python cookbook/tools/linkup_tools.py
    ```
  </Step>
</Steps>


