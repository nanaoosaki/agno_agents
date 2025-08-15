---
title: Hybrid Search- Combining Keyword and Vector Search
category: misc
source_lines: 61332-61390
line_count: 58
---

# Hybrid Search- Combining Keyword and Vector Search
Source: https://docs.agno.com/knowledge/hybrid_search

Understanding Hybrid Search and its benefits in combining keyword and vector search for better results.

With Hybrid search, you can get the precision of exact matching with the intelligence of semantic understanding. Combining both approaches will deliver more comprehensive and relevant results in many cases.

## What exactly is Hybrid Search?

**Hybrid search** is a retrieval technique that combines the strengths of both **vector search** (semantic search) and **keyword search** (lexical search) to find the most relevant results for a query.

* Vector search uses embeddings (dense vectors) to capture the semantic meaning of text, enabling the system to find results that are similar in meaning, even if the exact words don’t match.
* Keyword search (BM25, TF-IDF, etc.) matches documents based on the presence and frequency of exact words or phrases in the query.

Hybrid search blends these approaches, typically by scoring and/or ranking results from both methods, to maximize both precision and recall.

## Keyword Search vs Vector Search vs Hybrid Search

| Feature       | Keyword Search                  | Vector Search                             | Hybrid Search                             |
| ------------- | ------------------------------- | ----------------------------------------- | ----------------------------------------- |
| Based On      | Lexical matching (BM25, TF-IDF) | Embedding similarity (cosine, dot)        | Both                                      |
| Strength      | Exact matches, relevance        | Contextual meaning                        | Balanced relevance + meaning              |
| Weakness      | No semantic understanding       | Misses exact keywords                     | Slightly heavier in compute               |
| Example Match | "chicken soup" = *chicken soup* | "chicken soup" = *hot broth with chicken* | Both literal and related concepts         |
| Best Use Case | Legal docs, structured data     | Chatbots, Q\&A, semantic search           | Multimodal, real-world messy user queries |

<Note>
  Why Hybrid Search might be better for your application-

  * **Improved Recall**: Captures more relevant results missed by pure keyword or vector search.
  * **Balanced Precision**: Exact matches get priority while also including semantically relevant results.
  * **Robust to Ambiguity**: Handles spelling variations, synonyms, and fuzzy user intent.
  * **Best of Both Worlds**: Keywords matter when they should, and meaning matters when needed.

  **Perfect for **real-world apps** like recipe search, customer support, legal discovery, etc.**
</Note>

## Vector DBs in Agno that Support Hybrid Search

The following vector databases support hybrid search natively or via configurations:

| Database   | Hybrid Search Support       |
| ---------- | --------------------------- |
| `pgvector` | ✅ Yes                       |
| `milvus`   | ✅ Yes                       |
| `lancedb`  | ✅ Yes                       |
| `qdrantdb` | ✅ Yes                       |
| `weaviate` | ✅ Yes                       |
| `mongodb`  | ✅ Yes (Atlas Vector Search) |

***

## Example: Hybrid Search using `pgvector`

```python
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.pgvector import PgVector, SearchType

