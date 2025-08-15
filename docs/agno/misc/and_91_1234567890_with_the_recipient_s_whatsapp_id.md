---
title: and +91 1234567890 with the recipient's WhatsApp ID
category: misc
source_lines: 78533-78564
line_count: 31
---

# and +91 1234567890 with the recipient's WhatsApp ID
agent.print_response(
    "Send a template message using the '''hello_world''' template in English to +91 1234567890"
)
```

## Toolkit Params

| Parameter         | Type            | Default   | Description                                                                                                               |
| ----------------- | --------------- | --------- | ------------------------------------------------------------------------------------------------------------------------- |
| `access_token`    | `Optional[str]` | `None`    | WhatsApp Business API access token. If not provided, uses `WHATSAPP_ACCESS_TOKEN` environment variable.                   |
| `phone_number_id` | `Optional[str]` | `None`    | WhatsApp Business Account phone number ID. If not provided, uses `WHATSAPP_PHONE_NUMBER_ID` environment variable.         |
| `version`         | `str`           | `"v22.0"` | API version to use. If not provided, uses `WHATSAPP_VERSION` environment variable or defaults to "v22.0".                 |
| `recipient_waid`  | `Optional[str]` | `None`    | Default recipient WhatsApp ID (e.g., "1234567890"). If not provided, uses `WHATSAPP_RECIPIENT_WAID` environment variable. |
| `async_mode`      | `bool`          | `False`   | Enable asynchronous methods for sending messages.                                                                         |

## Toolkit Functions

| Function                      | Description                                                                                                                                                                                           |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `send_text_message_sync`      | Sends a text message to a WhatsApp user (synchronous). Parameters: `text` (str), `recipient` (Optional\[str]), `preview_url` (bool), `recipient_type` (str).                                          |
| `send_template_message_sync`  | Sends a template message to a WhatsApp user (synchronous). Parameters: `recipient` (Optional\[str]), `template_name` (str), `language_code` (str), `components` (Optional\[List\[Dict\[str, Any]]]).  |
| `send_text_message_async`     | Sends a text message to a WhatsApp user (asynchronous). Parameters: `text` (str), `recipient` (Optional\[str]), `preview_url` (bool), `recipient_type` (str).                                         |
| `send_template_message_async` | Sends a template message to a WhatsApp user (asynchronous). Parameters: `recipient` (Optional\[str]), `template_name` (str), `language_code` (str), `components` (Optional\[List\[Dict\[str, Any]]]). |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/whatsapp.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/whatsapp_tools.py)


