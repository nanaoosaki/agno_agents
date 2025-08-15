---
title: Create workflow with workflow_session_state
category: misc
source_lines: 85164-85213
line_count: 49
---

# Create workflow with workflow_session_state
shopping_workflow = Workflow(
    name="Shopping List Workflow",
    steps=[manage_items_step, view_list_step],
    workflow_session_state={},  # Initialize empty workflow session state
)

if __name__ == "__main__":
    # Example 1: Add items to the shopping list
    print("=== Example 1: Adding Items ===")
    shopping_workflow.print_response(
        message="Please add milk, bread, and eggs to my shopping list."
    )
    print("Workflow session state:", shopping_workflow.workflow_session_state)

    # Example 2: Add more items and view list
    print("\n=== Example 2: Adding More Items ===")
    shopping_workflow.print_response(
        message="Add apples and bananas to the list, then show me the complete list."
    )
    print("Workflow session state:", shopping_workflow.workflow_session_state)

    # Example 3: Remove items
    print("\n=== Example 3: Removing Items ===")
    shopping_workflow.print_response(
        message="Remove bread from the list and show me what's left."
    )
    print("Workflow session state:", shopping_workflow.workflow_session_state)

    # Example 4: Clear the entire list
    print("\n=== Example 4: Clearing List ===")
    shopping_workflow.print_response(
        message="Clear the entire shopping list and confirm it's empty."
    )
    print("Final workflow session state:", shopping_workflow.workflow_session_state)
```

In the example, the `add_item` function which is passed as a tool to the `Agent` modifies the workflow session state by adding an item to the shopping list.

<Note>
  The `workflow_session_state` is shared across all agents and teams within a workflow. This allows for seamless collaboration and data sharing between different components.
</Note>

**More Examples**:

* [Shared Session State with Agent](https://github.com/agno-agi/agno/tree/main/cookbook/workflows_2/sync/06_workflows_advanced_concepts/shared_session_state_with_agent.py)
* [Shared Session State with Team](https://github.com/agno-agi/agno/tree/main/cookbook/workflows_2/sync/06_workflows_advanced_concepts/shared_session_state_with_team.py)


