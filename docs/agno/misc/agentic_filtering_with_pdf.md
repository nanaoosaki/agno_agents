---
title: Agentic filtering with Pdf
category: misc
source_lines: 15443-15461
line_count: 18
---

# Agentic filtering with Pdf
Source: https://docs.agno.com/examples/concepts/knowledge/filters/pdf/agentic_filtering

Learn how to do agentic knowledge filtering using Pdf documents with user-specific metadata.

## Code

```python
from pathlib import Path

from agno.agent import Agent
from agno.knowledge.pdf import PDFKnowledgeBase
from agno.utils.media import (
    SampleDataFileExtension,
    download_knowledge_filters_sample_data,
)
from agno.vectordb.lancedb import LanceDb

