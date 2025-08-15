---
title: Couchbase Agent Knowledge
category: knowledge
source_lines: 80317-80379
line_count: 62
---

# Couchbase Agent Knowledge
Source: https://docs.agno.com/vectordb/couchbase



## Setup

### Local Setup (Docker)

Run Couchbase locally using Docker:

```shell
docker run -d --name couchbase-server \
  -p 8091-8096:8091-8096 \
  -p 11210:11210 \
  -e COUCHBASE_ADMINISTRATOR_USERNAME=Administrator \
  -e COUCHBASE_ADMINISTRATOR_PASSWORD=password \
  couchbase:latest
```

1. Access the Couchbase UI at: [http://localhost:8091](http://localhost:8091)
2. Login with username: `Administrator` and password: `password`
3. Create a bucket named `recipe_bucket`, a scope `recipe_scope`, and a collection `recipes`

### Managed Setup (Capella)

For a managed cluster, use [Couchbase Capella](https://cloud.couchbase.com/):

* Follow Capella's UI to create a database, bucket, scope, and collection

### Environment Variables

Set up your environment variables:

```shell
export COUCHBASE_USER="Administrator"
export COUCHBASE_PASSWORD="password" 
export COUCHBASE_CONNECTION_STRING="couchbase://localhost"
export OPENAI_API_KEY="<your-openai-api-key>"
```

For Capella, set `COUCHBASE_CONNECTION_STRING` to your Capella connection string.

### Install Dependencies

```shell
pip install couchbase
```

## Example

```python agent_with_knowledge.py
import os
import time
from agno.agent import Agent
from agno.embedder.openai import OpenAIEmbedder
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.couchbase import CouchbaseSearch
from couchbase.options import ClusterOptions, KnownConfigProfiles
from couchbase.auth import PasswordAuthenticator
from couchbase.management.search import SearchIndex

