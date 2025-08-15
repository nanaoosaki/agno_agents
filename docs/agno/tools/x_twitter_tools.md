---
title: X (Twitter) Tools
category: tools
source_lines: 30937-30997
line_count: 60
---

# X (Twitter) Tools
Source: https://docs.agno.com/examples/concepts/tools/social/x



## Code

```python cookbook/tools/x_tools.py
from agno.agent import Agent
from agno.tools.x import XTools

agent = Agent(
    tools=[XTools()],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("Make a post saying 'Hello World from Agno!'")
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export OPENAI_API_KEY=xxx
    ```
  </Step>

  <Step title="Set your X credentials">
    ```bash
    export X_CONSUMER_KEY=xxx
    export X_CONSUMER_SECRET=xxx
    export X_ACCESS_TOKEN=xxx
    export X_ACCESS_TOKEN_SECRET=xxx
    export X_BEARER_TOKEN=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U tweepy openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/tools/x_tools.py
      ```

      ```bash Windows
      python cookbook/tools/x_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


