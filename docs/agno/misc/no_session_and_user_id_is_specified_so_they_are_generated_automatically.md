---
title: No session and user ID is specified, so they are generated automatically
category: misc
source_lines: 17160-17186
line_count: 26
---

# No session and user ID is specified, so they are generated automatically
agent = Agent(
    model=Claude(id="claude-3-5-sonnet-20241022"),
    memory=memory,
    enable_user_memories=True,
    enable_session_summaries=True,
)

agent.print_response(
    "My name is John Doe and I like to hike in the mountains on weekends.",
    stream=True,
)

agent.print_response(
    "What are my hobbies?",
    stream=True,
)


memories = memory.get_user_memories()
print("John Doe's memories:")
pprint(memories)
session_summary = agent.get_session_summary()
pprint(session_summary)


