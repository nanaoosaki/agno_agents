---
title: Whatsapp App
category: misc
source_lines: 3603-3631
line_count: 28
---

# Whatsapp App
Source: https://docs.agno.com/applications/whatsapp/introduction

Host agents as Whatsapp Applications.

The Whatsapp App is used to serve Agents or Teams interacting via WhatsApp, using a FastAPI server to handle webhook events and to send messages.

<Snippet file="setup-whatsapp-app.mdx" />

### Example Usage

Create an agent, wrap it with `WhatsappAPI`, and serve it:

```python
from agno.agent import Agent
from agno.app.whatsapp.app import WhatsappAPI
from agno.models.openai import OpenAIChat
from agno.tools.openai import OpenAITools

image_agent = Agent(
    model=OpenAIChat(id="gpt-4o"), # Ensure OPENAI_API_KEY is set
    tools=[OpenAITools(image_model="gpt-image-1")],
    markdown=True,
    show_tool_calls=True,
    debug_mode=True,
    add_history_to_messages=True,
)

