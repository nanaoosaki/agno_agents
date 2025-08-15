---
title: Weaviate Agent Knowledge
category: knowledge
source_lines: 81511-81557
line_count: 46
---

# Weaviate Agent Knowledge
Source: https://docs.agno.com/vectordb/weaviate



Follow steps mentioned in [Weaviate setup guide](https://weaviate.io/developers/weaviate/quickstart) to setup Weaviate.

## Setup

Install weaviate packages

```shell
pip install weaviate-client
```

Run weaviate

```shell
docker run -d \
-p 8080:8080 \
-p 50051:50051 \
--name weaviate \
cr.weaviate.io/semitechnologies/weaviate:1.28.4 
```

or

```shell
./cookbook/scripts/run_weaviate.sh
```

## Example

```python agent_with_knowledge.py
from agno.agent import Agent
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.search import SearchType
from agno.vectordb.weaviate import Distance, VectorIndex, Weaviate

vector_db = Weaviate(
    collection="recipes",
    search_type=SearchType.hybrid,
    vector_index=VectorIndex.HNSW,
    distance=Distance.COSINE,
    local=True,  # Set to False if using Weaviate Cloud and True if using local instance
)
