---
title: Twilio
category: misc
source_lines: 78334-78401
line_count: 67
---

# Twilio
Source: https://docs.agno.com/tools/toolkits/social/twilio



**TwilioTools** enables an Agent to interact with [Twilio](https://www.twilio.com/docs) services, such as sending SMS, retrieving call details, and listing messages.

## Prerequisites

The following examples require the `twilio` library and appropriate Twilio credentials, which can be obtained from [here](https://www.twilio.com/console).

```shell
pip install twilio
```

Set the following environment variables:

```shell
export TWILIO_ACCOUNT_SID=***
export TWILIO_AUTH_TOKEN=***
```

## Example

The following agent will send an SMS message using Twilio:

```python
from agno.agent import Agent
from agno.tools.twilio import TwilioTools

agent = Agent(
    instructions=[
        "Use your tools to send SMS using Twilio.",
    ],
    tools=[TwilioTools(debug=True)],
    show_tool_calls=True,
)

agent.print_response("Send an SMS to +1234567890", markdown=True)
```

## Toolkit Params

| Name          | Type            | Default | Description                                       |
| ------------- | --------------- | ------- | ------------------------------------------------- |
| `account_sid` | `Optional[str]` | `None`  | Twilio Account SID for authentication.            |
| `auth_token`  | `Optional[str]` | `None`  | Twilio Auth Token for authentication.             |
| `api_key`     | `Optional[str]` | `None`  | Twilio API Key for alternative authentication.    |
| `api_secret`  | `Optional[str]` | `None`  | Twilio API Secret for alternative authentication. |
| `region`      | `Optional[str]` | `None`  | Optional Twilio region (e.g., `au1`).             |
| `edge`        | `Optional[str]` | `None`  | Optional Twilio edge location (e.g., `sydney`).   |
| `debug`       | `bool`          | `False` | Enable debug logging for troubleshooting.         |

## Toolkit Functions

| Function           | Description                                                                                                                                                                 |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `send_sms`         | Sends an SMS to a recipient. Takes recipient phone number, sender number (Twilio), and message body. Returns message SID if successful or error message if failed.          |
| `get_call_details` | Retrieves details of a call using its SID. Takes the call SID and returns a dictionary with call details (e.g., status, duration).                                          |
| `list_messages`    | Lists recent SMS messages. Takes a limit for the number of messages to return (default 20). Returns a list of message details (e.g., SID, sender, recipient, body, status). |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/twilio.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/twilio_tools.py)


