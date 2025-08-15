---
title: Generate Video using Models Lab
category: misc
source_lines: 18952-19013
line_count: 61
---

# Generate Video using Models Lab
Source: https://docs.agno.com/examples/concepts/multimodal/generate-video-models-lab



## Code

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.models_labs import ModelsLabTools

video_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[ModelsLabTools()],
    description="You are an AI agent that can generate videos using the ModelsLabs API.",
    instructions=[
        "When the user asks you to create a video, use the `generate_media` tool to create the video.",
        "The video will be displayed in the UI automatically below your response, so you don't need to show the video URL in your response.",
        "Politely and courteously let the user know that the video has been generated and will be displayed below as soon as its ready.",
    ],
    markdown=True,
    debug_mode=True,
    show_tool_calls=True,
)

video_agent.print_response("Generate a video of a cat playing with a ball")
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export OPENAI_API_KEY=xxx
    export MODELS_LAB_API_KEY=xxx
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
      python cookbook/agent_concepts/multimodal/generate_video_using_models_lab.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/multimodal/generate_video_using_models_lab.py
      ```
    </CodeGroup>
  </Step>
</Steps>


