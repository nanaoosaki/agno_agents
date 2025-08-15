---
title: Create MongoDB memory database
category: knowledge
source_lines: 17929-17936
line_count: 7
---

# Create MongoDB memory database
memory_db = MongoMemoryDb(
    connection_string=mongo_url,
    database_name=database_name,
    collection_name="memories"  # Collection name to use in the database
)

