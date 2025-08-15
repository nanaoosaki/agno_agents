---
title: Create workflow with direct execution
category: misc
source_lines: 55759-55779
line_count: 20
---

# Create workflow with direct execution
workflow = Workflow(
    name="Content Creation Pipeline",
    steps=[
        Parallel(research_hn_step, research_web_step, name="Research Phase"),
        write_step,
        review_step,
    ],
)

workflow.print_response("Write about the latest AI developments")
```

This was a synchronous non-streaming example of this pattern. To checkout async and streaming versions, see the cookbooks-

* [Parallel Steps Workflow (sync streaming)](https://github.com/agno-agi/agno/tree/main/cookbook/workflows_2/sync/04_workflows_parallel_execution/parallel_steps_workflow_stream.py)
* [Parallel Steps Workflow (async non-streaming)](https://github.com/agno-agi/agno/tree/main/cookbook/workflows_2/async/04_workflows_parallel_execution/parallel_steps_workflow.py)
* [Parallel Steps Workflow (async streaming)](https://github.com/agno-agi/agno/tree/main/cookbook/workflows_2/async/04_workflows_parallel_execution/parallel_steps_workflow_stream.py)


