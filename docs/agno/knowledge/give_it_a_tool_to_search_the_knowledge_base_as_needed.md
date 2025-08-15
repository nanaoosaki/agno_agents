---
title: give it a tool to search the knowledge base as needed
category: knowledge
source_lines: 61448-61509
line_count: 61
---

# give it a tool to search the knowledge base as needed
agent = Agent(knowledge=knowledge_base, search_knowledge=True)
```

We can give our agent access to the knowledge base in the following ways:

* We can set `search_knowledge=True` to add a `search_knowledge_base()` tool to the Agent. `search_knowledge` is `True` **by default** if you add `knowledge` to an Agent.
* We can set `add_references=True` to automatically add references from the knowledge base to the Agent's prompt. This is the traditional 2023 RAG approach.

<Tip>
  If you need complete control over the knowledge base search, you can pass your own `retriever` function with the following signature:

  ```python
  def retriever(agent: Agent, query: str, num_documents: Optional[int], **kwargs) -> Optional[list[dict]]:
    ...
  ```

  This function is called during `search_knowledge_base()` and is used by the Agent to retrieve references from the knowledge base.
  For more details check out the [Custom Retriever](../knowledge/custom_retriever) page.
</Tip>

## Vector Databases

While any type of storage can act as a knowledge base, vector databases offer the best solution for retrieving relevant results from dense information quickly. Here's how vector databases are used with Agents:

<Steps>
  <Step title="Chunk the information">
    Break down the knowledge into smaller chunks to ensure our search query
    returns only relevant results.
  </Step>

  <Step title="Load the knowledge base">
    Convert the chunks into embedding vectors and store them in a vector
    database.
  </Step>

  <Step title="Search the knowledge base">
    When the user sends a message, we convert the input message into an
    embedding and "search" for nearest neighbors in the vector database.
  </Step>
</Steps>

## Loading the Knowledge Base

Before you can use a knowledge base, it needs to be loaded with embeddings that will be used for retrieval.

### Asynchronous Loading

Many vector databases support asynchronous operations, which can significantly improve performance when loading large knowledge bases. You can leverage this capability using the `aload()` method:

```python
import asyncio

from agno.agent import Agent
from agno.knowledge.pdf import PDFKnowledgeBase, PDFReader
from agno.vectordb.qdrant import Qdrant

COLLECTION_NAME = "pdf-reader"

vector_db = Qdrant(collection=COLLECTION_NAME, url="http://localhost:6333")

