---
title: Cal.com
category: misc
source_lines: 74819-74894
line_count: 75
---

# Cal.com
Source: https://docs.agno.com/tools/toolkits/others/calcom



## Prerequisites

The following example requires the `pytz` and `requests` libraries.

```shell
pip install requests pytz
```

```shell
export CALCOM_API_KEY="your_api_key"
export CALCOM_EVENT_TYPE_ID="your_event_type_id"
```

## Example

The following agent will use Cal.com to list all events in your Cal.com account for tomorrow.

```python cookbook/tools/calcom_tools.py

agent = Agent(
    name="Calendar Assistant",
    instructions=[
        f"You're scheduing assistant. Today is {datetime.now()}.",
        "You can help users by:",
        "- Finding available time slots",
        "- Creating new bookings",
        "- Managing existing bookings (view, reschedule, cancel) ",
        "- Getting booking details",
        "- IMPORTANT: In case of rescheduling or cancelling booking, call the get_upcoming_bookings function to get the booking uid. check available slots before making a booking for given time",
        "Always confirm important details before making bookings or changes.",
    ],
    model=OpenAIChat(id="gpt-4"),
    tools=[CalComTools(user_timezone="America/New_York")],
    show_tool_calls=True,
    markdown=True,
)

agent.print_response("What are my bookings for tomorrow?")
```

## Toolkit Params

| Parameter               | Type   | Default | Description                                |
| ----------------------- | ------ | ------- | ------------------------------------------ |
| `api_key`               | `str`  | `None`  | Cal.com API key                            |
| `event_type_id`         | `int`  | `None`  | Event type ID for scheduling               |
| `user_timezone`         | `str`  | `None`  | User's timezone (e.g. "America/New\_York") |
| `get_available_slots`   | `bool` | `True`  | Enable getting available time slots        |
| `create_booking`        | `bool` | `True`  | Enable creating new bookings               |
| `get_upcoming_bookings` | `bool` | `True`  | Enable getting upcoming bookings           |
| `reschedule_booking`    | `bool` | `True`  | Enable rescheduling bookings               |
| `cancel_booking`        | `bool` | `True`  | Enable canceling bookings                  |

## Toolkit Functions

| Function                | Description                                      |
| ----------------------- | ------------------------------------------------ |
| `get_available_slots`   | Gets available time slots for a given date range |
| `create_booking`        | Creates a new booking with provided details      |
| `get_upcoming_bookings` | Gets list of upcoming bookings                   |
| `get_booking_details`   | Gets details for a specific booking              |
| `reschedule_booking`    | Reschedules an existing booking                  |
| `cancel_booking`        | Cancels an existing booking                      |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/calcom.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/calcom_tools.py)


