---
title: Google Calendar Tools
category: tools
source_lines: 28915-28973
line_count: 58
---

# Google Calendar Tools
Source: https://docs.agno.com/examples/concepts/tools/others/google_calendar



## Code

```python cookbook/tools/google_calendar_tools.py
from agno.agent import Agent
from agno.tools.googlecalendar import GoogleCalendarTools

agent = Agent(
    tools=[GoogleCalendarTools()],
    show_tool_calls=True,
    markdown=True,
)

agent.print_response("What events do I have today?")
agent.print_response("Schedule a meeting with John tomorrow at 2pm")
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export OPENAI_API_KEY=xxx
    ```
  </Step>

  <Step title="Set up Google Calendar credentials">
    ```bash
    export GOOGLE_CALENDAR_CREDENTIALS=path/to/credentials.json
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U google-auth-oauthlib google-auth-httplib2 google-api-python-client openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/tools/google_calendar_tools.py
      ```

      ```bash Windows
      python cookbook/tools/google_calendar_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


