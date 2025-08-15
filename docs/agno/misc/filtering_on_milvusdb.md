---
title: Filtering on MilvusDB
category: misc
source_lines: 14192-14208
line_count: 16
---

# Filtering on MilvusDB
Source: https://docs.agno.com/examples/concepts/knowledge/filters/filtering_milvus_db

Learn how to filter knowledge base searches using Pdf documents with user-specific metadata in MilvusDB.

## Code

```python
from agno.agent import Agent
from agno.knowledge.pdf import PDFKnowledgeBase
from agno.utils.media import (
    SampleDataFileExtension,
    download_knowledge_filters_sample_data,
)
from agno.vectordb.milvus import Milvus

