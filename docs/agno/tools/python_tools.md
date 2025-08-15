---
title: Python Tools
category: tools
source_lines: 26766-26816
line_count: 50
---

# Python Tools
Source: https://docs.agno.com/examples/concepts/tools/local/python



## Code

```python cookbook/tools/python_tools.py
from agno.agent import Agent
from agno.tools.python import PythonTools

agent = Agent(
    tools=[PythonTools()],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("Calculate the factorial of 5 using Python")
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
      python cookbook/tools/python_tools.py
      ```

      ```bash Windows
      python cookbook/tools/python_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


