---
title: store only important events
category: misc
source_lines: 82713-82725
line_count: 12
---

# store only important events
production_workflow = Workflow(
    name="Production Workflow", 
    store_events=True,
    events_to_skip=[
        WorkflowRunEvent.step_started,
        WorkflowRunEvent.parallel_execution_started,
        # keep step_completed and workflow_completed
    ],
    steps=[...]
)

