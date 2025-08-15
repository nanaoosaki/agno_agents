---
title: Common events you might want to skip
category: misc
source_lines: 82678-82706
line_count: 28
---

# Common events you might want to skip
events_to_skip = [
    WorkflowRunEvent.workflow_started,
    WorkflowRunEvent.workflow_completed,
    WorkflowRunEvent.step_started,
    WorkflowRunEvent.step_completed,
    WorkflowRunEvent.parallel_execution_started,
    WorkflowRunEvent.parallel_execution_completed,
    WorkflowRunEvent.condition_execution_started,
    WorkflowRunEvent.condition_execution_completed,
    WorkflowRunEvent.loop_execution_started,
    WorkflowRunEvent.loop_execution_completed,
    WorkflowRunEvent.router_execution_started,
    WorkflowRunEvent.router_execution_completed,
]
```

**When to use:**

* **Debugging**: Store all events to analyze workflow execution flow
* **Audit Trails**: Keep records of all workflow activities for compliance
* **Performance Analysis**: Analyze timing and execution patterns
* **Error Investigation**: Review event sequences leading to failures
* **Noise Reduction**: Skip verbose events like `step_started` to focus on results

**Example Use Cases:**

```python
