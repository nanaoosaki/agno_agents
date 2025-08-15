---
title: Example usage with a PDF knowledge base
category: knowledge
source_lines: 5547-5562
line_count: 15
---

# Example usage with a PDF knowledge base
knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    reader=PDFUrlReader(
        chunk_size=2048
    ),  # Required because Cohere model has a fixed size of 2048
    vector_db=PgVector(
        table_name="recipes",
        db_url="postgresql+psycopg://ai:ai@localhost:5532/ai",
        embedder=AwsBedrockEmbedder(),
    ),
)
knowledge_base.load(recreate=False)
```

