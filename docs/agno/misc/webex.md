---
title: Webex
category: misc
source_lines: 78401-78446
line_count: 45
---

# Webex
Source: https://docs.agno.com/tools/toolkits/social/webex



**WebexTools** enable an Agent to interact with Cisco Webex, allowing it to send messages and list rooms.

## Prerequisites

The following example requires the `webexpythonsdk` library and a Webex access token which can be obtained from [Webex Developer Portal](https://developer.webex.com/docs/bots).

To get started with Webex:

1. **Create a Webex Bot:**
   * Go to the [Developer Portal](https://developer.webex.com/)
   * Navigate to My Webex Apps → Create a Bot
   * Fill in the bot details and click Add Bot

2. **Get your access token:**
   * Copy the token shown after bot creation
   * Or regenerate via My Webex Apps → Edit Bot
   * Set as WEBEX\_ACCESS\_TOKEN environment variable

3. **Add the bot to Webex:**
   * Launch Webex and add the bot to a space
   * Use the bot's email (e.g. [test@webex.bot](mailto:test@webex.bot))

```shell
pip install webexpythonsdk
```

```shell
export WEBEX_ACCESS_TOKEN=your_access_token_here
```

## Example

The following agent will list all spaces and send a message using Webex:

```python cookbook/tools/webex_tool.py
from agno.agent import Agent
from agno.tools.webex import WebexTools

agent = Agent(tools=[WebexTools()], show_tool_calls=True)

