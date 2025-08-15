---
title: Fal Tools
category: tools
source_lines: 28664-28726
line_count: 62
---

# Fal Tools
Source: https://docs.agno.com/examples/concepts/tools/others/fal



## Code

```python cookbook/tools/fal_tools.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.fal import FalTools

fal_agent = Agent(
    name="Fal Video Generator Agent",
    model=OpenAIChat(id="gpt-4o"),
    tools=[FalTools("fal-ai/hunyuan-video")],
    description="You are an AI agent that can generate videos using the Fal API.",
    instructions=[
        "When the user asks you to create a video, use the `generate_media` tool to create the video.",
        "Return the URL as raw to the user.",
        "Don't convert video URL to markdown or anything else.",
    ],
    markdown=True,
    debug_mode=True,
    show_tool_calls=True,
)

fal_agent.print_response("Generate video of balloon in the ocean")
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API keys">
    ```bash
    export FAL_KEY=xxx
    export OPENAI_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U fal openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/tools/fal_tools.py
      ```

      ```bash Windows
      python cookbook/tools/fal_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


