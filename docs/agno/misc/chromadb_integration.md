---
title: ChromaDB Integration
category: misc
source_lines: 32646-32658
line_count: 12
---

# ChromaDB Integration
Source: https://docs.agno.com/examples/concepts/vectordb/chromadb



## Code

```python cookbook/agent_concepts/vector_dbs/chroma_db.py
from agno.agent import Agent
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.chroma import ChromaDb

