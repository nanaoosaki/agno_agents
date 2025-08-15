---
title: Telegram
category: misc
source_lines: 78272-78297
line_count: 25
---

# Telegram
Source: https://docs.agno.com/tools/toolkits/social/telegram



**TelegramTools** enable an Agent to send messages to a Telegram chat using the Telegram Bot API.

## Prerequisites

```shell
pip install -U agno httpx
```

```shell
export TELEGRAM_TOKEN=***
```

## Example

The following agent will send a message to a Telegram chat.

```python cookbook/tools/tavily_tools.py
from agno.agent import Agent
from agno.tools.telegram import TelegramTools

