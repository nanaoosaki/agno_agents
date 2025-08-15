---
title: Use the sequence in a workflow
category: misc
source_lines: 84849-84865
line_count: 16
---

# Use the sequence in a workflow
workflow = Workflow(
    name="Article Creation Workflow",
    steps=[article_creation_sequence]  # Single sequence
)

workflow.print_response("Write an article about renewable energy", markdown=True)
```

#### Steps with Router

This is where `Steps` really shines - creating distinct sequences for different content types or workflows:

```python
from agno.workflow.v2 import Steps, Router, Step, Workflow

