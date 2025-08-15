---
title: Initialize the DocxKnowledgeBase
category: knowledge
source_lines: 13738-13750
line_count: 12
---

# Initialize the DocxKnowledgeBase
knowledge_base = DocxKnowledgeBase(
    vector_db=vector_db,
    num_documents=5,
)

knowledge_base.load_document(
    path=downloaded_cv_paths[0],
    metadata={"user_id": "jordan_mitchell", "document_type": "cv", "year": 2025},
    recreate=True,  # Set to True only for the first run, then set to False
)

