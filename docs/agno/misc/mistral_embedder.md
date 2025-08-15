---
title: Mistral Embedder
category: misc
source_lines: 12146-12162
line_count: 16
---

# Mistral Embedder
Source: https://docs.agno.com/examples/concepts/embedders/mistral-embedder



## Code

```python
from agno.agent import AgentKnowledge
from agno.embedder.mistral import MistralEmbedder
from agno.vectordb.pgvector import PgVector

embeddings = MistralEmbedder().get_embedding(
    "The quick brown fox jumps over the lazy dog."
)

