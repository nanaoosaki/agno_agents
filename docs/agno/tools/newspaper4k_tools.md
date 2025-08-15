---
title: Newspaper4k Tools
category: tools
source_lines: 31210-31260
line_count: 50
---

# Newspaper4k Tools
Source: https://docs.agno.com/examples/concepts/tools/web_scrape/newspaper4k



## Code

```python cookbook/tools/newspaper4k_tools.py
from agno.agent import Agent
from agno.tools.newspaper4k import Newspaper4kTools

agent = Agent(
    tools=[Newspaper4kTools()],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("Analyze and summarize this news article: https://example.com/news")
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
    pip install -U newspaper4k openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/tools/newspaper4k_tools.py
      ```

      ```bash Windows
      python cookbook/tools/newspaper4k_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


