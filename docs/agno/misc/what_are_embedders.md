---
title: What are Embedders?
category: misc
source_lines: 5858-5870
line_count: 12
---

# What are Embedders?
Source: https://docs.agno.com/embedder/introduction

Learn how to use embedders with Agno to convert complex information into vector representations.

An Embedder converts complex information into vector representations, allowing it to be stored in a vector database. By transforming data into embeddings, the embedder enables efficient searching and retrieval of contextually relevant information. This process enhances the responses of language models by providing them with the necessary business context, ensuring they are context-aware. Agno uses the `OpenAIEmbedder` as the default embedder, but other embedders are supported as well. Here is an example:

```python
from agno.agent import Agent, AgentKnowledge
from agno.vectordb.pgvector import PgVector
from agno.embedder.openai import OpenAIEmbedder

