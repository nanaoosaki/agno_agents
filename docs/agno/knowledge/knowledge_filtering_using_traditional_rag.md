---
title: Knowledge filtering using Traditional RAG
category: knowledge
source_lines: 13824-13840
line_count: 16
---

# Knowledge filtering using Traditional RAG
Source: https://docs.agno.com/examples/concepts/knowledge/filters/filtering-traditional-RAG

Learn how to filter knowledge in Traditional RAG using metadata like user IDs, document types, and years. This example demonstrates how to set up a knowledge base with filters and query it effectively.

## Code

```python filtering-traditional-RAG.py
from agno.agent import Agent
from agno.knowledge.text import TextKnowledgeBase
from agno.utils.media import (
    SampleDataFileExtension,
    download_knowledge_filters_sample_data,
)
from agno.vectordb.lancedb import LanceDb

