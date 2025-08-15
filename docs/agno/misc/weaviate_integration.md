---
title: Weaviate Integration
category: misc
source_lines: 33325-33345
line_count: 20
---

# Weaviate Integration
Source: https://docs.agno.com/examples/concepts/vectordb/weaviate



## Code

```python cookbook/agent_concepts/vector_dbs/weaviate_db.py
from agno.agent import Agent
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.search import SearchType
from agno.vectordb.weaviate import Distance, VectorIndex, Weaviate

vector_db = Weaviate(
    collection="recipes",
    search_type=SearchType.hybrid,
    vector_index=VectorIndex.HNSW,
    distance=Distance.COSINE,
    local=True,  # Set to False if using Weaviate Cloud and True if using local instance
)
