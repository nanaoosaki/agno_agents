---
title: Lumalabs
category: misc
source_lines: 76261-76333
line_count: 72
---

# Lumalabs
Source: https://docs.agno.com/tools/toolkits/others/lumalabs



**LumaLabTools** enables an Agent to generate media using the [Lumalabs platform](https://lumalabs.ai/dream-machine).

## Prerequisites

```shell
export LUMAAI_API_KEY=***
```

The following example requires the `lumaai` library. To install the Lumalabs client, run the following command:

```shell
pip install -U lumaai
```

## Example

The following agent will use Lumalabs to generate any video requested by the user.

```python cookbook/tools/lumalabs_tool.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.lumalab import LumaLabTools

luma_agent = Agent(
    name="Luma Video Agent",
    model=OpenAIChat(id="gpt-4o"),
    tools=[LumaLabTools()],  # Using the LumaLab tool we created
    markdown=True,
    debug_mode=True,
    show_tool_calls=True,
    instructions=[
        "You are an agent designed to generate videos using the Luma AI API.",
        "You can generate videos in two ways:",
        "1. Text-to-Video Generation:",
        "2. Image-to-Video Generation:",
        "Choose the appropriate function based on whether the user provides image URLs or just a text prompt.",
        "The video will be displayed in the UI automatically below your response, so you don't need to show the video URL in your response.",
    ],
    system_message=(
        "Use generate_video for text-to-video requests and image_to_video for image-based "
        "generation. Don't modify default parameters unless specifically requested. "
        "Always provide clear feedback about the video generation status."
    ),
)

luma_agent.run("Generate a video of a car in a sky")
```

## Toolkit Params

| Parameter | Type  | Default | Description                                          |
| --------- | ----- | ------- | ---------------------------------------------------- |
| `api_key` | `str` | `None`  | If you want to manually supply the Lumalabs API key. |

## Toolkit Functions

| Function         | Description                                                           |
| ---------------- | --------------------------------------------------------------------- |
| `generate_video` | Generate a video from a prompt.                                       |
| `image_to_video` | Generate a video from a prompt, a starting image and an ending image. |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/lumalabs.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/lumalabs_tools.py)


