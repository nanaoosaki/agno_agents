---
title: Zendesk Tools
category: tools
source_lines: 29700-29758
line_count: 58
---

# Zendesk Tools
Source: https://docs.agno.com/examples/concepts/tools/others/zendesk



## Code

```python cookbook/tools/zendesk_tools.py
from agno.agent import Agent
from agno.tools.zendesk import ZendeskTools

agent = Agent(
    tools=[ZendeskTools()],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("Show me all open tickets")
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export OPENAI_API_KEY=xxx
    ```
  </Step>

  <Step title="Set your Zendesk credentials">
    ```bash
    export ZENDESK_EMAIL=xxx
    export ZENDESK_TOKEN=xxx
    export ZENDESK_SUBDOMAIN=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U zenpy openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/tools/zendesk_tools.py
      ```

      ```bash Windows
      python cookbook/tools/zendesk_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


