---
title: Discord
category: misc
source_lines: 78022-78078
line_count: 56
---

# Discord
Source: https://docs.agno.com/tools/toolkits/social/discord



**DiscordTools** enable an agent to send messages, read message history, manage channels, and delete messages in Discord.

## Prerequisites

The following example requires a Discord bot token which can be obtained from [here](https://discord.com/developers/applications).

```shell
export DISCORD_BOT_TOKEN=***
```

## Example

```python cookbook/tools/discord.py
from agno.agent import Agent
from agno.tools.discord import DiscordTools

agent = Agent(
    tools=[DiscordTools()],
    show_tool_calls=True,
    markdown=True,
)

agent.print_response("Send 'Hello World!' to channel 1234567890", markdown=True)
```

## Toolkit Params

| Parameter                   | Type   | Default | Description                                                   |
| --------------------------- | ------ | ------- | ------------------------------------------------------------- |
| `bot_token`                 | `str`  | -       | Discord bot token for authentication.                         |
| `enable_messaging`          | `bool` | `True`  | Whether to enable sending messages to channels.               |
| `enable_history`            | `bool` | `True`  | Whether to enable retrieving message history from channels.   |
| `enable_channel_management` | `bool` | `True`  | Whether to enable fetching channel info and listing channels. |
| `enable_message_management` | `bool` | `True`  | Whether to enable deleting messages from channels.            |

## Toolkit Functions

| Function               | Description                                                                                   |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| `send_message`         | Send a message to a specified channel. Returns a success or error message.                    |
| `get_channel_info`     | Retrieve information about a specified channel. Returns the channel info as a JSON string.    |
| `list_channels`        | List all channels in a specified server (guild). Returns the list of channels as JSON.        |
| `get_channel_messages` | Retrieve message history from a specified channel. Returns messages as a JSON string.         |
| `delete_message`       | Delete a specific message by ID from a specified channel. Returns a success or error message. |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/discord.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/discord.py)


