---
title: Load PDF knowledge base using hybrid search
category: knowledge
source_lines: 61400-61406
line_count: 6
---

# Load PDF knowledge base using hybrid search
knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=hybrid_db,
)

