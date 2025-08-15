---
title: Initialize Pinecone
category: misc
source_lines: 14571-14584
line_count: 13
---

# Initialize Pinecone
api_key = getenv("PINECONE_API_KEY")
index_name = "thai-recipe-index"

vector_db = PineconeDb(
    name=index_name,
    dimension=1536,
    metric="cosine",
    spec={"serverless": {"cloud": "aws", "region": "us-east-1"}},
    api_key=api_key,
)


