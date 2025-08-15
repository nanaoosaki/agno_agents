---
title: Filtering on Weaviate
category: misc
source_lines: 14926-14943
line_count: 17
---

# Filtering on Weaviate
Source: https://docs.agno.com/examples/concepts/knowledge/filters/filtering_weaviate

Learn how to filter knowledge base searches using Pdf documents with user-specific metadata in Weaviate.

## Code

```python
from agno.agent import Agent
from agno.knowledge.pdf import PDFKnowledgeBase
from agno.utils.media import (
    SampleDataFileExtension,
    download_knowledge_filters_sample_data,
)
from agno.vectordb.search import SearchType
from agno.vectordb.weaviate import Distance, VectorIndex, Weaviate

