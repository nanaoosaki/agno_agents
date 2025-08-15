---
title: MLX Transcribe Tools
category: tools
source_lines: 29252-29302
line_count: 50
---

# MLX Transcribe Tools
Source: https://docs.agno.com/examples/concepts/tools/others/mlx_transcribe



## Code

```python cookbook/tools/mlx_transcribe_tools.py
from agno.agent import Agent
from agno.tools.mlx_transcribe import MLXTranscribeTools

agent = Agent(
    tools=[MLXTranscribeTools()],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("Transcribe this audio file: path/to/audio.mp3")
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
    pip install -U mlx-transcribe openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/tools/mlx_transcribe_tools.py
      ```

      ```bash Windows
      python cookbook/tools/mlx_transcribe_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


