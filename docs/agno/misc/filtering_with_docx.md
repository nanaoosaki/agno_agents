---
title: Filtering with Docx
category: misc
source_lines: 13556-13589
line_count: 33
---

# Filtering with Docx
Source: https://docs.agno.com/examples/concepts/knowledge/filters/docx/filtering

Learn how to filter knowledge base searches using Docx documents with user-specific metadata.

## Code

```python
"""
User-Level Knowledge Filtering Example

This cookbook demonstrates how to use knowledge filters to restrict knowledge base searches to specific users, document types, or any other metadata attributes.

Key concepts demonstrated:
1. Loading documents with user-specific metadata
2. Filtering knowledge base searches by user ID
3. Combining multiple filter criteria
4. Comparing results across different filter combinations

You can pass filters in the following ways:
1. If you pass on Agent only, we use that for all runs
2. If you pass on run/print_response only, we use that for that run
3. If you pass on both, we override with the filters passed on run/print_response for that run
"""

from agno.agent import Agent
from agno.knowledge.docx import DocxKnowledgeBase
from agno.utils.media import (
    SampleDataFileExtension,
    download_knowledge_filters_sample_data,
)
from agno.vectordb.lancedb import LanceDb

