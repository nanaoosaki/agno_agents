---
title: Jina Reader Tools
category: tools
source_lines: 31110-31160
line_count: 50
---

# Jina Reader Tools
Source: https://docs.agno.com/examples/concepts/tools/web_scrape/jina_reader



## Code

```python cookbook/tools/jina_reader_tools.py
from agno.agent import Agent
from agno.tools.jina_reader import JinaReaderTools

agent = Agent(
    tools=[JinaReaderTools()],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("Read and summarize this PDF: https://example.com/sample.pdf")
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
    pip install -U jina-reader openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/tools/jina_reader_tools.py
      ```

      ```bash Windows
      python cookbook/tools/jina_reader_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


