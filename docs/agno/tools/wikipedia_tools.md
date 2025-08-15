---
title: Wikipedia Tools
category: tools
source_lines: 30488-30538
line_count: 50
---

# Wikipedia Tools
Source: https://docs.agno.com/examples/concepts/tools/search/wikipedia



## Code

```python cookbook/tools/wikipedia_tools.py
from agno.agent import Agent
from agno.tools.wikipedia import WikipediaTools

agent = Agent(
    tools=[WikipediaTools()],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("Search Wikipedia for information about artificial intelligence")
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
    pip install -U wikipedia openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/tools/wikipedia_tools.py
      ```

      ```bash Windows
      python cookbook/tools/wikipedia_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


