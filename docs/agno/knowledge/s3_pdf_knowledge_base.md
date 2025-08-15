---
title: S3 PDF Knowledge Base
category: knowledge
source_lines: 62231-62287
line_count: 56
---

# S3 PDF Knowledge Base
Source: https://docs.agno.com/knowledge/s3_pdf

Learn how to use PDFs from an S3 bucket in your knowledge base.

The **S3PDFKnowledgeBase** reads **PDF** files from an S3 bucket, converts them into vector embeddings and loads them to a vector database.

## Usage

<Note>
  We are using a local PgVector database for this example. [Make sure it's running](https://docs.agno.com/vectordb/pgvector)
</Note>

```python
from agno.knowledge.s3.pdf import S3PDFKnowledgeBase
from agno.vectordb.pgvector import PgVector

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

knowledge_base = S3PDFKnowledgeBase(
    bucket_name="agno-public",
    key="recipes/ThaiRecipes.pdf",
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

agent.print_response("How to make Thai curry?")
```

## Params

| Parameter     | Type          | Default         | Description                                                                        |
| ------------- | ------------- | --------------- | ---------------------------------------------------------------------------------- |
| `bucket_name` | `str`         | `None`          | The name of the S3 Bucket where the PDFs are.                                      |
| `key`         | `str`         | `None`          | The key of the PDF file in the bucket.                                             |
| `reader`      | `S3PDFReader` | `S3PDFReader()` | A `S3PDFReader` that converts the `PDFs` into `Documents` for the vector database. |

`S3PDFKnowledgeBase` is a subclass of the [AgentKnowledge](/reference/knowledge/base) class and has access to the same params.

## Developer Resources

* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/s3_pdf_kb.py)


