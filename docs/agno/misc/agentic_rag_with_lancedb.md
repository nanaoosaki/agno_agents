---
title: Agentic RAG with LanceDB
category: misc
source_lines: 21102-21116
line_count: 14
---

# Agentic RAG with LanceDB
Source: https://docs.agno.com/examples/concepts/rag/agentic-rag-lancedb



## Code

```python
from agno.agent import Agent
from agno.embedder.openai import OpenAIEmbedder
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.models.openai import OpenAIChat
from agno.vectordb.lancedb import LanceDb, SearchType

