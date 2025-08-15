---
title: SentenceTransformers Embedder
category: misc
source_lines: 6195-6209
line_count: 14
---

# SentenceTransformers Embedder
Source: https://docs.agno.com/embedder/sentencetransformers



The `SentenceTransformerEmbedder` class is used to embed text data into vectors using the [SentenceTransformers](https://www.sbert.net/) library.

## Usage

```python cookbook/embedders/sentence_transformer_embedder.py
from agno.agent import AgentKnowledge
from agno.vectordb.pgvector import PgVector
from agno.embedder.sentence_transformer import SentenceTransformerEmbedder

