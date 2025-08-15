---
title: Azure OpenAI Embedder
category: misc
source_lines: 11689-11705
line_count: 16
---

# Azure OpenAI Embedder
Source: https://docs.agno.com/examples/concepts/embedders/azure-embedder



## Code

```python
from agno.agent import AgentKnowledge
from agno.embedder.azure_openai import AzureOpenAIEmbedder
from agno.vectordb.pgvector import PgVector

embeddings = AzureOpenAIEmbedder().get_embedding(
    "The quick brown fox jumps over the lazy dog."
)

