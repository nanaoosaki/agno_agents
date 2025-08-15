---
title: Youtube KnowledgeBase
category: knowledge
source_lines: 62762-62869
line_count: 107
---

# Youtube KnowledgeBase
Source: https://docs.agno.com/knowledge/youtube

Learn how to use YouTube video transcripts in your knowledge base.

The **YouTubeKnowledgeBase** iterates over a list of YouTube URLs, extracts the video transcripts, converts them into vector embeddings and loads them to a vector database.

## Usage

<Note>
  We are using a local PgVector database for this example. [Make sure it's running](http://localhost:3333/vectordb/pgvector)
</Note>

```shell
pip install bs4
```

```python knowledge_base.py
from agno.knowledge.youtube import YouTubeKnowledgeBase
from agno.vectordb.pgvector import PgVector

knowledge_base = YouTubeKnowledgeBase(
    urls=["https://www.youtube.com/watch?v=CDC3GOuJyZ0"],
    # Table name: ai.website_documents
    vector_db=PgVector(
        table_name="youtube_documents",
        db_url="postgresql+psycopg://ai:ai@localhost:5532/ai",
    ),
)
```

Then use the `knowledge_base` with an `Agent`:

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

#### YouTubeKnowledgeBase also supports async loading.

```shell
pip install qdrant-client
```

We are using a local Qdrant database for this example. [Make sure it's running](https://docs.agno.com/vectordb/qdrant)

```python async_knowledge_base.py
import asyncio

from agno.agent import Agent
from agno.knowledge.youtube import YouTubeKnowledgeBase, YouTubeReader
from agno.vectordb.qdrant import Qdrant

COLLECTION_NAME = "youtube-reader"

vector_db = Qdrant(collection=COLLECTION_NAME, url="http://localhost:6333")

knowledge_base = YouTubeKnowledgeBase(
    urls=[
        "https://www.youtube.com/watch?v=CDC3GOuJyZ0",
        "https://www.youtube.com/watch?v=JbF_8g1EXj4",
    ],
    vector_db=vector_db,
    reader=YouTubeReader(chunk=True),
)

agent = Agent(
    knowledge=knowledge_base,
    search_knowledge=True,
)

if __name__ == "__main__":
    # Comment out after first run
    asyncio.run(knowledge_base.aload(recreate=False))

    # Create and use the agent
    asyncio.run(
        agent.aprint_response(
            "What is the major focus of the knowledge provided in both the videos, explain briefly.",
            markdown=True,
        )
    )
```

## Params

| Parameter | Type                      | Default | Description                                                                                                                    |
| --------- | ------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------ |
| `urls`    | `List[str]`               | `[]`    | URLs of the videos to read                                                                                                     |
| `reader`  | `Optional[YouTubeReader]` | `None`  | A `YouTubeReader` that reads transcripts of the videos at the urls and converts them into `Documents` for the vector database. |

`YouTubeKnowledgeBase` is a subclass of the [AgentKnowledge](/reference/knowledge/base) class and has access to the same params.

## Developer Resources

* View [Sync loading Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/youtube_kb.py)
* View [Async loading Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/youtube_kb_async.py)


