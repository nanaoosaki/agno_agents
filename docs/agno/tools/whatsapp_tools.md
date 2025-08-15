---
title: WhatsApp Tools
category: tools
source_lines: 30873-30891
line_count: 18
---

# WhatsApp Tools
Source: https://docs.agno.com/examples/concepts/tools/social/whatsapp



## Code

```python cookbook/tools/whatsapp_tools.py
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.whatsapp import WhatsAppTools

agent = Agent(
    name="whatsapp",
    model=Gemini(id="gemini-2.0-flash"),
    tools=[WhatsAppTools()],
)

