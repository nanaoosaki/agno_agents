---
title: Filtering with Pdf-Url
category: misc
source_lines: 15881-15911
line_count: 30
---

# Filtering with Pdf-Url
Source: https://docs.agno.com/examples/concepts/knowledge/filters/pdf_url/filtering

Learn how to filter knowledge base searches using Pdf-Url documents with user-specific metadata.

## Code

```python
"""
User-Level Knowledge Filtering Example with PDF URLs

This cookbook demonstrates how to use knowledge filters with PDF documents accessed via URLs,
showing how to restrict knowledge base searches to specific cuisines, sources, or any other metadata attributes.

Key concepts demonstrated:
1. Loading PDF documents from URLs with specific metadata
2. Filtering knowledge base searches by cuisine type
3. Combining multiple filter criteria
4. Comparing results across different filter combinations

You can pass filters in the following ways:
1. If you pass on Agent only, we use that for all runs
2. If you pass on run/print_response only, we use that for that run
3. If you pass on both, we override with the filters passed on run/print_response for that run
"""

from agno.agent import Agent
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.lancedb import LanceDb

