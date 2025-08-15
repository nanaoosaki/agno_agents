---
title: Initialize Redis storage with default local connection
category: misc
source_lines: 69106-69113
line_count: 7
---

# Initialize Redis storage with default local connection
storage = RedisStorage(
    prefix="agno_test",    # Prefix for Redis keys to namespace the sessions
    host="localhost",      # Redis host address
    port=6379,             # Redis port number
)

