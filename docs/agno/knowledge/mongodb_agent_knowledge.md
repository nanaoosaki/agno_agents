---
title: MongoDB Agent Knowledge
category: knowledge
source_lines: 80791-80813
line_count: 22
---

# MongoDB Agent Knowledge
Source: https://docs.agno.com/vectordb/mongodb



## Setup

Follow the instructions in the [MongoDB Setup Guide](https://www.mongodb.com/docs/atlas/getting-started/) to get connection string

Install MongoDB packages

```shell
pip install "pymongo[srv]"
```

## Example

```python agent_with_knowledge.py
from agno.agent import Agent
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.mongodb import MongoDb

