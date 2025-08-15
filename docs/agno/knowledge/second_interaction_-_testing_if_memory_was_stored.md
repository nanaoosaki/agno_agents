---
title: Second interaction - testing if memory was stored
category: knowledge
source_lines: 18237-18245
line_count: 8
---

# Second interaction - testing if memory was stored
agent.print_response(
    "What are my hobbies?", 
    stream=True, 
    user_id=user_id, 
    session_id=session_id
)

