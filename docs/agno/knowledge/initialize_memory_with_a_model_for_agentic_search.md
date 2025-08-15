---
title: Initialize memory with a model for agentic search
category: knowledge
source_lines: 63207-63223
line_count: 16
---

# Initialize memory with a model for agentic search
memory = Memory(model=Gemini(id="gemini-2.0-flash-exp"))

john_doe_id = "john_doe@example.com"

memory.add_user_memory(
    memory=UserMemory(memory="The user enjoys hiking in the mountains on weekends"),
    user_id=john_doe_id,
)
memory.add_user_memory(
    memory=UserMemory(
        memory="The user enjoys reading science fiction novels before bed"
    ),
    user_id=john_doe_id,
)

