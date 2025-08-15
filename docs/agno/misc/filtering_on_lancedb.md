---
title: Filtering on LanceDB
category: misc
source_lines: 14072-14088
line_count: 16
---

# Filtering on LanceDB
Source: https://docs.agno.com/examples/concepts/knowledge/filters/filtering_lance_db

Learn how to filter knowledge base searches using Pdf documents with user-specific metadata in LanceDB.

## Code

```python
from agno.agent import Agent
from agno.knowledge.pdf import PDFKnowledgeBase
from agno.utils.media import (
    SampleDataFileExtension,
    download_knowledge_filters_sample_data,
)
from agno.vectordb.lancedb import LanceDb

