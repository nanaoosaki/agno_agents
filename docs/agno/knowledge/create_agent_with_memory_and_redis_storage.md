---
title: Create agent with memory and Redis storage
category: knowledge
source_lines: 18114-18123
line_count: 9
---

# Create agent with memory and Redis storage
agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    memory=memory,
    storage=RedisStorage(prefix="agno_test", host="localhost", port=6379),
    enable_user_memories=True,
    enable_session_summaries=True,
)

