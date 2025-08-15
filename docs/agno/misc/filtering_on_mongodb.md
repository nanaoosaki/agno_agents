---
title: Filtering on MongoDB
category: misc
source_lines: 14311-14327
line_count: 16
---

# Filtering on MongoDB
Source: https://docs.agno.com/examples/concepts/knowledge/filters/filtering_mongo_db

Learn how to filter knowledge base searches using Pdf documents with user-specific metadata in MongoDB.

## Code

```python
from agno.agent import Agent
from agno.knowledge.pdf import PDFKnowledgeBase
from agno.utils.media import (
    SampleDataFileExtension,
    download_knowledge_filters_sample_data,
)
from agno.vectordb.mongodb import MongoDb

