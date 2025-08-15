---
title: Azure Cosmos DB MongoDB vCore Agent Knowledge
category: knowledge
source_lines: 79903-79926
line_count: 23
---

# Azure Cosmos DB MongoDB vCore Agent Knowledge
Source: https://docs.agno.com/vectordb/azure_cosmos_mongodb



## Setup

Follow the instructions in the [Azure Cosmos DB Setup Guide](https://learn.microsoft.com/en-us/azure/cosmos-db/mongodb/vcore) to get the connection string.

Install MongoDB packages:

```shell
pip install "pymongo[srv]"
```

## Example

```python agent_with_knowledge.py
import urllib.parse
from agno.agent import Agent
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.mongodb import MongoDb

