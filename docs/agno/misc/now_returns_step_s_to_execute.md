---
title: Now returns Step(s) to execute
category: misc
source_lines: 55841-55904
line_count: 63
---

# Now returns Step(s) to execute
def research_router(step_input: StepInput) -> List[Step]:
    """
    Decide which research method to use based on the input topic.
    Returns a list containing the step(s) to execute.
    """
    # Use the original workflow message if this is the first step
    topic = step_input.previous_step_content or step_input.message or ""
    topic = topic.lower()

    # Check if the topic is tech/startup related - use HackerNews
    tech_keywords = [
        "startup",
        "programming",
        "ai",
        "machine learning",
        "software",
        "developer",
        "coding",
        "tech",
        "silicon valley",
        "venture capital",
        "cryptocurrency",
        "blockchain",
        "open source",
        "github",
    ]

    if any(keyword in topic for keyword in tech_keywords):
        print(f"🔍 Tech topic detected: Using HackerNews research for '{topic}'")
        return [research_hackernews]
    else:
        print(f"🌐 General topic detected: Using web research for '{topic}'")
        return [research_web]


workflow = Workflow(
    name="Intelligent Research Workflow",
    description="Automatically selects the best research method based on topic, then publishes content",
    steps=[
        Router(
            name="research_strategy_router",
            selector=research_router,
            choices=[research_hackernews, research_web],
            description="Intelligently selects research method based on topic",
        ),
        publish_content,
    ],
)

if __name__ == "__main__":
    workflow.print_response(
        "Latest developments in artificial intelligence and machine learning"
    )
```

This was a synchronous non-streaming example of this pattern. To checkout async and streaming versions, see the cookbooks-

* [Router Steps Workflow (sync streaming)](https://github.com/agno-agi/agno/tree/main/cookbook/workflows_2/sync/05_workflows_conditional_branching/router_steps_workflow_stream.py)
* [Router Steps Workflow (async non-streaming)](https://github.com/agno-agi/agno/tree/main/cookbook/workflows_2/async/05_workflows_conditional_branching/router_steps_workflow.py)
* [Router Steps Workflow (async streaming)](https://github.com/agno-agi/agno/tree/main/cookbook/workflows_2/async/05_workflows_conditional_branching/router_steps_workflow_stream.py)


