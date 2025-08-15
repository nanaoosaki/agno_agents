---
title: Knowledge base setup (same as synchronous example)
category: knowledge
source_lines: 61097-61104
line_count: 7
---

# Knowledge base setup (same as synchronous example)
embedder = OpenAIEmbedder(id="text-embedding-3-small")
vector_db = Qdrant(collection="thai-recipes", url="http://localhost:6333", embedder=embedder)
knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=vector_db,
)
