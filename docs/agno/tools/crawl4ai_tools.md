---
title: Crawl4ai Tools
category: tools
source_lines: 29912-29958
line_count: 46
---

# Crawl4ai Tools
Source: https://docs.agno.com/examples/concepts/tools/search/crawl4ai



## Code

```python cookbook/tools/crawl4ai_tools.py
from agno.agent import Agent
from agno.tools.crawl4ai import Crawl4aiTools

agent = Agent(tools=[Crawl4aiTools(max_length=None)], show_tool_calls=True)
agent.print_response("Tell me about https://github.com/agno-agi/agno.")
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
    pip install -U crawl4ai openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/tools/crawl4ai_tools.py
      ```

      ```bash Windows
      python cookbook/tools/crawl4ai_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


