---
title: Agentic RAG with PgVector
category: misc
source_lines: 21175-21190
line_count: 15
---

# Agentic RAG with PgVector
Source: https://docs.agno.com/examples/concepts/rag/agentic-rag-pgvector



## Code

```python
from agno.agent import Agent
from agno.embedder.openai import OpenAIEmbedder
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.models.openai import OpenAIChat
from agno.vectordb.pgvector import PgVector, SearchType

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
