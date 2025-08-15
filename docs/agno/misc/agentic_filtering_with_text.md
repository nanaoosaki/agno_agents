---
title: Agentic filtering with Text
category: misc
source_lines: 16093-16111
line_count: 18
---

# Agentic filtering with Text
Source: https://docs.agno.com/examples/concepts/knowledge/filters/text/agentic_filtering

Learn how to do agentic knowledge filtering using Text documents with user-specific metadata.

## Code

```python
from pathlib import Path

from agno.agent import Agent
from agno.knowledge.text import TextKnowledgeBase
from agno.utils.media import (
    SampleDataFileExtension,
    download_knowledge_filters_sample_data,
)
from agno.vectordb.lancedb import LanceDb

