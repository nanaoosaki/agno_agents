---
title: Document Knowledge Base
category: knowledge
source_lines: 61168-61228
line_count: 60
---

# Document Knowledge Base
Source: https://docs.agno.com/knowledge/document

Learn how to use local documents in your knowledge base.

The **DocumentKnowledgeBase** reads **local docs** files, converts them into vector embeddings and loads them to a vector database.

## Usage

<Note>
  We are using a local PgVector database for this example. [Make sure it's running](https://docs.agno.com/vectordb/pgvector)
</Note>

```shell
pip install textract
```

```python
from agno.knowledge.document import DocumentKnowledgeBase
from agno.vectordb.pgvector import PgVector

knowledge_base = DocumentKnowledgeBase(
    path="data/docs",
    # Table name: ai.documents
    vector_db=PgVector(
        table_name="documents",
        db_url="postgresql+psycopg://ai:ai@localhost:5532/ai",
    ),
)
```

Then use the `knowledge_base` with an `Agent`:

```python
from agno.agent import Agent
from knowledge_base import knowledge_base

agent = Agent(
    knowledge=knowledge_base,
    search_knowledge=True,
)
agent.knowledge.load(recreate=False)

agent.print_response("Ask me about something from the knowledge base")
```

## Params

| Parameter   | Type             | Default | Description                                               |
| ----------- | ---------------- | ------- | --------------------------------------------------------- |
| `documents` | `List[Document]` | -       | List of Document objects to be used as the knowledge base |

`DocumentKnowledgeBase` is a subclass of the [AgentKnowledge](/reference/knowledge/base) class and has access to the same params.

## Developer Resources

* View [Sync loading Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/doc_kb.py)
* View [Async loading Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/doc_kb_async.py)


