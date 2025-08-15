---
title: MongoDB Atlas connection string
category: misc
source_lines: 80813-80831
line_count: 18
---

# MongoDB Atlas connection string
"""
Example connection strings:
"mongodb+srv://<username>:<password>@cluster0.mongodb.net/?retryWrites=true&w=majority"
"mongodb://localhost/?directConnection=true"
"""
mdb_connection_string = ""

knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=MongoDb(
        collection_name="recipes",
        db_url=mdb_connection_string,
        wait_until_index_ready=60,
        wait_after_insert=300
    ),
)  # adjust wait_after_insert and wait_until_index_ready to your needs

