---
title: Voyage AI Embedder
category: misc
source_lines: 6286-6300
line_count: 14
---

# Voyage AI Embedder
Source: https://docs.agno.com/embedder/voyageai



The `VoyageAIEmbedder` class is used to embed text data into vectors using the Voyage AI API. Get your key from [here](https://dash.voyageai.com/api-keys).

## Usage

```python cookbook/embedders/voyageai_embedder.py
from agno.agent import AgentKnowledge
from agno.vectordb.pgvector import PgVector
from agno.embedder.voyageai import VoyageAIEmbedder

