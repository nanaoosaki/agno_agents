---
title: Agentic filtering with Json
category: misc
source_lines: 15047-15065
line_count: 18
---

# Agentic filtering with Json
Source: https://docs.agno.com/examples/concepts/knowledge/filters/json/agentic_filtering

Learn how to do agentic knowledge filtering using Json documents with user-specific metadata.

## Code

```python
from pathlib import Path

from agno.agent import Agent
from agno.knowledge.json import JSONKnowledgeBase
from agno.utils.media import (
    SampleDataFileExtension,
    download_knowledge_filters_sample_data,
)
from agno.vectordb.lancedb import LanceDb

