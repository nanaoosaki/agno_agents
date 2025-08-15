---
title: Define your workflow
category: misc
source_lines: 84421-84525
line_count: 104
---

# Define your workflow
...

async def main():
    try:
        response: AsyncIterator[WorkflowRunResponseEvent] = await basic_workflow.arun(
            message="Recent breakthroughs in quantum computing",
            stream=True,
            stream_intermediate_steps=True,
        )
        async for event in response:
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

if __name__ == "__main__":
    asyncio.run(main())
```

### Event Types

The following events are yielded by the `Workflow.run()` and `Workflow.arun()` functions depending on the workflow's configuration:

#### Core Events

| Event Type          | Description                                         |
| ------------------- | --------------------------------------------------- |
| `WorkflowStarted`   | Indicates the start of a workflow run               |
| `WorkflowCompleted` | Signals successful completion of the workflow run   |
| `WorkflowError`     | Indicates an error occurred during the workflow run |

#### Step Events

| Event Type      | Description                               |
| --------------- | ----------------------------------------- |
| `StepStarted`   | Indicates the start of a step             |
| `StepCompleted` | Signals successful completion of a step   |
| `StepError`     | Indicates an error occurred during a step |

#### Step Output Events (For custom functions)

| Event Type   | Description                    |
| ------------ | ------------------------------ |
| `StepOutput` | Indicates the output of a step |

#### Parallel Execution Events

| Event Type                   | Description                                      |
| ---------------------------- | ------------------------------------------------ |
| `ParallelExecutionStarted`   | Indicates the start of a parallel step           |
| `ParallelExecutionCompleted` | Signals successful completion of a parallel step |

#### Condition Execution Events

| Event Type                    | Description                                  |
| ----------------------------- | -------------------------------------------- |
| `ConditionExecutionStarted`   | Indicates the start of a condition           |
| `ConditionExecutionCompleted` | Signals successful completion of a condition |

#### Loop Execution Events

| Event Type                    | Description                                       |
| ----------------------------- | ------------------------------------------------- |
| `LoopExecutionStarted`        | Indicates the start of a loop                     |
| `LoopIterationStartedEvent`   | Indicates the start of a loop iteration           |
| `LoopIterationCompletedEvent` | Signals successful completion of a loop iteration |
| `LoopExecutionCompleted`      | Signals successful completion of a loop           |

#### Router Execution Events

| Event Type                 | Description                               |
| -------------------------- | ----------------------------------------- |
| `RouterExecutionStarted`   | Indicates the start of a router           |
| `RouterExecutionCompleted` | Signals successful completion of a router |

#### Steps Execution Events

| Event Type                | Description                                        |
| ------------------------- | -------------------------------------------------- |
| `StepsExecutionStarted`   | Indicates the start of `Steps` being executed      |
| `StepsExecutionCompleted` | Signals successful completion of `Steps` execution |

See detailed documentation in the [WorkflowRunResponseEvent](/reference/workflows_2/workflow_run_response) documentation.


