---
title: Spider Tools
category: tools
source_lines: 31310-31360
line_count: 50
---

# Spider Tools
Source: https://docs.agno.com/examples/concepts/tools/web_scrape/spider



## Code

```python cookbook/tools/spider_tools.py
from agno.agent import Agent
from agno.tools.spider import SpiderTools

agent = Agent(
    tools=[SpiderTools()],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("Crawl https://example.com and extract all links")
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
    pip install -U scrapy openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/tools/spider_tools.py
      ```

      ```bash Windows
      python cookbook/tools/spider_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


