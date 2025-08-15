---
title: Reset for this example
category: misc
source_lines: 17845-17861
line_count: 16
---

# Reset for this example
memory_db.clear()

memory = Memory(db=memory_db)

user_id = "john_doe@example.com"
session_id = "session_summaries"

agent = Agent(
    model=Gemini(id="gemini-2.0-flash-exp"),
    memory=memory,
    storage=PostgresStorage(table_name="agent_sessions", db_url=db_url),
    enable_session_summaries=True,
    session_id=session_id,
)

