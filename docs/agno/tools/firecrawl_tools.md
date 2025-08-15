---
title: Firecrawl Tools
category: tools
source_lines: 31059-31110
line_count: 51
---

# Firecrawl Tools
Source: https://docs.agno.com/examples/concepts/tools/web_scrape/firecrawl

Use Firecrawl with Agno to scrape and crawl the web.

## Code

```python cookbook/tools/firecrawl_tools.py
from agno.agent import Agent
from agno.tools.firecrawl import FirecrawlTools

agent = Agent(
    tools=[FirecrawlTools(scrape=False, crawl=True)],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("Summarize this https://finance.yahoo.com/")
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export FIRECRAWL_API_KEY=xxx
    export OPENAI_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U firecrawl openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/tools/firecrawl_tools.py
      ```

      ```bash Windows
      python cookbook/tools/firecrawl_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


