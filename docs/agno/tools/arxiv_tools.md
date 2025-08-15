---
title: ArXiv Tools
category: tools
source_lines: 29758-29804
line_count: 46
---

# ArXiv Tools
Source: https://docs.agno.com/examples/concepts/tools/search/arxiv



## Code

```python cookbook/tools/arxiv_tools.py
from agno.agent import Agent
from agno.tools.arxiv_toolkit import ArxivTools

agent = Agent(tools=[ArxivTools()], show_tool_calls=True)
agent.print_response("Search arxiv for 'language models'", markdown=True)
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
    pip install -U arxiv openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/tools/arxiv_tools.py
      ```

      ```bash Windows
      python cookbook/tools/arxiv_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


