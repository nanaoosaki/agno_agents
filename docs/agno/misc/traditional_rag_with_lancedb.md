---
title: Traditional RAG with LanceDB
category: misc
source_lines: 21430-21444
line_count: 14
---

# Traditional RAG with LanceDB
Source: https://docs.agno.com/examples/concepts/rag/traditional-rag-lancedb



## Code

```python
from agno.agent import Agent
from agno.embedder.openai import OpenAIEmbedder
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.models.openai import OpenAIChat
from agno.vectordb.lancedb import LanceDb, SearchType

