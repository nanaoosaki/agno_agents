---
title: Reasoning Agent with Knowledge Tools
category: knowledge
source_lines: 22970-22986
line_count: 16
---

# Reasoning Agent with Knowledge Tools
Source: https://docs.agno.com/examples/concepts/reasoning/tools/knowledge-tools



## Code

```python cookbook/reasoning/tools/knowledge_tools.py

from agno.agent import Agent
from agno.embedder.openai import OpenAIEmbedder
from agno.knowledge.url import UrlKnowledge
from agno.models.openai import OpenAIChat
from agno.tools.knowledge import KnowledgeTools
from agno.vectordb.lancedb import LanceDb, SearchType

