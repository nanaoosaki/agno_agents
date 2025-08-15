---
title: Now lets do a new session with a different user
category: misc
source_lines: 17186-17209
line_count: 23
---

# Now lets do a new session with a different user
session_id_2 = "1002"
mark_gonzales_id = "mark@example.com"

agent.print_response(
    "My name is Mark Gonzales and I like anime and video games.",
    stream=True,
    user_id=mark_gonzales_id,
    session_id=session_id_2,
)

agent.print_response(
    "What are my hobbies?",
    stream=True,
    user_id=mark_gonzales_id,
    session_id=session_id_2,
)


memories = memory.get_user_memories(user_id=mark_gonzales_id)
print("Mark Gonzales's memories:")
pprint(memories)

