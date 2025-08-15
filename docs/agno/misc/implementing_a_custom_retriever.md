---
title: Implementing a Custom Retriever
category: misc
source_lines: 60991-61014
line_count: 23
---

# Implementing a Custom Retriever
Source: https://docs.agno.com/knowledge/custom_retriever

Learn how to implement a custom retriever for precise control over document retrieval in your knowledge base.

In some cases, you may need complete control over how your agent retrieves information from the knowledge base. This can be achieved by implementing a custom retriever function. A custom retriever allows you to define the logic for searching and retrieving documents from your vector database.

## Setup

Follow the instructions in the [Qdrant Setup Guide](https://qdrant.tech/documentation/guides/installation/) to install Qdrant locally. Here is a guide to get API keys: [Qdrant API Keys](https://qdrant.tech/documentation/cloud/authentication/).

### Example: Custom Retriever for a PDF Knowledge Base

Below is a detailed example of how to implement a custom retriever function using the `agno` library. This example demonstrates how to set up a knowledge base with PDF documents, define a custom retriever, and use it with an agent.

```python
from typing import Optional
from agno.agent import Agent
from agno.embedder.openai import OpenAIEmbedder
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.qdrant import Qdrant
from qdrant_client import QdrantClient

