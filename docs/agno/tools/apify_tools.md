---
title: Apify Tools
category: tools
source_lines: 27963-28010
line_count: 47
---

# Apify Tools
Source: https://docs.agno.com/examples/concepts/tools/others/apify



## Code

```python cookbook/tools/apify_tools.py
from agno.agent import Agent
from agno.tools.apify import ApifyTools

agent = Agent(tools=[ApifyTools()], show_tool_calls=True)
agent.print_response("Tell me about https://docs.agno.com/introduction", markdown=True)
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export APIFY_API_KEY=xxx
    export OPENAI_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U apify-client openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/tools/apify_tools.py
      ```

      ```bash Windows
      python cookbook/tools/apify_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


