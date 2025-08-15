---
title: Initialize the TextKnowledgeBase
category: knowledge
source_lines: 62555-62562
line_count: 7
---

# Initialize the TextKnowledgeBase
knowledge_base = TextKnowledgeBase(
    path=Path("tmp/docs"),
    vector_db=vector_db,
    num_documents=5,
)

