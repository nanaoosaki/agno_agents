---
title: Mem0 Memory Tools
category: knowledge
source_lines: 26141-26213
line_count: 72
---

# Mem0 Memory Tools
Source: https://docs.agno.com/examples/concepts/tools/database/mem0



## Code

```python cookbook/tools/mem0_tools.py
from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.mem0 import Mem0Tools

USER_ID = "jane_doe"
SESSION_ID = "agno_session"

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[Mem0Tools()],
    user_id=USER_ID,
    session_id=SESSION_ID,
    add_state_in_messages=True,
    markdown=True,
    instructions=dedent(
        """
        You have an evolving memory of this user. Proactively capture new personal details,
        preferences, plans, and relevant context the user shares, and naturally bring them up
        in later conversation. Before answering questions about past details, recall from your memory
        to provide precise and personalized responses. Keep your memory concise: store only
        meaningful information that enhances long-term dialogue. If the user asks to start fresh,
        clear all remembered information and proceed anew.
        """
    ),
    show_tool_calls=True,
)

agent.print_response("I live in NYC")
agent.print_response("I lived in San Francisco for 5 years previously")
agent.print_response("I'm going to a Taylor Swift concert tomorrow")

agent.print_response("Summarize all the details of the conversation")
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API keys">
    ```bash
    export OPENAI_API_KEY=xxx
    export MEM0_API_KEY=xxx
    export MEM0_ORG_ID=xxx        # Optional
    export MEM0_PROJECT_ID=xxx    # Optional
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U mem0ai openai agno
    ```
  </Step>

  <Step title="Run Agent">
    ```bash
    python cookbook/tools/mem0_tools.py
    ```
  </Step>
</Steps>


