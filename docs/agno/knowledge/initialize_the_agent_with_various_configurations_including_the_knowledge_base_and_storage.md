---
title: Initialize the Agent with various configurations including the knowledge base and storage
category: knowledge
source_lines: 21383-21394
line_count: 11
---

# Initialize the Agent with various configurations including the knowledge base and storage
agent = Agent(
    session_id="session_id",  # use any unique identifier to identify the run
    user_id="user",  # user identifier to identify the user
    model=model,
    knowledge=knowledge_base,
    storage=storage,
    show_tool_calls=True,
    debug_mode=True,  # Enable debug mode for additional information
)

