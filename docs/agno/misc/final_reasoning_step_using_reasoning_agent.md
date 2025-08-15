---
title: Final reasoning step using reasoning agent
category: misc
source_lines: 56380-56407
line_count: 27
---

# Final reasoning step using reasoning agent
reasoning_step = Step(
    name="final_reasoning",
    agent=reasoning_agent,
    description="Apply reasoning to create final insights and recommendations",
)

workflow = Workflow(
    name="Enhanced Research Workflow",
    description="Multi-source research with custom data flow and reasoning",
    steps=[
        research_hackernews,
        # research_web,
        comprehensive_report_step,  # Has access to both previous steps
        reasoning_step,  # Gets the last step output (comprehensive report)
    ],
)

if __name__ == "__main__":
    workflow.print_response(
        "Latest developments in artificial intelligence and machine learning",
        stream=True,
        stream_intermediate_steps=True,
    )
```


