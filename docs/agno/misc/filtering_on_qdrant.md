---
title: Filtering on Qdrant
category: misc
source_lines: 14672-14688
line_count: 16
---

# Filtering on Qdrant
Source: https://docs.agno.com/examples/concepts/knowledge/filters/filtering_qdrant_db

Learn how to filter knowledge base searches using Pdf documents with user-specific metadata in Qdrant.

## Code

```python
from agno.agent import Agent
from agno.knowledge.pdf import PDFKnowledgeBase
from agno.utils.media import (
    SampleDataFileExtension,
    download_knowledge_filters_sample_data,
)
from agno.vectordb.qdrant import Qdrant

