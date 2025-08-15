---
title: Filtering on SurrealDB
category: misc
source_lines: 14788-14805
line_count: 17
---

# Filtering on SurrealDB
Source: https://docs.agno.com/examples/concepts/knowledge/filters/filtering_surreal_db

Learn how to filter knowledge base searches using Pdf documents with user-specific metadata in SurrealDB.

## Code

```python
from agno.agent import Agent
from agno.knowledge.pdf import PDFKnowledgeBase
from agno.utils.media import (
    SampleDataFileExtension,
    download_knowledge_filters_sample_data,
)
from agno.vectordb.surrealdb import SurrealDb
from surrealdb import Surreal

