---
title: Example 2: Generate an image with custom settings
category: misc
source_lines: 75217-75252
line_count: 35
---

# Example 2: Generate an image with custom settings
custom_dalle = Dalle(model="dall-e-3", size="1792x1024", quality="hd", style="natural")

agent_custom = Agent(
    tools=[custom_dalle],
    name="Custom DALL-E Generator",
    show_tool_calls=True,
)

agent_custom.print_response("Create a panoramic nature scene showing a peaceful mountain lake at sunset", markdown=True)
```

## Toolkit Params

| Parameter | Type  | Default       | Description                                                       |
| --------- | ----- | ------------- | ----------------------------------------------------------------- |
| `model`   | `str` | `"dall-e-3"`  | The DALL-E model to use                                           |
| `n`       | `int` | `1`           | Number of images to generate                                      |
| `size`    | `str` | `"1024x1024"` | Image size (256x256, 512x512, 1024x1024, 1792x1024, or 1024x1792) |
| `quality` | `str` | `"standard"`  | Image quality (standard or hd)                                    |
| `style`   | `str` | `"vivid"`     | Image style (vivid or natural)                                    |
| `api_key` | `str` | `None`        | The OpenAI API key for authentication                             |

## Toolkit Functions

| Function         | Description                               |
| ---------------- | ----------------------------------------- |
| `generate_image` | Generates an image based on a text prompt |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/dalle.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/dalle_tools.py)


