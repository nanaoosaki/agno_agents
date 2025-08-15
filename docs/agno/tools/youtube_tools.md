---
title: YouTube Tools
category: tools
source_lines: 29649-29700
line_count: 51
---

# YouTube Tools
Source: https://docs.agno.com/examples/concepts/tools/others/youtube



## Code

```python cookbook/tools/youtube_tools.py
from agno.agent import Agent
from agno.tools.youtube import YouTubeTools

agent = Agent(
    tools=[YouTubeTools()],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("Search for recent videos about artificial intelligence")
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export YOUTUBE_API_KEY=xxx
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
      python cookbook/tools/youtube_tools.py
      ```

      ```bash Windows
      python cookbook/tools/youtube_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


