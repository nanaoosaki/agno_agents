---
title: Gmail
category: misc
source_lines: 78131-78205
line_count: 74
---

# Gmail
Source: https://docs.agno.com/tools/toolkits/social/gmail



**Gmail** enables an Agent to interact with Gmail, allowing it to read, search, send, and manage emails.

## Prerequisites

The Gmail toolkit requires Google API client libraries and proper authentication setup. Install the required dependencies:

```shell
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

You'll also need to set up Google Cloud credentials:

1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Create a project or select an existing one
3. Enable the Gmail API
4. Create OAuth 2.0 credentials
5. Set up environment variables:

```shell
export GOOGLE_CLIENT_ID=your_client_id_here
export GOOGLE_CLIENT_SECRET=your_client_secret_here
export GOOGLE_PROJECT_ID=your_project_id_here
export GOOGLE_REDIRECT_URI=http://localhost  # Default value
```

## Example

```python cookbook/tools/gmail_tools.py
from agno.agent import Agent
from agno.tools.gmail import GmailTools

agent = Agent(tools=[GmailTools()], show_tool_calls=True)
agent.print_response("Show me my latest 5 unread emails", markdown=True)
```

## Toolkit Params

| Parameter               | Type   | Default | Description                                 |
| ----------------------- | ------ | ------- | ------------------------------------------- |
| `get_latest_emails`     | `bool` | `True`  | Enable retrieving latest emails from inbox  |
| `get_emails_from_user`  | `bool` | `True`  | Enable getting emails from specific senders |
| `get_unread_emails`     | `bool` | `True`  | Enable fetching unread emails               |
| `get_starred_emails`    | `bool` | `True`  | Enable retrieving starred emails            |
| `get_emails_by_context` | `bool` | `True`  | Enable searching emails by context          |
| `get_emails_by_date`    | `bool` | `True`  | Enable retrieving emails within date ranges |
| `create_draft_email`    | `bool` | `True`  | Enable creating email drafts                |
| `send_email`            | `bool` | `True`  | Enable sending emails                       |
| `search_emails`         | `bool` | `True`  | Enable searching emails                     |

## Toolkit Functions

| Function                | Description                                        |
| ----------------------- | -------------------------------------------------- |
| `get_latest_emails`     | Get the latest X emails from the user's inbox      |
| `get_emails_from_user`  | Get X number of emails from a specific sender      |
| `get_unread_emails`     | Get the latest X unread emails                     |
| `get_starred_emails`    | Get X number of starred emails                     |
| `get_emails_by_context` | Get X number of emails matching a specific context |
| `get_emails_by_date`    | Get emails within a specific date range            |
| `create_draft_email`    | Create and save an email draft                     |
| `send_email`            | Send an email immediately                          |
| `search_emails`         | Search emails using natural language queries       |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/gmail.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/gmail_tools.py)


