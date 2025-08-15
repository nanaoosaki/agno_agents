---
title: Filtering on ChromaDB
category: misc
source_lines: 13956-13972
line_count: 16
---

# Filtering on ChromaDB
Source: https://docs.agno.com/examples/concepts/knowledge/filters/filtering_chroma_db

Learn how to filter knowledge base searches using Pdf documents with user-specific metadata in ChromaDB.

## Code

```python
from agno.agent import Agent
from agno.knowledge.pdf import PDFKnowledgeBase
from agno.utils.media import (
    SampleDataFileExtension,
    download_knowledge_filters_sample_data,
)
from agno.vectordb.chroma import ChromaDb

