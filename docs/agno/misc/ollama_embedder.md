---
title: Ollama Embedder
category: misc
source_lines: 12222-12238
line_count: 16
---

# Ollama Embedder
Source: https://docs.agno.com/examples/concepts/embedders/ollama-embedder



## Code

```python
from agno.agent import AgentKnowledge
from agno.embedder.ollama import OllamaEmbedder
from agno.vectordb.pgvector import PgVector

embeddings = OllamaEmbedder().get_embedding(
    "The quick brown fox jumps over the lazy dog."
)

