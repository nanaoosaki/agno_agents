---
title: The team will remember previous interactions
category: misc
source_lines: 69611-69623
line_count: 12
---

# The team will remember previous interactions
team_with_memory.print_response("What are the key challenges in quantum computing?")
team_with_memory.print_response("Elaborate on the second challenge you mentioned")
```

The team can also manage user memories:

```python
from agno.team import Team
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory

