---
title: Create a knowledge base with the PDFs from the data/pdfs directory
category: knowledge
source_lines: 62195-62202
line_count: 7
---

# Create a knowledge base with the PDFs from the data/pdfs directory
knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=vector_db,
    reader=PDFUrlReader(chunk=True),
)

