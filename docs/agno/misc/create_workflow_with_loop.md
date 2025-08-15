---
title: Create workflow with loop
category: misc
source_lines: 55556-55585
line_count: 29
---

# Create workflow with loop
workflow = Workflow(
    name="Research and Content Workflow",
    description="Research topics in a loop until conditions are met, then create content",
    steps=[
        Loop(
            name="Research Loop",
            steps=[research_hackernews_step, research_web_step],
            end_condition=research_evaluator,
            max_iterations=3,  # Maximum 3 iterations
        ),
        content_step,
    ],
)

if __name__ == "__main__":
    # Test the workflow
    workflow.print_response(
        message="Research the latest trends in AI and machine learning, then create a summary",
    )
```

This was a synchronous non-streaming example of this pattern. To checkout async and streaming versions, see the cookbooks-

* [Loop Steps Workflow (sync streaming)](https://github.com/agno-agi/agno/tree/main/cookbook/workflows_2/sync/03_workflows_loop_execution/loop_steps_workflow_stream.py)
* [Loop Steps Workflow (async non-streaming)](https://github.com/agno-agi/agno/tree/main/cookbook/workflows_2/async/03_workflows_loop_execution/loop_steps_workflow.py)
* [Loop Steps Workflow (async streaming)](https://github.com/agno-agi/agno/tree/main/cookbook/workflows_2/async/03_workflows_loop_execution/loop_steps_workflow_stream.py)


