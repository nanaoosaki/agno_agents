---
title: === BASIC LINEAR WORKFLOW ===
category: misc
source_lines: 84364-84421
line_count: 57
---

# === BASIC LINEAR WORKFLOW ===
basic_workflow = Workflow(
    name="Basic Linear Workflow",
    description="Research -> Summarize -> Condition(Fact Check) -> Write Article",
    steps=[
        research_step,
        summarize_step,
        Condition(
            name="fact_check_condition",
            description="Check if fact-checking is needed",
            evaluator=needs_fact_checking,
            steps=[fact_check_step],
        ),
        write_article,
    ],
)

if __name__ == "__main__":
    try:
        response: Iterator[WorkflowRunResponseEvent] = basic_workflow.run(
            message="Recent breakthroughs in quantum computing",
            stream=True,
            stream_intermediate_steps=True,
        )
        for event in response:
            if event.event == WorkflowRunEvent.condition_execution_started.value:
                print(event)
                print()
            elif event.event == WorkflowRunEvent.condition_execution_completed.value:
                print(event)
                print()
            elif event.event == WorkflowRunEvent.workflow_started.value:
                print(event)
                print()
            elif event.event == WorkflowRunEvent.step_started.value:
                print(event)
                print()
            elif event.event == WorkflowRunEvent.step_completed.value:
                print(event)
                print() 
            elif event.event == WorkflowRunEvent.workflow_completed.value:
                print(event)
                print()
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback

        traceback.print_exc()
```

### Async Streaming

The `Workflow.arun(stream=True)` returns an async iterator of `WorkflowRunResponseEvent` objects instead of a single response.
So for example, if you want to stream the response, you can do the following:

```Python

