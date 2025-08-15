---
title: Complex workflow combining multiple patterns
category: misc
source_lines: 84970-85018
line_count: 48
---

# Complex workflow combining multiple patterns
workflow = Workflow(
    name="Advanced Multi-Pattern Workflow",
    steps=[
        Parallel(
            Condition(
                name="Tech Check",
                evaluator=is_tech_topic,
                steps=[Step(name="Tech Research", agent=tech_researcher)]
            ),
            Condition(
                name="Business Check", 
                evaluator=is_business_topic,
                steps=[
                    Loop(
                        name="Deep Business Research",
                        steps=[Step(name="Market Research", agent=market_researcher)],
                        end_condition=research_quality_check,
                        max_iterations=3
                    )
                ]
            ),
            name="Conditional Research Phase"
        ),
        Step(
            name="Research Post-Processing",
            executor=research_post_processor,
            description="Consolidate and analyze research findings with quality metrics"
        ),
        Router(
            name="Content Type Router",
            selector=content_type_selector,
            choices=[blog_post_step, social_media_step, report_step]
        ),
        Step(name="Final Review", agent=reviewer),
    ]
)

workflow.print_response("Create a comprehensive analysis of sustainable technology trends and their business impact for 2024", markdown=True)
```

**More Examples**:

* [Condition and Parallel Steps (Streaming Example)](/examples/workflows_2/02-workflows-conditional-execution/condition_and_parallel_steps_stream)
* [Loop with Parallel Steps (Streaming Example)](/examples/workflows_2/03-workflows-loop-execution/loop_with_parallel_steps_stream)
* [Router with Loop Steps](/examples/workflows_2/05-workflows-conditional-branching/router_with_loop_steps)


