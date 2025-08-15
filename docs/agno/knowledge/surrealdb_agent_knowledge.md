---
title: SurrealDB Agent Knowledge
category: knowledge
source_lines: 81356-81388
line_count: 32
---

# SurrealDB Agent Knowledge
Source: https://docs.agno.com/vectordb/surrealdb



## Setup

```shell
docker run --rm \
  --pull always \
  -p 8000:8000 \
  surrealdb/surrealdb:latest \
  start \
  --user root \
  --pass root
```

or

```shell
./cookbook/scripts/run_surrealdb.sh
```

## Example

```python agent_with_knowledge.py
from agno.agent import Agent
from agno.embedder.openai import OpenAIEmbedder
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.surrealdb import SurrealDb
from surrealdb import Surreal

