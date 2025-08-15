---
title: Email Tools
category: tools
source_lines: 30616-30683
line_count: 67
---

# Email Tools
Source: https://docs.agno.com/examples/concepts/tools/social/email



## Code

```python cookbook/tools/email_tools.py
from agno.agent import Agent
from agno.tools.email import EmailTools

receiver_email = "<receiver_email>"
sender_email = "<sender_email>"
sender_name = "<sender_name>"
sender_passkey = "<sender_passkey>"

agent = Agent(
    tools=[
        EmailTools(
            receiver_email=receiver_email,
            sender_email=sender_email,
            sender_name=sender_name,
            sender_passkey=sender_passkey,
        )
    ]
)
agent.print_response("Send an email to <receiver_email>.")
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export OPENAI_API_KEY=xxx
    ```
  </Step>

  <Step title="Set your email credentials">
    ```bash
    export SENDER_EMAIL=xxx
    export SENDER_PASSKEY=xxx
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
      python cookbook/tools/email_tools.py
      ```

      ```bash Windows
      python cookbook/tools/email_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


