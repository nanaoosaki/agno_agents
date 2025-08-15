---
title: PDF Bytes Knowledge Base
category: knowledge
source_lines: 62070-62130
line_count: 60
---

# PDF Bytes Knowledge Base
Source: https://docs.agno.com/knowledge/pdf-bytes

Learn how to use in-memory PDF bytes in your knowledge base.

The **PDFBytesKnowledgeBase** reads **PDF content from bytes or IO streams**, converts them into vector embeddings and loads them to a vector database. This is useful when working with dynamically generated PDFs, API responses, or file uploads without needing to save files to disk.

## Usage

<Note>
  We are using a local LanceDB database for this example. [Make sure it's running](https://docs.agno.com/vectordb/lancedb)
</Note>

```shell
pip install pypdf
```

```python knowledge_base.py
from agno.agent import Agent
from agno.knowledge.pdf import PDFBytesKnowledgeBase
from agno.vectordb.lancedb import LanceDb

vector_db = LanceDb(
    table_name="recipes_async",
    uri="tmp/lancedb",
)

with open("data/pdfs/ThaiRecipes.pdf", "rb") as f:
    pdf_bytes = f.read()

knowledge_base = PDFBytesKnowledgeBase(
    pdfs=[pdf_bytes],
    vector_db=vector_db,
)
knowledge_base.load(recreate=False)  # Comment out after first run

agent = Agent(
    knowledge=knowledge_base,
    search_knowledge=True,
)

agent.print_response("How to make Tom Kha Gai?", markdown=True)
```

## Params

| Parameter      | Type                              | Default     | Description                                                                                  |
| -------------- | --------------------------------- | ----------- | -------------------------------------------------------------------------------------------- |
| pdfs           | Union\[List\[bytes], List\[IO]]   | -           | List of PDF content as bytes or IO streams.                                                  |
| exclude\_files | List\[str]                        | \[]         | List of file patterns to exclude (inherited from base class).                                |
| reader         | Union\[PDFReader, PDFImageReader] | PDFReader() | A PDFReader or PDFImageReader that converts the PDFs into Documents for the vector database. |

`PDFBytesKnowledgeBase` is a subclass of the [AgentKnowledge](/reference/knowledge/base) class and has access to the same params.

## Developer Resources

* View [Sync loading Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/pdf_bytes_kb.py)
* View [Async loading Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/pdf_bytes_kb_async.py)


