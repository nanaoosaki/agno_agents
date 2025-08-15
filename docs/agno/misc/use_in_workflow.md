---
title: Use in workflow
category: misc
source_lines: 82621-82678
line_count: 57
---

# Use in workflow
workflow = Workflow(
    name="Enhanced Research Workflow",
    steps=[
        Step(name="research_hackernews", agent=hackernews_agent),
        Step(name="research_web", agent=web_agent),
        Step(name="comprehensive_report", executor=create_comprehensive_report),  # Accesses both previous steps
        Step(name="final_reasoning", agent=reasoning_agent),
    ],
)
```

**Key Methods:**

* `step_input.get_step_content("step_name")` - Get content from specific step by name
* `step_input.get_all_previous_content()` - Get all previous step content combined
* `step_input.message` - Access the original workflow input message
* `step_input.previous_step_content` - Get content from immediate previous step

<Note>
  In case of `Parallel` step, when you do `step_input.get_step_content("parallel_step_name")`, it will return a dict with each key as `individual_step_name` for all the outputs from the steps defined in parallel.
  Example:

  ```python
  parallel_step_output = step_input.get_step_content("parallel_step_name")
  ```

  `parallel_step_output` will be a dict with each key as `individual_step_name` for all the outputs from the steps defined in parallel.

  ```python
  {
      "individual_step_name_1": "output_from_individual_step_1",
      "individual_step_name_2": "output_from_individual_step_2",
  }
  ```
</Note>

**More Examples**:

* [Access Multiple Previous Steps Output](/examples/workflows_2/06-workflows-advanced-concepts/access_multiple_previous_steps_output)

## Store Events

Workflows can automatically store all events for later analysis, debugging, or audit purposes.
You can also filter out specific event types to reduce noise and storage overhead.
You can access these events on the `WorkflowRunResponse` and in the `runs` column in your `Workflow's Session DB` in your configured storage backend (SQLite, PostgreSQL, etc.).

* `store_events=True`: Automatically stores all workflow events in the database
* `events_to_skip=[]`: Filter out specific event types to reduce storage and noise

Access all stored events via `workflow.run_response.events`

**Available Events to Skip:**

```python
from agno.run.v2.workflow import WorkflowRunEvent

