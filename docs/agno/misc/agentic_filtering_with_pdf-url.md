---
title: Agentic filtering with Pdf-Url
category: misc
source_lines: 15792-15804
line_count: 12
---

# Agentic filtering with Pdf-Url
Source: https://docs.agno.com/examples/concepts/knowledge/filters/pdf_url/agentic_filtering

Learn how to do agentic knowledge filtering using Pdf-Url documents with user-specific metadata.

## Code

```python
from agno.agent import Agent
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.lancedb import LanceDb

