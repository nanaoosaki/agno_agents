---
title: Google Search Tools
category: tools
source_lines: 30062-30114
line_count: 52
---

# Google Search Tools
Source: https://docs.agno.com/examples/concepts/tools/search/google_search



## Code

```python cookbook/tools/googlesearch_tools.py
from agno.agent import Agent
from agno.tools.googlesearch import GoogleSearchTools

agent = Agent(
    tools=[GoogleSearchTools()],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("What are the latest developments in AI?")
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API credentials">
    ```bash
    export GOOGLE_CSE_ID=xxx
    export GOOGLE_API_KEY=xxx
    export OPENAI_API_KEY=xxx 
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U google-api-python-client openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/tools/googlesearch_tools.py
      ```

      ```bash Windows
      python cookbook/tools/googlesearch_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


