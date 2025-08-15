---
title: Filtering on Pinecone
category: misc
source_lines: 14548-14566
line_count: 18
---

# Filtering on Pinecone
Source: https://docs.agno.com/examples/concepts/knowledge/filters/filtering_pinecone

Learn how to filter knowledge base searches using Pdf documents with user-specific metadata in Pinecone.

## Code

```python
from os import getenv

from agno.agent import Agent
from agno.knowledge.pdf import PDFKnowledgeBase
from agno.utils.media import (
    SampleDataFileExtension,
    download_knowledge_filters_sample_data,
)
from agno.vectordb.pineconedb import PineconeDb

