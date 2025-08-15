---
title: Create a knowledge base from a PDF URL using LanceDb for vector storage and OllamaEmbedder for embedding
category: knowledge
source_lines: 21370-21376
line_count: 6
---

# Create a knowledge base from a PDF URL using LanceDb for vector storage and OllamaEmbedder for embedding
knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=vector_db,
)

