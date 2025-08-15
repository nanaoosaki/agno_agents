---
title: PgVector Hybrid Search
category: misc
source_lines: 12684-12704
line_count: 20
---

# PgVector Hybrid Search
Source: https://docs.agno.com/examples/concepts/hybrid-search/pgvector



## Code

```python
from agno.agent import Agent
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.models.openai import OpenAIChat
from agno.vectordb.pgvector import PgVector, SearchType

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=PgVector(
        table_name="recipes", db_url=db_url, search_type=SearchType.hybrid
    ),
)
