---
title: Fireworks Embedder
category: misc
source_lines: 11842-11858
line_count: 16
---

# Fireworks Embedder
Source: https://docs.agno.com/examples/concepts/embedders/fireworks-embedder



## Code

```python
from agno.agent import AgentKnowledge
from agno.embedder.fireworks import FireworksEmbedder
from agno.vectordb.pgvector import PgVector

embeddings = FireworksEmbedder().get_embedding(
    "The quick brown fox jumps over the lazy dog."
)

