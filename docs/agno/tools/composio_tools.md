---
title: Composio Tools
category: tools
source_lines: 28243-28295
line_count: 52
---

# Composio Tools
Source: https://docs.agno.com/examples/concepts/tools/others/composio



## Code

```python cookbook/tools/composio_tools.py
from agno.agent import Agent
from composio_agno import Action, ComposioToolSet

toolset = ComposioToolSet()
composio_tools = toolset.get_tools(
    actions=[Action.GITHUB_STAR_A_REPOSITORY_FOR_THE_AUTHENTICATED_USER]
)

agent = Agent(tools=composio_tools, show_tool_calls=True)
agent.print_response("Can you star agno-agi/agno repo?")
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export COMPOSIO_API_KEY=xxx
    export OPENAI_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U composio-agno openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/tools/composio_tools.py
      ```

      ```bash Windows
      python cookbook/tools/composio_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


