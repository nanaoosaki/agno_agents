---
title: You can also override the entire `system_message` for the memory manager
category: knowledge
source_lines: 17365-17373
line_count: 8
---

# You can also override the entire `system_message` for the memory manager
memory_manager = MemoryManager(
    model=OpenRouter(id="meta-llama/llama-3.3-70b-instruct"),
    additional_instructions="""
    IMPORTANT: Don't store any memories about the user's name. Just say "The User" instead of referencing the user's name.
    """,
)

