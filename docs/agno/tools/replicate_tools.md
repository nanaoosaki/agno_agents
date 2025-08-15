---
title: Replicate Tools
category: tools
source_lines: 29404-29455
line_count: 51
---

# Replicate Tools
Source: https://docs.agno.com/examples/concepts/tools/others/replicate



## Code

```python cookbook/tools/replicate_tools.py
from agno.agent import Agent
from agno.tools.replicate import ReplicateTools

agent = Agent(
    tools=[ReplicateTools()],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("Generate an image of a cyberpunk city")
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API token">
    ```bash
    export REPLICATE_API_TOKEN=xxx
    export OPENAI_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U replicate openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/tools/replicate_tools.py
      ```

      ```bash Windows
      python cookbook/tools/replicate_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


