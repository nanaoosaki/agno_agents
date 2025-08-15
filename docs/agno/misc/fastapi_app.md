---
title: FastAPI App
category: misc
source_lines: 3273-3299
line_count: 26
---

# FastAPI App
Source: https://docs.agno.com/applications/fastapi/introduction

Host agents as FastAPI Applications.

The FastAPI App is used to serve Agents or Teams using a FastAPI server with a rest api interface.

### Example Usage

Create an agent, wrap it with `FastAPIApp`, and serve it:

```python
from agno.agent import Agent
from agno.app.fastapi.app import FastAPIApp
from agno.models.openai import OpenAIChat

basic_agent = Agent(
    name="Basic Agent",
    agent_id="basic_agent",
    model=OpenAIChat(id="gpt-4o"), # Ensure OPENAI_API_KEY is set
    add_history_to_messages=True,
    num_history_responses=3,
    add_datetime_to_instructions=True,
    markdown=True,
)

