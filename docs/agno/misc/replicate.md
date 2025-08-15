---
title: Replicate
category: misc
source_lines: 76687-76754
line_count: 67
---

# Replicate
Source: https://docs.agno.com/tools/toolkits/others/replicate



**ReplicateTools** enables an Agent to generate media using the [Replicate platform](https://replicate.com/).

## Prerequisites

```shell
export REPLICATE_API_TOKEN=***
```

The following example requires the `replicate` library. To install the Replicate client, run the following command:

```shell
pip install -U replicate
```

## Example

The following agent will use Replicate to generate images or videos requested by the user.

```python cookbook/tools/replicate_tool.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.replicate import ReplicateTools

"""Create an agent specialized for Replicate AI content generation"""

image_agent = Agent(
    name="Image Generator Agent",
    model=OpenAIChat(id="gpt-4o"),
    tools=[ReplicateTools(model="luma/photon-flash")],
    description="You are an AI agent that can generate images using the Replicate API.",
    instructions=[
        "When the user asks you to create an image, use the `generate_media` tool to create the image.",
        "Return the URL as raw to the user.",
        "Don't convert image URL to markdown or anything else.",
    ],
    markdown=True,
    debug_mode=True,
    show_tool_calls=True,
)

image_agent.print_response("Generate an image of a horse in the dessert.")
```

## Toolkit Params

| Parameter | Type  | Default            | Description                                                          |
| --------- | ----- | ------------------ | -------------------------------------------------------------------- |
| `api_key` | `str` | `None`             | If you want to manually supply the Replicate API key.                |
| `model`   | `str` | `minimax/video-01` | The replicate model to use. Find out more on the Replicate platform. |

## Toolkit Functions

| Function         | Description                                                                         |
| ---------------- | ----------------------------------------------------------------------------------- |
| `generate_media` | Generate either an image or a video from a prompt. The output depends on the model. |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/replicate.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/replicate_tools.py)


