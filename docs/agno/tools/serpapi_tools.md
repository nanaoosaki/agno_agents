---
title: SerpAPI Tools
category: tools
source_lines: 30305-30356
line_count: 51
---

# SerpAPI Tools
Source: https://docs.agno.com/examples/concepts/tools/search/serpapi



## Code

```python cookbook/tools/serpapi_tools.py
from agno.agent import Agent
from agno.tools.serpapi import SerpAPITools

agent = Agent(
    tools=[SerpAPITools()],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("What are the top search results for 'machine learning'?")
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export SERPAPI_API_KEY=xxx
    export OPENAI_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U google-search-results openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/tools/serpapi_tools.py
      ```

      ```bash Windows
      python cookbook/tools/serpapi_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


