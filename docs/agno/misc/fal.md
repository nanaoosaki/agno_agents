---
title: Fal
category: misc
source_lines: 75564-75630
line_count: 66
---

# Fal
Source: https://docs.agno.com/tools/toolkits/others/fal



**FalTools** enable an Agent to perform media generation tasks.

## Prerequisites

The following example requires the `fal_client` library and an API key which can be obtained from [Fal](https://fal.ai/).

```shell
pip install -U fal_client
```

```shell
export FAL_KEY=***
```

## Example

The following agent will use FAL to generate any video requested by the user.

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

## Toolkit Params

| Parameter | Type  | Default | Description                                |
| --------- | ----- | ------- | ------------------------------------------ |
| `api_key` | `str` | `None`  | API key for authentication purposes.       |
| `model`   | `str` | `None`  | The model to use for the media generation. |

## Toolkit Functions

| Function         | Description                                                    |
| ---------------- | -------------------------------------------------------------- |
| `generate_media` | Generate either images or videos depending on the user prompt. |
| `image_to_image` | Transform an input image based on a text prompt.               |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/fal.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/fal_tools.py)


