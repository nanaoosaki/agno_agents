---
title: Agentic filtering with Docx
category: misc
source_lines: 13432-13450
line_count: 18
---

# Agentic filtering with Docx
Source: https://docs.agno.com/examples/concepts/knowledge/filters/docx/agentic_filtering

Learn how to do agentic knowledge filtering using Docx documents with user-specific metadata.

## Code

```python
from pathlib import Path

from agno.agent import Agent
from agno.knowledge.docx import DocxKnowledgeBase
from agno.utils.media import (
    SampleDataFileExtension,
    download_knowledge_filters_sample_data,
)
from agno.vectordb.lancedb import LanceDb

