---
title: Filtering on load with Pdf
category: misc
source_lines: 15683-15699
line_count: 16
---

# Filtering on load with Pdf
Source: https://docs.agno.com/examples/concepts/knowledge/filters/pdf/filtering_on_load

Learn how to filter knowledge base at load time using Pdf documents with user-specific metadata.

## Code

```python
from agno.agent import Agent
from agno.knowledge.pdf import PDFKnowledgeBase
from agno.utils.media import (
    SampleDataFileExtension,
    download_knowledge_filters_sample_data,
)
from agno.vectordb.lancedb import LanceDb

