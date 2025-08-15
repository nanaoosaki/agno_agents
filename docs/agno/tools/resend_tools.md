---
title: Resend Tools
category: tools
source_lines: 29455-29506
line_count: 51
---

# Resend Tools
Source: https://docs.agno.com/examples/concepts/tools/others/resend



## Code

```python cookbook/tools/resend_tools.py
from agno.agent import Agent
from agno.tools.resend import ResendTools

agent = Agent(
    tools=[ResendTools()],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("Send an email to test@example.com with the subject 'Test Email'")
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export RESEND_API_KEY=xxx
    export OPENAI_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U resend openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/tools/resend_tools.py
      ```

      ```bash Windows
      python cookbook/tools/resend_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


