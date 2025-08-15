---
title: Cohere Embedder
category: misc
source_lines: 11767-11782
line_count: 15
---

# Cohere Embedder
Source: https://docs.agno.com/examples/concepts/embedders/cohere-embedder



## Code

```python
from agno.agent import AgentKnowledge
from agno.embedder.cohere import CohereEmbedder
from agno.vectordb.pgvector import PgVector

embeddings = CohereEmbedder().get_embedding(
    "The quick brown fox jumps over the lazy dog."
)
