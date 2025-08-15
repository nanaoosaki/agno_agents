---
title: Milvus Agent Knowledge
category: knowledge
source_lines: 80691-80722
line_count: 31
---

# Milvus Agent Knowledge
Source: https://docs.agno.com/vectordb/milvus



## Setup

```shell
pip install pymilvus
```

## Initialize Milvus

Set the uri and token for your Milvus server.

* If you only need a local vector database for small scale data or prototyping, setting the uri as a local file, e.g.`./milvus.db`, is the most convenient method, as it automatically utilizes [Milvus Lite](https://milvus.io/docs/milvus_lite.md) to store all data in this file.
* If you have large scale data, say more than a million vectors, you can set up a more performant Milvus server on [Docker or Kubernetes](https://milvus.io/docs/quickstart.md).
  In this setup, please use the server address and port as your uri, e.g.`http://localhost:19530`. If you enable the authentication feature on Milvus, use `your_username:your_password` as the token, otherwise don't set the token.
* If you use [Zilliz Cloud](https://zilliz.com/cloud), the fully managed cloud service for Milvus, adjust the `uri` and `token`, which correspond to the [Public Endpoint and API key](https://docs.zilliz.com/docs/on-zilliz-cloud-console#cluster-details) in Zilliz Cloud.

## Example

```python agent_with_knowledge.py
from agno.agent import Agent
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.milvus import Milvus

vector_db = Milvus(
    collection="recipes",
    uri="./milvus.db",
)
