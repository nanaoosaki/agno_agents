---
title: Filtering with Pdf
category: misc
source_lines: 15567-15583
line_count: 16
---

# Filtering with Pdf
Source: https://docs.agno.com/examples/concepts/knowledge/filters/pdf/filtering

Learn how to filter knowledge base searches using Pdf documents with user-specific metadata.

## Code

```python
from agno.agent import Agent
from agno.knowledge.pdf import PDFKnowledgeBase
from agno.utils.media import (
    SampleDataFileExtension,
    download_knowledge_filters_sample_data,
)
from agno.vectordb.lancedb import LanceDb

