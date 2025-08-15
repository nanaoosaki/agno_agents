---
title: Tavily Tools
category: tools
source_lines: 30437-30488
line_count: 51
---

# Tavily Tools
Source: https://docs.agno.com/examples/concepts/tools/search/tavily



## Code

```python cookbook/tools/tavily_tools.py
from agno.agent import Agent
from agno.tools.tavily import TavilyTools

agent = Agent(
    tools=[TavilyTools()],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("Search for recent breakthroughs in quantum computing")
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API keys">
    ```bash
    export TAVILY_API_KEY=xxx
    export OPENAI_API_KEY=xxx 
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U openai tavily-python agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/tools/tavily_tools.py
      ```

      ```bash Windows
      python cookbook/tools/tavily_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


