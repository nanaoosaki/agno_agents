---
title: Filtering on load with Json
category: misc
source_lines: 15324-15340
line_count: 16
---

# Filtering on load with Json
Source: https://docs.agno.com/examples/concepts/knowledge/filters/json/filtering_on_load

Learn how to filter knowledge base at load time using Json documents with user-specific metadata.

## Code

```python
from agno.agent import Agent
from agno.knowledge.json import JSONKnowledgeBase
from agno.utils.media import (
    SampleDataFileExtension,
    download_knowledge_filters_sample_data,
)
from agno.vectordb.lancedb import LanceDb

