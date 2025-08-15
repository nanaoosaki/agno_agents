---
title: Twilio Tools
category: tools
source_lines: 30739-30797
line_count: 58
---

# Twilio Tools
Source: https://docs.agno.com/examples/concepts/tools/social/twilio



## Code

```python cookbook/tools/twilio_tools.py
from agno.agent import Agent
from agno.tools.twilio import TwilioTools

agent = Agent(
    tools=[TwilioTools()],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("Send an SMS to +1234567890 saying 'Hello from Agno!'")
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export OPENAI_API_KEY=xxx
    ```
  </Step>

  <Step title="Set your Twilio credentials">
    ```bash
    export TWILIO_ACCOUNT_SID=xxx
    export TWILIO_AUTH_TOKEN=xxx
    export TWILIO_FROM_NUMBER=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U twilio openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/tools/twilio_tools.py
      ```

      ```bash Windows
      python cookbook/tools/twilio_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


