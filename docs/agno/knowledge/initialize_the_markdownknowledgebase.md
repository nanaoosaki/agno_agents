---
title: Initialize the MarkdownKnowledgeBase
category: knowledge
source_lines: 61929-61936
line_count: 7
---

# Initialize the MarkdownKnowledgeBase
knowledge_base = MarkdownKnowledgeBase(
    path=Path("tmp/mds"),
    vector_db=vector_db,
    num_documents=5,
)

