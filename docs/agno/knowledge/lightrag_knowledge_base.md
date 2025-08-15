---
title: LightRAG Knowledge Base
category: knowledge
source_lines: 61717-61733
line_count: 16
---

# LightRAG Knowledge Base
Source: https://docs.agno.com/knowledge/lightrag

Learn how to use LightRAG, a fast graph-based retrieval-augmented generation system for enhanced knowledge querying.

The **LightRAGKnowledgeBase** integrates with a [LightRAG Server](https://github.com/HKUDS/LightRAG), a simple and fast retrieval-augmented generation system that uses graph structures to enhance document retrieval and knowledge querying capabilities.

## Usage

```python knowledge_base.py
import asyncio

from agno.agent import Agent
from agno.knowledge.light_rag import LightRagKnowledgeBase, lightrag_retriever
from agno.models.anthropic import Claude

