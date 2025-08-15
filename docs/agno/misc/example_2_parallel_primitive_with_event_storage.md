---
title: Example 2: Parallel Primitive with Event Storage
category: misc
source_lines: 56938-56980
line_count: 42
---

# Example 2: Parallel Primitive with Event Storage
print("=== 2. Parallel Example ===")
parallel_workflow = Workflow(
    name="Parallel Research Workflow",
    steps=[
        Parallel(
            Step(name="News Research", agent=news_agent),
            Step(name="Web Search", agent=search_agent),
            name="Parallel Research",
        ),
        Step(name="Combine Results", agent=analysis_agent),
    ],
    storage=SqliteStorage(
        table_name="workflow_v2_parallel",
        db_file="tmp/workflow_v2_parallel.db",
        mode="workflow_v2",
    ),
    store_events=True,
    events_to_skip=[
        WorkflowRunEvent.parallel_execution_started,
        WorkflowRunEvent.parallel_execution_completed,
    ],
)

print("Running Parallel workflow...")
for event in parallel_workflow.run(
    message="Research machine learning developments",
    stream=True,
    stream_intermediate_steps=True,
):
    # Filter out RunResponseContentEvent from printing
    if not isinstance(event, RunResponseContentEvent):
        print(
            f"Event: {event.event if hasattr(event, 'event') else type(event).__name__}"
        )

print(f"Parallel workflow stored {len(parallel_workflow.run_response.events)} events")
print_stored_events(parallel_workflow, "Parallel Workflow")
print()
```


