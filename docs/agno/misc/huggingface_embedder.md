---
title: Huggingface Embedder
category: misc
source_lines: 11994-12010
line_count: 16
---

# Huggingface Embedder
Source: https://docs.agno.com/examples/concepts/embedders/huggingface-embedder



## Code

```python
from agno.agent import AgentKnowledge
from agno.embedder.huggingface import HuggingfaceCustomEmbedder
from agno.vectordb.pgvector import PgVector

embeddings = HuggingfaceCustomEmbedder().get_embedding(
    "The quick brown fox jumps over the lazy dog."
)

