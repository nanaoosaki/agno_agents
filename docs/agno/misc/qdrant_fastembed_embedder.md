---
title: Qdrant FastEmbed Embedder
category: misc
source_lines: 12372-12388
line_count: 16
---

# Qdrant FastEmbed Embedder
Source: https://docs.agno.com/examples/concepts/embedders/qdrant-fastembed



## Code

```python
from agno.agent import AgentKnowledge
from agno.embedder.fastembed import FastEmbedEmbedder
from agno.vectordb.pgvector import PgVector

embeddings = FastEmbedEmbedder().get_embedding(
    "The quick brown fox jumps over the lazy dog."
)

