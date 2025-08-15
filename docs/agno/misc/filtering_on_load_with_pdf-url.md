---
title: Filtering on load with Pdf-Url
category: misc
source_lines: 16003-16015
line_count: 12
---

# Filtering on load with Pdf-Url
Source: https://docs.agno.com/examples/concepts/knowledge/filters/pdf_url/filtering_on_load

Learn how to filter knowledge base at load time using Pdf-Url documents with user-specific metadata.

## Code

```python
from agno.agent import Agent
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.lancedb import LanceDb

