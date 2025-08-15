---
title: OpenAI Embedder
category: misc
source_lines: 12296-12312
line_count: 16
---

# OpenAI Embedder
Source: https://docs.agno.com/examples/concepts/embedders/openai-embedder



## Code

```python
from agno.agent import AgentKnowledge
from agno.embedder.openai import OpenAIEmbedder
from agno.vectordb.pgvector import PgVector

embeddings = OpenAIEmbedder().get_embedding(
    "The quick brown fox jumps over the lazy dog."
)

