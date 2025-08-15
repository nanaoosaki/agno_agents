---
title: Brave Search Tools
category: tools
source_lines: 29859-29912
line_count: 53
---

# Brave Search Tools
Source: https://docs.agno.com/examples/concepts/tools/search/bravesearch



## Code

```python cookbook/tools/bravesearch_tools.py
from agno.agent import Agent
from agno.tools.bravesearch import BraveSearchTools

agent = Agent(
    tools=[BraveSearchTools()],
    description="You are a news agent that helps users find the latest news.",
    instructions=[
        "Given a topic by the user, respond with 4 latest news items about that topic."
    ],
    show_tool_calls=True,
)
agent.print_response("AI Agents", markdown=True)
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API credentials">
    ```bash
    export BRAVE_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U brave-search openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/tools/bravesearch_tools.py
      ```

      ```bash Windows
      python cookbook/tools/bravesearch_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


