---
title: Cal.com Tools
category: tools
source_lines: 28175-28243
line_count: 68
---

# Cal.com Tools
Source: https://docs.agno.com/examples/concepts/tools/others/calcom



## Code

```python cookbook/tools/calcom_tools.py
from datetime import datetime

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.calcom import CalComTools

agent = Agent(
    name="Calendar Assistant",
    instructions=[
        f"You're scheduing assistant. Today is {datetime.now()}.",
        "You can help users by:",
        "    - Finding available time slots",
        "    - Creating new bookings",
        "    - Managing existing bookings (view, reschedule, cancel)",
        "    - Getting booking details",
        "    - IMPORTANT: In case of rescheduling or cancelling booking, call the get_upcoming_bookings function to get the booking uid. check available slots before making a booking for given time",
        "Always confirm important details before making bookings or changes.",
    ],
    model=OpenAIChat(id="gpt-4"),
    tools=[CalComTools(user_timezone="America/New_York")],
    show_tool_calls=True,
    markdown=True,
)

agent.print_response("What are my bookings for tomorrow?")
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API keys">
    ```bash
    export CALCOM_API_KEY=xxx
    export CALCOM_EVENT_TYPE_ID=xxx
    export OPENAI_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U requests pytz openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/tools/calcom_tools.py
      ```

      ```bash Windows
      python cookbook/tools/calcom_tools.py
      ```
    </CodeGroup>
  </Step>
</Steps>


