---
title: MongoDB Hybrid Search
category: misc
source_lines: 12597-12612
line_count: 15
---

# MongoDB Hybrid Search
Source: https://docs.agno.com/examples/concepts/hybrid-search/mongodb



## Code

```python cookbook/agent_concepts/knowledge/vector_dbs/mongo_db/mongo_db_hybrid_search.py
import typer
from agno.agent import Agent
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.mongodb import MongoDb
from agno.vectordb.search import SearchType
from rich.prompt import Prompt

