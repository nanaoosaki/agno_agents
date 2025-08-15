---
title: Define and use examples
category: misc
source_lines: 56779-56813
line_count: 34
---

# Define and use examples
if __name__ == "__main__":
    content_creation_workflow = Workflow(
        name="Content Creation Workflow",
        description="Automated content creation with custom execution options",
        storage=SqliteStorage(
            table_name="workflow_v2",
            db_file="tmp/workflow_v2.db",
            mode="workflow_v2",
        ),
        steps=[research_step, content_planning_step],
    )

    # Run workflow with additional_data
    content_creation_workflow.print_response(
        message="AI trends in 2024",
        additional_data={
            "user_email": "kaustubh@agno.com",
            "priority": "high",
            "client_type": "enterprise",
        },
        markdown=True,
        stream=True,
        stream_intermediate_steps=True,
    )

    print("\n" + "=" * 60 + "\n")
```

To checkout async version, see the cookbook-

* [Step with Function using Additional Data (async)](https://github.com/agno-agi/agno/tree/main/cookbook/workflows_2/async/01_basic_workflows/step_with_function_additional_data.py)


