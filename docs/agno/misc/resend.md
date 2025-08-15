---
title: Resend
category: misc
source_lines: 76754-76807
line_count: 53
---

# Resend
Source: https://docs.agno.com/tools/toolkits/others/resend



**ResendTools** enable an Agent to send emails using Resend

## Prerequisites

The following example requires the `resend` library and an API key from [Resend](https://resend.com/).

```shell
pip install -U resend
```

```shell
export RESEND_API_KEY=***
```

## Example

The following agent will send an email using Resend

```python cookbook/tools/resend_tools.py
from agno.agent import Agent
from agno.tools.resend import ResendTools

from_email = "<enter_from_email>"
to_email = "<enter_to_email>"

agent = Agent(tools=[ResendTools(from_email=from_email)], show_tool_calls=True)
agent.print_response(f"Send an email to {to_email} greeting them with hello world")
```

## Toolkit Params

| Parameter    | Type  | Default | Description                                                   |
| ------------ | ----- | ------- | ------------------------------------------------------------- |
| `api_key`    | `str` | -       | API key for authentication purposes.                          |
| `from_email` | `str` | -       | The email address used as the sender in email communications. |

## Toolkit Functions

| Function     | Description                         |
| ------------ | ----------------------------------- |
| `send_email` | Send an email using the Resend API. |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/resend.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/resend_tools.py)


