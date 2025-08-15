---
title: File Tools
category: tools
source_lines: 26716-26766
line_count: 50
---

# File Tools
Source: https://docs.agno.com/examples/concepts/tools/local/file



## Code

```python cookbook/tools/file_tools.py
from pathlib import Path

from agno.agent import Agent
from agno.tools.file import FileTools

agent = Agent(tools=[FileTools(Path("tmp/file"))], show_tool_calls=True)
agent.print_response(
    "What is the most advanced LLM currently? Save the answer to a file.", markdown=True
)
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
      python cookbook/tools/file_tools.py
      ```

      ```bash Windows
      python cookbook/tools/file_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


