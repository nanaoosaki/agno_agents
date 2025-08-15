---
title: Exa Tools
category: tools
source_lines: 30012-30062
line_count: 50
---

# Exa Tools
Source: https://docs.agno.com/examples/concepts/tools/search/exa



## Code

```python cookbook/tools/exa_tools.py
from agno.agent import Agent
from agno.tools.exa import ExaTools

agent = Agent(
    tools=[ExaTools(include_domains=["cnbc.com", "reuters.com", "bloomberg.com"])],
    show_tool_calls=True,
)
agent.print_response("Search for AAPL news", markdown=True)
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export EXA_API_KEY=xxx
    export OPENAI_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U exa-py openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/tools/exa_tools.py
      ```

      ```bash Windows
      python cookbook/tools/exa_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


