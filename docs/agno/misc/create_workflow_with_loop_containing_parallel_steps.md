---
title: Create workflow with loop containing parallel steps
category: misc
source_lines: 55689-55728
line_count: 39
---

# Create workflow with loop containing parallel steps
workflow = Workflow(
    name="Advanced Research and Content Workflow",
    description="Research topics with parallel execution in a loop until conditions are met, then create content",
    steps=[
        Loop(
            name="Research Loop with Parallel Execution",
            steps=[
                Parallel(
                    research_hackernews_step,
                    research_web_step,
                    trend_analysis_step,
                    name="Parallel Research & Analysis",
                    description="Execute research and analysis in parallel for efficiency",
                ),
                sentiment_analysis_step,
            ],
            end_condition=research_evaluator,
            max_iterations=3,  # Maximum 3 iterations
        ),
        content_step,
    ],
)

if __name__ == "__main__":
    workflow.print_response(
        message="Research the latest trends in AI and machine learning, then create a summary",
        stream=True,
        stream_intermediate_steps=True,
    )
```

This was a synchronous streaming example of this pattern. To checkout async and non-streaming versions, see the cookbooks-

* [Loop with Parallel Steps Workflow (sync)](https://github.com/agno-agi/agno/tree/main/cookbook/workflows_2/sync/03_workflows_loop_execution/loop_with_parallel_steps.py)
* [Loop with Parallel Steps Workflow (async non-streaming)](https://github.com/agno-agi/agno/tree/main/cookbook/workflows_2/async/03_workflows_loop_execution/loop_with_parallel_steps.py)
* [Loop with Parallel Steps Workflow (async streaming)](https://github.com/agno-agi/agno/tree/main/cookbook/workflows_2/async/03_workflows_loop_execution/loop_with_parallel_steps_stream.py)


