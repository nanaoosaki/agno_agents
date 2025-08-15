---
title: Create a knowledge base with the loaded documents
category: knowledge
source_lines: 13294-13303
line_count: 9
---

# Create a knowledge base with the loaded documents
knowledge_base = DocumentKnowledgeBase(
    documents=documents,
    vector_db=PgVector(
        table_name="documents",
        db_url=db_url,
    ),
)

