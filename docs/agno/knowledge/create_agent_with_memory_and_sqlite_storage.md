---
title: Create agent with memory and SQLite storage
category: knowledge
source_lines: 18217-18229
line_count: 12
---

# Create agent with memory and SQLite storage
agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    memory=memory,
    storage=SqliteStorage(
        table_name="agent_sessions", 
        db_file="tmp/memory.db"
    ),
    enable_user_memories=True,
    enable_session_summaries=True,
)

