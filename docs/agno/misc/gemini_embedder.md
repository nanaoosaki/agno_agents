---
title: Gemini Embedder
category: misc
source_lines: 11918-11934
line_count: 16
---

# Gemini Embedder
Source: https://docs.agno.com/examples/concepts/embedders/gemini-embedder



## Code

```python
from agno.agent import AgentKnowledge
from agno.embedder.google import GeminiEmbedder
from agno.vectordb.pgvector import PgVector

embeddings = GeminiEmbedder().get_embedding(
    "The quick brown fox jumps over the lazy dog."
)

