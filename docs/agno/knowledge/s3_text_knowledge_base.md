---
title: S3 Text Knowledge Base
category: knowledge
source_lines: 62287-62348
line_count: 61
---

# S3 Text Knowledge Base
Source: https://docs.agno.com/knowledge/s3_text

Learn how to use text files from an S3 bucket in your knowledge base.

The **S3TextKnowledgeBase** reads **text** files from an S3 bucket, converts them into vector embeddings and loads them to a vector database.

## Usage

<Note>
  We are using a local PgVector database for this example. [Make sure it's running](https://docs.agno.com/vectordb/pgvector)
</Note>

```shell
pip install textract
```

```python
from agno.knowledge.s3.text import S3TextKnowledgeBase
from agno.vectordb.pgvector import PgVector

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

knowledge_base = S3TextKnowledgeBase(
    bucket_name="agno-public",
    key="recipes/recipes.docx",
    vector_db=PgVector(table_name="recipes", db_url=db_url),
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

agent.print_response("How to make Hummus?")
```

## Params

| Parameter     | Type           | Default             | Description                                                                               |
| ------------- | -------------- | ------------------- | ----------------------------------------------------------------------------------------- |
| `bucket_name` | `str`          | `None`              | The name of the S3 Bucket where the files are.                                            |
| `key`         | `str`          | `None`              | The key of the file in the bucket.                                                        |
| `formats`     | `List[str]`    | `[".doc", ".docx"]` | Formats accepted by this knowledge base.                                                  |
| `reader`      | `S3TextReader` | `S3TextReader()`    | A `S3TextReader` that converts the `Text` files into `Documents` for the vector database. |

`S3TextKnowledgeBase` is a subclass of the [AgentKnowledge](/reference/knowledge/base) class and has access to the same params.

## Developer Resources

* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/s3_text_kb.py)


