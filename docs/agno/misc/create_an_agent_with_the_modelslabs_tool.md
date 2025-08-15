---
title: Create an Agent with the ModelsLabs tool
category: misc
source_lines: 76455-76483
line_count: 28
---

# Create an Agent with the ModelsLabs tool
agent = Agent(tools=[ModelsLabsTools()], name="ModelsLabs Agent")

agent.print_response("Generate a video of a beautiful sunset over the ocean", markdown=True)
```

## Toolkit Params

| Parameter             | Type   | Default | Description                                                                |
| --------------------- | ------ | ------- | -------------------------------------------------------------------------- |
| `api_key`             | `str`  | `None`  | The ModelsLab API key for authentication                                   |
| `wait_for_completion` | `bool` | `False` | Whether to wait for the video to be ready                                  |
| `add_to_eta`          | `int`  | `15`    | Time to add to the ETA to account for the time it takes to fetch the video |
| `max_wait_time`       | `int`  | `60`    | Maximum time to wait for the video to be ready                             |
| `file_type`           | `str`  | `"mp4"` | The type of file to generate                                               |

## Toolkit Functions

| Function         | Description                                     |
| ---------------- | ----------------------------------------------- |
| `generate_media` | Generates a video or gif based on a text prompt |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/models_labs.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/models_labs_tools.py)


