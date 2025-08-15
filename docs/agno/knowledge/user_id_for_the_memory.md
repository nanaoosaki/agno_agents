---
title: User ID for the memory
category: knowledge
source_lines: 62991-63000
line_count: 9
---

# User ID for the memory
john_doe_id = "john_doe@example.com"
agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    memory=memory,
    # This will trigger the MemoryManager after each user message
    enable_user_memories=True,
)

