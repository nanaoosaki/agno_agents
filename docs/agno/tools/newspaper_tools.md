---
title: Newspaper Tools
category: tools
source_lines: 31160-31210
line_count: 50
---

# Newspaper Tools
Source: https://docs.agno.com/examples/concepts/tools/web_scrape/newspaper



## Code

```python cookbook/tools/newspaper_tools.py
from agno.agent import Agent
from agno.tools.newspaper import NewspaperTools

agent = Agent(
    tools=[NewspaperTools()],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("Extract the main article content from https://example.com/article")
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
    pip install -U newspaper3k openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/tools/newspaper_tools.py
      ```

      ```bash Windows
      python cookbook/tools/newspaper_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


