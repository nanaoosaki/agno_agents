---
title: Example 3: Get the message history of a specific channel by channel ID
category: misc
source_lines: 78244-78272
line_count: 28
---

# Example 3: Get the message history of a specific channel by channel ID
agent.print_response("Get the last 10 messages from the channel 1231241", markdown=True)

```

## Toolkit Params

| Parameter             | Type   | Default | Description                                                         |
| --------------------- | ------ | ------- | ------------------------------------------------------------------- |
| `token`               | `str`  | -       | Slack API token for authentication                                  |
| `send_message`        | `bool` | `True`  | Enables the functionality to send messages to Slack channels        |
| `list_channels`       | `bool` | `True`  | Enables the functionality to list available Slack channels          |
| `get_channel_history` | `bool` | `True`  | Enables the functionality to retrieve message history from channels |

## Toolkit Functions

| Function              | Description                                         |
| --------------------- | --------------------------------------------------- |
| `send_message`        | Sends a message to a specified Slack channel        |
| `list_channels`       | Lists all available channels in the Slack workspace |
| `get_channel_history` | Retrieves message history from a specified channel  |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/slack.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/slack_tools.py)


