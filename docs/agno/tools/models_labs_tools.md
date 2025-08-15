---
title: Models Labs Tools
category: tools
source_lines: 29302-29353
line_count: 51
---

# Models Labs Tools
Source: https://docs.agno.com/examples/concepts/tools/others/models_labs



## Code

```python cookbook/tools/models_labs_tools.py
from agno.agent import Agent
from agno.tools.models_labs import ModelsLabsTools

agent = Agent(
    tools=[ModelsLabsTools()],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("Generate an image of a sunset over mountains")
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export MODELS_LABS_API_KEY=xxx
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
      python cookbook/tools/models_labs_tools.py
      ```

      ```bash Windows
      python cookbook/tools/models_labs_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


