---
title: Markdown Knowledge Base
category: knowledge
source_lines: 61868-61929
line_count: 61
---

# Markdown Knowledge Base
Source: https://docs.agno.com/knowledge/markdown

Learn how to use Markdown files in your knowledge base.

The **MarkdownKnowledgeBase** reads **local markdown** files, converts them into vector embeddings and loads them to a vector database.

## Usage

<Note>
  We are using a local PgVector database for this example. [Make sure it's running](https://docs.agno.com/vectordb/pgvector)
</Note>

```python knowledge_base.py
from agno.knowledge.markdown import MarkdownKnowledgeBase
from agno.vectordb.pgvector import PgVector

knowledge_base = MarkdownKnowledgeBase(
    path="data/markdown_files",
    vector_db=PgVector(
        table_name="markdown_documents",
        db_url="postgresql+psycopg://ai:ai@localhost:5532/ai",
    ),
)
```

Then use the `knowledge_base` with an Agent:

```python agent.py
from agno.agent import Agent
from knowledge_base import knowledge_base

agent = Agent(
    knowledge_base=knowledge_base,
    search_knowledge=True,
)
agent.knowledge.load(recreate=False)

agent.print_response("Ask me about something from the knowledge base")
```

#### MarkdownKnowledgeBase also supports async loading.

```shell
pip install qdrant-client
```

We are using a local Qdrant database for this example. [Make sure it's running](https://docs.agno.com/vectordb/qdrant)

```python async_knowledge_base.py
import asyncio
from pathlib import Path

from agno.agent import Agent
from agno.knowledge.markdown import MarkdownKnowledgeBase
from agno.vectordb.qdrant import Qdrant

COLLECTION_NAME = "essay-txt"

vector_db = Qdrant(collection=COLLECTION_NAME, url="http://localhost:6333")

