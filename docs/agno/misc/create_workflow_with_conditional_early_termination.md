---
title: Create workflow with conditional early termination
category: misc
source_lines: 56605-56638
line_count: 33
---

# Create workflow with conditional early termination
workflow = Workflow(
    name="Data Processing with Early Exit",
    description="Process data but stop early if validation fails",
    steps=[
        data_validator,  # Step 1: Validate data
        early_exit_validator,  # Step 2: Check validation and possibly stop early
        data_processor,  # Step 3: Process data (only if validation passed)
        report_generator,  # Step 4: Generate report (only if processing completed)
    ],
)

if __name__ == "__main__":
    print("\n=== Testing with INVALID data ===")
    workflow.print_response(
        message="Process this data: {'user_count': -50, 'revenue': 'invalid_amount', 'date': 'bad_date'}"
    )

    print("=== Testing with VALID data ===")
    workflow.print_response(
        message="Process this data: {'user_count': 1000, 'revenue': 50000, 'date': '2024-01-15'}"
    )
```

To checkout async version, see the cookbook-

* [Early Stop Workflow with Loop](https://github.com/agno-agi/agno/tree/main/cookbook/workflows_2/sync/06_workflows_advanced_concepts/early_stop_workflow_with_loop.py)
* [Early Stop Workflow with Parallel](https://github.com/agno-agi/agno/tree/main/cookbook/workflows_2/sync/06_workflows_advanced_concepts/early_stop_workflow_with_parallel.py)
* [Early Stop Workflow with Router](https://github.com/agno-agi/agno/tree/main/cookbook/workflows_2/sync/06_workflows_advanced_concepts/early_stop_workflow_with_router.py)
* [Early Stop Workflow with Step](https://github.com/agno-agi/agno/tree/main/cookbook/workflows_2/sync/06_workflows_advanced_concepts/early_stop_workflow_with_step.py)
* [Early Stop Workflow with Steps](https://github.com/agno-agi/agno/tree/main/cookbook/workflows_2/sync/06_workflows_advanced_concepts/early_stop_workflow_with_steps.py)


