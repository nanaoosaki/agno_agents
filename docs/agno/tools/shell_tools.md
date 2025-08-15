---
title: Shell Tools
category: tools
source_lines: 26816-26866
line_count: 50
---

# Shell Tools
Source: https://docs.agno.com/examples/concepts/tools/local/shell



## Code

```python cookbook/tools/shell_tools.py
from agno.agent import Agent
from agno.tools.shell import ShellTools

agent = Agent(
    tools=[ShellTools()],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("List all files in the current directory")
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
    pip install -U openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/tools/shell_tools.py
      ```

      ```bash Windows
      python cookbook/tools/shell_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


