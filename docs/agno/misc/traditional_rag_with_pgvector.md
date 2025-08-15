---
title: Traditional RAG with PgVector
category: misc
source_lines: 21504-21519
line_count: 15
---

# Traditional RAG with PgVector
Source: https://docs.agno.com/examples/concepts/rag/traditional-rag-pgvector



## Code

```python
from agno.agent import Agent
from agno.embedder.openai import OpenAIEmbedder
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.models.openai import OpenAIChat
from agno.vectordb.pgvector import PgVector, SearchType

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
