---
title: Filtering on load with Docx
category: misc
source_lines: 13705-13721
line_count: 16
---

# Filtering on load with Docx
Source: https://docs.agno.com/examples/concepts/knowledge/filters/docx/filtering_on_load

Learn how to filter knowledge base at load time using Docx documents with user-specific metadata.

## Code

```python
from agno.agent import Agent
from agno.knowledge.docx import DocxKnowledgeBase
from agno.utils.media import (
    SampleDataFileExtension,
    download_knowledge_filters_sample_data,
)
from agno.vectordb.lancedb import LanceDb

