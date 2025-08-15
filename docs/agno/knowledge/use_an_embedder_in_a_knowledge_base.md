---
title: Use an embedder in a knowledge base
category: knowledge
source_lines: 58887-58901
line_count: 14
---

# Use an embedder in a knowledge base
knowledge_base = AgentKnowledge(
    vector_db=PgVector(
        db_url="postgresql+psycopg://ai:ai@localhost:5532/ai",
        table_name="gemini_embeddings",
        embedder=GeminiEmbedder(),
    ),
    num_documents=2,
)
```

For more details on configuring different model providers, check our [Embeddings documentation](../embedder/)


