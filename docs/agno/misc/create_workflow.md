---
title: Create workflow
category: misc
source_lines: 57113-57137
line_count: 24
---

# Create workflow
structured_workflow = Workflow(
    name="Structured Content Creation Pipeline",
    description="AI-powered content creation with structured data flow",
    steps=[research_step, strategy_step, planning_step],
)

if __name__ == "__main__":
    print("=== Testing Structured Output Flow Between Steps ===")

    # Test with simple string input
    structured_workflow.print_response(
        message="Latest developments in artificial intelligence and machine learning"
    )
```

Examples for some more scenarios where you can use this pattern:

* [Structured IO at each Step level Agent](https://github.com/agno-agi/agno/tree/main/cookbook/workflows_2/sync/06_workflows_advanced_concepts/structured_io_at_each_step_level_agent_stream.py)
* [Structured IO at each Step level Team](https://github.com/agno-agi/agno/tree/main/cookbook/workflows_2/async/06_workflows_advanced_concepts/structured_io_at_each_step_level_team_stream.py)
* [Structured IO at each Step level Custom Function-1](https://github.com/agno-agi/agno/tree/main/cookbook/workflows_2/sync/06_workflows_advanced_concepts/structured_io_at_each_step_level_function_1.py)
* [Structured IO at each Step level Custom Function-2](https://github.com/agno-agi/agno/tree/main/cookbook/workflows_2/sync/06_workflows_advanced_concepts/structured_io_at_each_step_level_function_2.py)


