---
title: Agentic RAG with Reranking
category: misc
source_lines: 21263-21278
line_count: 15
---

# Agentic RAG with Reranking
Source: https://docs.agno.com/examples/concepts/rag/agentic-rag-with-reranking



## Code

```python
from agno.agent import Agent
from agno.embedder.openai import OpenAIEmbedder
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.models.openai import OpenAIChat
from agno.reranker.cohere import CohereReranker
from agno.vectordb.lancedb import LanceDb, SearchType

