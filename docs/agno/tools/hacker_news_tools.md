---
title: Hacker News Tools
category: tools
source_lines: 30114-30164
line_count: 50
---

# Hacker News Tools
Source: https://docs.agno.com/examples/concepts/tools/search/hackernews



## Code

```python cookbook/tools/hackernews_tools.py
from agno.agent import Agent
from agno.tools.hackernews import HackerNewsTools

agent = Agent(
    tools=[HackerNewsTools()],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("What are the top stories on Hacker News right now?")
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
    pip install -U requests openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/tools/hackernews_tools.py
      ```

      ```bash Windows
      python cookbook/tools/hackernews_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


