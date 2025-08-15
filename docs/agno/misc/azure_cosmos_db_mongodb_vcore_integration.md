---
title: Azure Cosmos DB MongoDB vCore Integration
category: misc
source_lines: 32502-32515
line_count: 13
---

# Azure Cosmos DB MongoDB vCore Integration
Source: https://docs.agno.com/examples/concepts/vectordb/azure_cosmos_mongodb



## Code

```python cookbook/agent_concepts/knowledge/vector_dbs/mongo_db/cosmos_mongodb_vcore.py
import urllib.parse
from agno.agent import Agent
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.mongodb import MongoDb

