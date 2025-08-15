---
title: Send a message to a Space in Webex
category: misc
source_lines: 78449-78476
line_count: 27
---

# Send a message to a Space in Webex
agent.print_response(
    "Send a funny ice-breaking message to the webex Welcome space", markdown=True
)
```

## Toolkit Params

| Parameter      | Type   | Default | Description                                                                                             |
| -------------- | ------ | ------- | ------------------------------------------------------------------------------------------------------- |
| `access_token` | `str`  | `None`  | Webex access token for authentication. If not provided, uses WEBEX\_ACCESS\_TOKEN environment variable. |
| `send_message` | `bool` | `True`  | Enable sending messages to Webex spaces.                                                                |
| `list_rooms`   | `bool` | `True`  | Enable listing Webex spaces/rooms.                                                                      |

## Toolkit Functions

| Function       | Description                                                                                                     |
| -------------- | --------------------------------------------------------------------------------------------------------------- |
| `send_message` | Sends a message to a Webex room. Parameters: `room_id` (str) for the target room, `text` (str) for the message. |
| `list_rooms`   | Lists all available Webex rooms/spaces with their details including ID, title, type, and visibility settings.   |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/webex.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/webex_tools.py)


