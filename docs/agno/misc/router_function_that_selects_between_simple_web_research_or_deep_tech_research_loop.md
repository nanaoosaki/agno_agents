---
title: Router function that selects between simple web research or deep tech research loop
category: misc
source_lines: 55997-56065
line_count: 68
---

# Router function that selects between simple web research or deep tech research loop


def research_strategy_router(step_input: StepInput) -> List[Step]:
    """
    Decide between simple web research or deep tech research loop based on the input topic.
    Returns either a single web research step or a tech research loop.
    """
    # Use the original workflow message if this is the first step
    topic = step_input.previous_step_content or step_input.message or ""
    topic = topic.lower()

    # Check if the topic requires deep tech research
    deep_tech_keywords = [
        "startup trends",
        "ai developments",
        "machine learning research",
        "programming languages",
        "developer tools",
        "silicon valley",
        "venture capital",
        "cryptocurrency analysis",
        "blockchain technology",
        "open source projects",
        "github trends",
        "tech industry",
        "software engineering",
    ]

    # Check if it's a complex tech topic that needs deep research
    if any(keyword in topic for keyword in deep_tech_keywords) or (
        "tech" in topic and len(topic.split()) > 3
    ):
        print(
            f"🔬 Deep tech topic detected: Using iterative research loop for '{topic}'"
        )
        return [deep_tech_research_loop]
    else:
        print(f"🌐 Simple topic detected: Using basic web research for '{topic}'")
        return [research_web]


workflow = Workflow(
    name="Adaptive Research Workflow",
    description="Intelligently selects between simple web research or deep iterative tech research based on topic complexity",
    steps=[
        Router(
            name="research_strategy_router",
            selector=research_strategy_router,
            choices=[research_web, deep_tech_research_loop],
            description="Chooses between simple web research or deep tech research loop",
        ),
        publish_content,
    ],
)

if __name__ == "__main__":
    print("=== Testing with deep tech topic ===")
    workflow.print_response(
        "Latest developments in artificial intelligence and machine learning and deep tech research trends"
    )
```

To checkout async version, see the cookbook-

* [Router with Loop Steps Workflow (async)](https://github.com/agno-agi/agno/tree/main/cookbook/workflows_2/async/05_workflows_conditional_branching/router_with_loop_steps.py)


