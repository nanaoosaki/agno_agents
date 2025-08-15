---
title: === CONDITION EVALUATORS ===
category: misc
source_lines: 55401-55476
line_count: 75
---

# === CONDITION EVALUATORS ===
def check_if_we_should_search_hn(step_input: StepInput) -> bool:
    """Check if we should search Hacker News"""
    topic = step_input.message or step_input.previous_step_content or ""
    tech_keywords = [
        "ai",
        "machine learning",
        "programming",
        "software",
        "tech",
        "startup",
        "coding",
    ]
    return any(keyword in topic.lower() for keyword in tech_keywords)


def check_if_comprehensive_research_needed(step_input: StepInput) -> bool:
    """Check if comprehensive multi-step research is needed"""
    topic = step_input.message or step_input.previous_step_content or ""
    comprehensive_keywords = [
        "comprehensive",
        "detailed",
        "thorough",
        "in-depth",
        "complete analysis",
        "full report",
        "extensive research",
    ]
    return any(keyword in topic.lower() for keyword in comprehensive_keywords)


if __name__ == "__main__":
    workflow = Workflow(
        name="Conditional Workflow with Multi-Step Condition",
        steps=[
            Parallel(
                Condition(
                    name="HackerNewsCondition",
                    description="Check if we should search Hacker News for tech topics",
                    evaluator=check_if_we_should_search_hn,
                    steps=[research_hackernews_step],  # Single step
                ),
                Condition(
                    name="ComprehensiveResearchCondition",
                    description="Check if comprehensive multi-step research is needed",
                    evaluator=check_if_comprehensive_research_needed,
                    steps=[  # Multiple steps
                        deep_exa_analysis_step,
                        trend_analysis_step,
                        fact_verification_step,
                    ],
                ),
                name="ConditionalResearch",
                description="Run conditional research steps in parallel",
            ),
            write_step,
        ],
    )

    try:
        workflow.print_response(
            message="Comprehensive analysis of climate change research",
            stream=True,
            stream_intermediate_steps=True,
        )
    except Exception as e:
        print(f"❌ Error: {e}")
    print()
```

To see the async example, see the cookbook-

* [Condition with list of steps (async)](https://github.com/agno-agi/agno/tree/main/cookbook/workflows_2/async/02_conditional_execution/condition_with_list_of_steps.py)


