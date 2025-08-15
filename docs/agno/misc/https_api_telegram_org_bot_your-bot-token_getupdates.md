---
title: https://api.telegram.org/bot/<your-bot-token>/getUpdates
category: misc
source_lines: 78302-78334
line_count: 32
---

#    https://api.telegram.org/bot/<your-bot-token>/getUpdates

telegram_token = "<enter-your-bot-token>"
chat_id = "<enter-your-chat-id>"

agent = Agent(
    name="telegram",
    tools=[TelegramTools(token=telegram_token, chat_id=chat_id)],
)

agent.print_response("Send message to telegram chat a paragraph about the moon")
```

## Toolkit Params

| Parameter | Type              | Default | Description                                                                               |
| --------- | ----------------- | ------- | ----------------------------------------------------------------------------------------- |
| `token`   | `Optional[str]`   | `None`  | Telegram Bot API token. If not provided, will check TELEGRAM\_TOKEN environment variable. |
| `chat_id` | `Union[str, int]` | -       | The ID of the chat to send messages to.                                                   |

## Toolkit Functions

| Function       | Description                                                                                                                                                         |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `send_message` | Sends a message to the specified Telegram chat. Takes a message string as input and returns the API response as text. If an error occurs, returns an error message. |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/telegram.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/telegram_tools.py)


