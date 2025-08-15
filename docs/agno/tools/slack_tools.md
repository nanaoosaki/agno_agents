---
title: Slack Tools
category: tools
source_lines: 30683-30739
line_count: 56
---

# Slack Tools
Source: https://docs.agno.com/examples/concepts/tools/social/slack



## Code

```python cookbook/tools/slack_tools.py
from agno.agent import Agent
from agno.tools.slack import SlackTools

agent = Agent(
    tools=[SlackTools()],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("Send a message to #general channel saying 'Hello from Agno!'")
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export OPENAI_API_KEY=xxx
    ```
  </Step>

  <Step title="Set your Slack token">
    ```bash
    export SLACK_BOT_TOKEN=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U slack-sdk openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/tools/slack_tools.py
      ```

      ```bash Windows
      python cookbook/tools/slack_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


