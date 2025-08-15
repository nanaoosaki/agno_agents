---
title: Jina Embedder
category: misc
source_lines: 12070-12086
line_count: 16
---

# Jina Embedder
Source: https://docs.agno.com/examples/concepts/embedders/jina-embedder



## Code

```python
from agno.agent import AgentKnowledge
from agno.embedder.jina import JinaEmbedder
from agno.vectordb.pgvector import PgVector

embeddings = JinaEmbedder().get_embedding(
    "The quick brown fox jumps over the lazy dog."
)

