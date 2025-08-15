---
title: Couchbase Integration
category: misc
source_lines: 32775-32792
line_count: 17
---

# Couchbase Integration
Source: https://docs.agno.com/examples/concepts/vectordb/couchbase



## Code

```python cookbook/agent_concepts/vector_dbs/couchbase.py
import os
import time
from agno.agent import Agent
from agno.embedder.openai import OpenAIEmbedder
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.couchbase import CouchbaseSearch
from couchbase.options import ClusterOptions, KnownConfigProfiles
from couchbase.auth import PasswordAuthenticator

