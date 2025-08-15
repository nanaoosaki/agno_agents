---
title: Create Redis memory database
category: knowledge
source_lines: 18097-18104
line_count: 7
---

# Create Redis memory database
memory_db = RedisMemoryDb(
    prefix="agno_memory",  # Prefix for Redis keys to namespace the memories
    host="localhost",      # Redis host address
    port=6379,             # Redis port number
)

