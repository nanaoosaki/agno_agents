---
title: Slack
category: misc
source_lines: 78205-78238
line_count: 33
---

# Slack
Source: https://docs.agno.com/tools/toolkits/social/slack



## Prerequisites

The following example requires the `slack-sdk` library.

```shell
pip install openai slack-sdk
```

Get a Slack token from [here](https://api.slack.com/tutorials/tracks/getting-a-token).

```shell
export SLACK_TOKEN=***
```

## Example

The following agent will use Slack to send a message to a channel, list all channels, and get the message history of a specific channel.

```python cookbook/tools/slack_tools.py
import os

from agno.agent import Agent
from agno.tools.slack import SlackTools

slack_tools = SlackTools()

agent = Agent(tools=[slack_tools], show_tool_calls=True)

