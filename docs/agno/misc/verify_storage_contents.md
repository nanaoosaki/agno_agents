---
title: Verify storage contents
category: misc
source_lines: 69124-69145
line_count: 21
---

# Verify storage contents
print("\nVerifying storage contents...")
all_sessions = storage.get_all_sessions()
print(f"Total sessions in Redis: {len(all_sessions)}")

if all_sessions:
    print("\nSession details:")
    session = all_sessions[0]
    print(f"Session ID: {session.session_id}")
    print(f"Messages count: {len(session.memory['messages'])}")
```

## Params

<Snippet file="storage-redis-params.mdx" />

## Developer Resources

* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/storage/redis_storage/redis_storage_for_agent.py)


