---
title: Create a knowledge base with the DOCX files from the data/docs directory
category: knowledge
source_lines: 61290-61300
line_count: 10
---

# Create a knowledge base with the DOCX files from the data/docs directory
knowledge_base = DocxKnowledgeBase(
    path=Path("tmp/docs"),
    vector_db=LanceDb(
        uri="tmp/lancedb",
        table_name="docx_reader",
        search_type=SearchType.hybrid,
    ),
)

