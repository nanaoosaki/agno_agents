---
title: Google Calendar
category: misc
source_lines: 76029-76141
line_count: 112
---

# Google Calendar
Source: https://docs.agno.com/tools/toolkits/others/googlecalendar



Enable an Agent to work with Google Calendar to view and schedule meetings.

## Prerequisites

### Install dependencies

```shell
pip install tzlocal
```

### Setup Google Project and OAuth

Reference: [https://developers.google.com/calendar/api/quickstart/python](https://developers.google.com/calendar/api/quickstart/python)

1. Enable Google Calender API

   * Go to [Google Cloud Console](https://console.cloud.google.com/apis/enableflow?apiid=calendar-json.googleapis.com).
   * Select Project and Enable.

2. Go To API & Service -> OAuth Consent Screen

3. Select User Type

   * If you are a Google Workspace user, select Internal.
   * Otherwise, select External.

4. Fill in the app details (App name, logo, support email, etc).

5. Select Scope

   * Click on Add or Remove Scope.
   * Search for Google Calender API (Make sure you've enabled Google calender API otherwise scopes wont be visible).
   * Select scopes accordingly
     * From the dropdown check on `/auth/calendar` scope
   * Save and continue.

6. Adding Test User

   * Click Add Users and enter the email addresses of the users you want to allow during testing.
   * NOTE : Only these users can access the app's OAuth functionality when the app is in "Testing" mode.
     Any other users will receive access denied errors.
   * To make the app available to all users, you'll need to move the app's status to "In Production".
     Before doing so, ensure the app is fully verified by Google if it uses sensitive or restricted scopes.
   * Click on Go back to Dashboard.

7. Generate OAuth 2.0 Client ID

   * Go to Credentials.
   * Click on Create Credentials -> OAuth Client ID
   * Select Application Type as Desktop app.
   * Download JSON.

8. Using Google Calender Tool
   * Pass the path of downloaded credentials as credentials\_path to Google Calender tool.
   * Optional: Set the `token_path` parameter to specify where the tool should create the `token.json` file.
   * The `token.json` file is used to store the user's access and refresh tokens and is automatically created during the authorization flow if it doesn't already exist.
   * If `token_path` is not explicitly provided, the file will be created in the default location which is your current working directory.
   * If you choose to specify `token_path`, please ensure that the directory you provide has write access, as the application needs to create or update this file during the authentication process.

## Example

The following agent will use GoogleCalendarTools to find today's events.

```python cookbook/tools/googlecalendar_tools.py
from agno.agent import Agent
from agno.tools.googlecalendar import GoogleCalendarTools
import datetime
import os
from tzlocal import get_localzone_name

agent = Agent(
    tools=[GoogleCalendarTools(credentials_path="<PATH_TO_YOUR_CREDENTIALS_FILE>")],
    show_tool_calls=True,
    instructions=[
        f"""
        You are scheduling assistant . Today is {datetime.datetime.now()} and the users timezone is {get_localzone_name()}.
        You should help users to perform these actions in their Google calendar:
            - get their scheduled events from a certain date and time
            - create events based on provided details
        """
    ],
    add_datetime_to_instructions=True,
)

agent.print_response("Give me the list of todays events", markdown=True)
```

## Toolkit Params

| Parameter          | Type  | Default | Description                                                                    |
| ------------------ | ----- | ------- | ------------------------------------------------------------------------------ |
| `credentials_path` | `str` | `None`  | Path of the file credentials.json file which contains OAuth 2.0 Client ID.     |
| `token_path`       | `str` | `None`  | Path of the file token.json which stores the user's access and refresh tokens. |

## Toolkit Functions

| Function       | Description                                        |
| -------------- | -------------------------------------------------- |
| `list_events`  | List events from the user's primary calendar.      |
| `create_event` | Create a new event in the user's primary calendar. |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/googlecalendar.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/googlecalendar_tools.py)


