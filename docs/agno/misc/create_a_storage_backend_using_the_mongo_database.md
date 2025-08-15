---
title: Create a storage backend using the Mongo database
category: misc
source_lines: 68963-68970
line_count: 7
---

# Create a storage backend using the Mongo database
storage = MongoDbStorage(
    # store sessions in the agent_sessions collection
    collection_name="agent_sessions",
    db_url=db_url,
)

