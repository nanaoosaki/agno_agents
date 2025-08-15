---
title: Create agent with Redis storage
category: misc
source_lines: 69113-69124
line_count: 11
---

# Create agent with Redis storage
agent = Agent(
    storage=storage,
    tools=[DuckDuckGoTools()],
    add_history_to_messages=True,
)

agent.print_response("How many people live in Canada?")

agent.print_response("What is their national anthem called?")

