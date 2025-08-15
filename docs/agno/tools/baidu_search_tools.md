---
title: Baidu Search Tools
category: tools
source_lines: 29804-29859
line_count: 55
---

# Baidu Search Tools
Source: https://docs.agno.com/examples/concepts/tools/search/baidusearch



## Code

```python cookbook/tools/baidusearch_tools.py
from agno.agent import Agent
from agno.tools.baidusearch import BaiduSearchTools

agent = Agent(
    tools=[BaiduSearchTools()],
    description="You are a search agent that helps users find the most relevant information using Baidu.",
    instructions=[
        "Given a topic by the user, respond with the 3 most relevant search results about that topic.",
        "Search for 5 results and select the top 3 unique items.",
        "Search in both English and Chinese.",
    ],
    show_tool_calls=True,
)
agent.print_response("What are the latest advancements in AI?", markdown=True)
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
    pip install -U openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/tools/baidusearch_tools.py
      ```

      ```bash Windows
      python cookbook/tools/baidusearch_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


