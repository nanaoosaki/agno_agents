---
title: Google Sheets
category: misc
source_lines: 75927-76029
line_count: 102
---

# Google Sheets
Source: https://docs.agno.com/tools/toolkits/others/google_sheets



**GoogleSheetsTools** enable an Agent to interact with Google Sheets API for reading, creating, updating, and duplicating spreadsheets.

## Prerequisites

You need to install the required Google API client libraries:

```bash
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

Set up the following environment variables:

```bash
export GOOGLE_CLIENT_ID=your_client_id_here
export GOOGLE_CLIENT_SECRET=your_client_secret_here
export GOOGLE_PROJECT_ID=your_project_id_here
export GOOGLE_REDIRECT_URI=your_redirect_uri_here
```

## How to Get Credentials

1. Go to Google Cloud Console ([https://console.cloud.google.com](https://console.cloud.google.com))

2. Create a new project or select an existing one

3. Enable the Google Sheets API:
   * Go to "APIs & Services" > "Enable APIs and Services"
   * Search for "Google Sheets API"
   * Click "Enable"

4. Create OAuth 2.0 credentials:
   * Go to "APIs & Services" > "Credentials"
   * Click "Create Credentials" > "OAuth client ID"
   * Go through the OAuth consent screen setup
   * Give it a name and click "Create"
   * You'll receive:
     * Client ID (GOOGLE\_CLIENT\_ID)
     * Client Secret (GOOGLE\_CLIENT\_SECRET)
   * The Project ID (GOOGLE\_PROJECT\_ID) is visible in the project dropdown at the top of the page

## Example

The following agent will use Google Sheets to read and update spreadsheet data.

```python cookbook/tools/googlesheets_tools.py
from agno.agent import Agent
from agno.tools.googlesheets import GoogleSheetsTools

SAMPLE_SPREADSHEET_ID = "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms"
SAMPLE_RANGE_NAME = "Class Data!A2:E"

google_sheets_tools = GoogleSheetsTools(
    spreadsheet_id=SAMPLE_SPREADSHEET_ID,
    spreadsheet_range=SAMPLE_RANGE_NAME,
)

agent = Agent(
    tools=[google_sheets_tools],
    instructions=[
        "You help users interact with Google Sheets using tools that use the Google Sheets API",
        "Before asking for spreadsheet details, first attempt the operation as the user may have already configured the ID and range in the constructor",
    ],
)
agent.print_response("Please tell me about the contents of the spreadsheet")

```

## Toolkit Params

| Parameter           | Type          | Default | Description                                             |
| ------------------- | ------------- | ------- | ------------------------------------------------------- |
| `scopes`            | `List[str]`   | `None`  | Custom OAuth scopes. If None, determined by operations. |
| `spreadsheet_id`    | `str`         | `None`  | ID of the target spreadsheet.                           |
| `spreadsheet_range` | `str`         | `None`  | Range within the spreadsheet.                           |
| `creds`             | `Credentials` | `None`  | Pre-existing credentials.                               |
| `creds_path`        | `str`         | `None`  | Path to credentials file.                               |
| `token_path`        | `str`         | `None`  | Path to token file.                                     |
| `read`              | `bool`        | `True`  | Enable read operations.                                 |
| `create`            | `bool`        | `False` | Enable create operations.                               |
| `update`            | `bool`        | `False` | Enable update operations.                               |
| `duplicate`         | `bool`        | `False` | Enable duplicate operations.                            |

## Toolkit Functions

| Function                 | Description                                    |
| ------------------------ | ---------------------------------------------- |
| `read_sheet`             | Read values from a Google Sheet                |
| `create_sheet`           | Create a new Google Sheet                      |
| `update_sheet`           | Update data in a Google Sheet                  |
| `create_duplicate_sheet` | Create a duplicate of an existing Google Sheet |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/googlesheets.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/googlesheets_tools.py)


