---
title: Filtering on PgVector
category: misc
source_lines: 14430-14446
line_count: 16
---

# Filtering on PgVector
Source: https://docs.agno.com/examples/concepts/knowledge/filters/filtering_pgvector

Learn how to filter knowledge base searches using Pdf documents with user-specific metadata in PgVector.

## Code

```python
from agno.agent import Agent
from agno.knowledge.pdf import PDFKnowledgeBase
from agno.utils.media import (
    SampleDataFileExtension,
    download_knowledge_filters_sample_data,
)
from agno.vectordb.pgvector import PgVector

