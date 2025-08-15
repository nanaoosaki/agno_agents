---
title: Sets the session state for the session with the id "user_2_session_1"
category: misc
source_lines: 2057-2060
line_count: 3
---

# Sets the session state for the session with the id "user_2_session_1"
agent.print_response("What is my name?", session_id="user_2_session_1", user_id="user_2", session_state={"user_name": "Jane", "age": 25})

