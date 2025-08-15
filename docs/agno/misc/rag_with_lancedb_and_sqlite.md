---
title: RAG with LanceDB and SQLite
category: misc
source_lines: 21339-21354
line_count: 15
---

# RAG with LanceDB and SQLite
Source: https://docs.agno.com/examples/concepts/rag/rag-with-lance-db-and-sqlite



## Code

```python
from agno.agent import Agent
from agno.embedder.ollama import OllamaEmbedder
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.models.ollama import Ollama
from agno.storage.sqlite import SqliteStorage
from agno.vectordb.lancedb import LanceDb

