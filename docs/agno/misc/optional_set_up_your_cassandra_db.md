---
title: (Optional) Set up your Cassandra DB
category: misc
source_lines: 79995-80013
line_count: 18
---

# (Optional) Set up your Cassandra DB

cluster = Cluster()

session = cluster.connect()
session.execute(
    """
    CREATE KEYSPACE IF NOT EXISTS testkeyspace
    WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }
    """
)

knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=Cassandra(table_name="recipes", keyspace="testkeyspace", session=session, embedder=MistralEmbedder()),
)


