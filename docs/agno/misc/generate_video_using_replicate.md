---
title: Generate Video using Replicate
category: misc
source_lines: 19013-19079
line_count: 66
---

# Generate Video using Replicate
Source: https://docs.agno.com/examples/concepts/multimodal/generate-video-replicate



## Code

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.replicate import ReplicateTools

video_agent = Agent(
    name="Video Generator Agent",
    model=OpenAIChat(id="gpt-4o"),
    tools=[
        ReplicateTools(
            model="tencent/hunyuan-video:847dfa8b01e739637fc76f480ede0c1d76408e1d694b830b5dfb8e547bf98405"
        )
    ],
    description="You are an AI agent that can generate videos using the Replicate API.",
    instructions=[
        "When the user asks you to create a video, use the `generate_media` tool to create the video.",
        "Return the URL as raw to the user.",
        "Don't convert video URL to markdown or anything else.",
    ],
    markdown=True,
    debug_mode=True,
    show_tool_calls=True,
)

video_agent.print_response("Generate a video of a horse in the dessert.")
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export OPENAI_API_KEY=xxx
    export REPLICATE_API_TOKEN=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U openai replicate agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/agent_concepts/multimodal/generate_video_using_replicate.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/multimodal/generate_video_using_replicate.py
      ```
    </CodeGroup>
  </Step>
</Steps>


