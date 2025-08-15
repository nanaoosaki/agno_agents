---
title: Sleep Tools
category: tools
source_lines: 26866-26916
line_count: 50
---

# Sleep Tools
Source: https://docs.agno.com/examples/concepts/tools/local/sleep



## Code

```python cookbook/tools/sleep_tools.py
from agno.agent import Agent
from agno.tools.sleep import SleepTools

agent = Agent(
    tools=[SleepTools()],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("Wait for 5 seconds before continuing")
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
      python cookbook/tools/sleep_tools.py
      ```

      ```bash Windows
      python cookbook/tools/sleep_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


