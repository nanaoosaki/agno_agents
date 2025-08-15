---
title: wget https://storage.googleapis.com/generativeai-downloads/images/GreatRedSpot.mp4
category: misc
source_lines: 1286-1342
line_count: 56
---

# wget https://storage.googleapis.com/generativeai-downloads/images/GreatRedSpot.mp4
video_path = Path(__file__).parent.joinpath("GreatRedSpot.mp4")

agent.print_response("Tell me about this video", videos=[Video(filepath=video_path)])
```

## Multimodal outputs from an agent

Similar to providing multimodal inputs, you can also get multimodal outputs from an agent.

### Image Generation

The following example demonstrates how to generate an image using DALL-E with an agent.

```python image_agent.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.dalle import DalleTools

image_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[DalleTools()],
    description="You are an AI agent that can generate images using DALL-E.",
    instructions="When the user asks you to create an image, use the `create_image` tool to create the image.",
    markdown=True,
    show_tool_calls=True,
)

image_agent.print_response("Generate an image of a white siamese cat")

images = image_agent.get_images()
if images and isinstance(images, list):
    for image_response in images:
        image_url = image_response.url
        print(image_url)
```

### Audio Response

The following example demonstrates how to obtain both text and audio responses from an agent. The agent will respond with text and audio bytes that can be saved to a file.

```python audio_agent.py
from agno.agent import Agent, RunResponse
from agno.models.openai import OpenAIChat
from agno.utils.audio import write_audio_to_file

agent = Agent(
    model=OpenAIChat(
        id="gpt-4o-audio-preview",
        modalities=["text", "audio"],
        audio={"voice": "alloy", "format": "wav"},
    ),
    markdown=True,
)
response: RunResponse = agent.run("Tell me a 5 second scary story")

