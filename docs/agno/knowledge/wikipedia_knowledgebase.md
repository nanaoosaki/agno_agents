---
title: Wikipedia KnowledgeBase
category: knowledge
source_lines: 62702-62762
line_count: 60
---

# Wikipedia KnowledgeBase
Source: https://docs.agno.com/knowledge/wikipedia

Learn how to use Wikipedia topics in your knowledge base.

The **WikipediaKnowledgeBase** reads wikipedia topics, converts them into vector embeddings and loads them to a vector database.

## Usage

<Note>
  We are using a local PgVector database for this example. [Make sure it's running](http://localhost:3333/vectordb/pgvector)
</Note>

```shell
pip install wikipedia
```

```python knowledge_base.py
from agno.knowledge.wikipedia import WikipediaKnowledgeBase
from agno.vectordb.pgvector import PgVector

knowledge_base = WikipediaKnowledgeBase(
    topics=["Manchester United", "Real Madrid"],
    # Table name: ai.wikipedia_documents
    vector_db=PgVector(
        table_name="wikipedia_documents",
        db_url="postgresql+psycopg://ai:ai@localhost:5532/ai",
    ),
)
```

Then use the `knowledge_base` with an Agent:

```python agent.py
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

| Parameter | Type        | Default | Description    |
| --------- | ----------- | ------- | -------------- |
| `topics`  | `List[str]` | \[]     | Topics to read |

`WikipediaKnowledgeBase` is a subclass of the [AgentKnowledge](/reference/knowledge/base) class and has access to the same params.

## Developer Resources

* View [Sync loading Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/wikipedia_kb.py)
* View [Async loading Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/wikipedia_kb_async.py)


