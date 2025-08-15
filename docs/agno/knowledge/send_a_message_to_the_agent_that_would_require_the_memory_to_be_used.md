---
title: Send a message to the agent that would require the memory to be used
category: knowledge
source_lines: 63000-63007
line_count: 7
---

# Send a message to the agent that would require the memory to be used
agent.print_response(
    "My name is John Doe and I like to hike in the mountains on weekends.",
    stream=True,
    user_id=john_doe_id,
)

