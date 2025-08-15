---
title: Cassandra Agent Knowledge
category: knowledge
source_lines: 79963-79995
line_count: 32
---

# Cassandra Agent Knowledge
Source: https://docs.agno.com/vectordb/cassandra



## Setup

Install cassandra packages

```shell
pip install cassandra-driver
```

Run cassandra

```shell
docker run -d \
--name cassandra-db\
-p 9042:9042 \
cassandra:latest
```

## Example

```python agent_with_knowledge.py
from agno.agent import Agent
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.cassandra import Cassandra

from agno.embedder.mistral import MistralEmbedder
from agno.models.mistral import MistralChat

