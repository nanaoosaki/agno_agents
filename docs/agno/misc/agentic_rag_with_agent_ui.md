---
title: Agentic RAG with Agent UI
category: misc
source_lines: 20997-21014
line_count: 17
---

# Agentic RAG with Agent UI
Source: https://docs.agno.com/examples/concepts/rag/agentic-rag-agent-ui



## Code

```python
from agno.agent import Agent
from agno.embedder.openai import OpenAIEmbedder
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.models.openai import OpenAIChat
from agno.playground import Playground
from agno.storage.postgres import PostgresStorage
from agno.vectordb.pgvector import PgVector, SearchType

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
