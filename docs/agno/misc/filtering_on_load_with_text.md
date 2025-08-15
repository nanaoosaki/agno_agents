---
title: Filtering on load with Text
category: misc
source_lines: 16370-16386
line_count: 16
---

# Filtering on load with Text
Source: https://docs.agno.com/examples/concepts/knowledge/filters/text/filtering_on_load

Learn how to filter knowledge base at load time using Text documents with user-specific metadata.

## Code

```python
from agno.agent import Agent
from agno.knowledge.text import TextKnowledgeBase
from agno.utils.media import (
    SampleDataFileExtension,
    download_knowledge_filters_sample_data,
)
from agno.vectordb.lancedb import LanceDb

