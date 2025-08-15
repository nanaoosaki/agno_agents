---
title: Schedule a meeting
category: misc
source_lines: 78737-78781
line_count: 44
---

# Schedule a meeting
response = agent.print_response("""
Schedule a team meeting with the following details:
- Topic: Weekly Team Sync
- Time: Tomorrow at 2 PM UTC
- Duration: 45 minutes
""", markdown=True)
```

## Toolkit Parameters

| Parameter       | Type  | Default | Description                                       |
| --------------- | ----- | ------- | ------------------------------------------------- |
| `account_id`    | `str` | `None`  | Zoom account ID (from Server-to-Server OAuth app) |
| `client_id`     | `str` | `None`  | Client ID (from Server-to-Server OAuth app)       |
| `client_secret` | `str` | `None`  | Client secret (from Server-to-Server OAuth app)   |

## Toolkit Functions

| Function                 | Description                                       |
| ------------------------ | ------------------------------------------------- |
| `schedule_meeting`       | Schedule a new Zoom meeting                       |
| `get_upcoming_meetings`  | Get a list of upcoming meetings                   |
| `list_meetings`          | List all meetings based on type                   |
| `get_meeting_recordings` | Get recordings for a specific meeting             |
| `delete_meeting`         | Delete a scheduled meeting                        |
| `get_meeting`            | Get detailed information about a specific meeting |

## Rate Limits

The Zoom API has rate limits that vary by endpoint and account type:

* Server-to-Server OAuth apps: 100 requests/second
* Meeting endpoints: Specific limits apply based on account type
* Recording endpoints: Lower rate limits, check Zoom documentation

For detailed rate limits, refer to [Zoom API Rate Limits](https://developers.zoom.us/docs/api/#rate-limits).

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/zoom.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/zoom_tools.py)


