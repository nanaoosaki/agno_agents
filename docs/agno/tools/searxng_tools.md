---
title: SearxNG Tools
category: tools
source_lines: 30255-30305
line_count: 50
---

# SearxNG Tools
Source: https://docs.agno.com/examples/concepts/tools/search/searxng



## Code

```python cookbook/tools/searxng_tools.py
from agno.agent import Agent
from agno.tools.searxng import SearxNGTools

agent = Agent(
    tools=[SearxNGTools(instance_url="https://your-searxng-instance.com")],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("Search for recent news about artificial intelligence")
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
    pip install -U searxng-client openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/tools/searxng_tools.py
      ```

      ```bash Windows
      python cookbook/tools/searxng_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


