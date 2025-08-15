---
title: You can also override the entire `system_message` for the session summarizer
category: misc
source_lines: 17373-17387
line_count: 14
---

# You can also override the entire `system_message` for the session summarizer
session_summarizer = SessionSummarizer(
    model=Claude(id="claude-3-5-sonnet-20241022"),
    additional_instructions="""
    Make the summary very informal and conversational.
    """,
)

memory = Memory(
    db=memory_db,
    memory_manager=memory_manager,
    summarizer=session_summarizer,
)

