---
title: Define agents for different tasks
category: misc
source_lines: 56846-56932
line_count: 86
---

# Define agents for different tasks
news_agent = Agent(
    name="News Agent",
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[HackerNewsTools()],
    instructions="You are a news researcher. Get the latest tech news and summarize key points.",
)

search_agent = Agent(
    name="Search Agent",
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[GoogleSearchTools()],
    instructions="You are a search specialist. Find relevant information on given topics.",
)

analysis_agent = Agent(
    name="Analysis Agent",
    model=OpenAIChat(id="gpt-4o-mini"),
    instructions="You are an analyst. Analyze the provided information and give insights.",
)

summary_agent = Agent(
    name="Summary Agent",
    model=OpenAIChat(id="gpt-4o-mini"),
    instructions="You are a summarizer. Create concise summaries of the provided content.",
)

research_step = Step(
    name="Research Step",
    agent=news_agent,
)

search_step = Step(
    name="Search Step",
    agent=search_agent,
)


def print_stored_events(workflow, example_name):
    """Helper function to print stored events in a nice format"""
    print(f"\n--- {example_name} - Stored Events ---")
    if workflow.run_response and workflow.run_response.events:
        print(f"Total stored events: {len(workflow.run_response.events)}")
        for i, event in enumerate(workflow.run_response.events, 1):
            print(f"  {i}. {event.event}")
    else:
        print("No events stored")
    print()


print("=== Simple Step Workflow with Event Storage ===")
step_workflow = Workflow(
    name="Simple Step Workflow",
    description="Basic workflow demonstrating step event storage",
    storage=SqliteStorage(
        table_name="workflow_v2_steps",
        db_file="tmp/workflow_v2_steps.db",
        mode="workflow_v2",
    ),
    steps=[research_step, search_step],
    store_events=True,
    events_to_skip=[
        WorkflowRunEvent.step_started,
        WorkflowRunEvent.workflow_completed,
    ],  # Skip step started events to reduce noise
)

print("Running Step workflow with streaming...")
for event in step_workflow.run(
    message="AI trends in 2024",
    stream=True,
    stream_intermediate_steps=True,
):
    # Filter out RunResponseContentEvent from printing to reduce noise
    if not isinstance(
        event, (RunResponseContentEvent, ToolCallStartedEvent, ToolCallCompletedEvent)
    ):
        print(
            f"Event: {event.event if hasattr(event, 'event') else type(event).__name__}"
        )

print(f"\nStep workflow completed!")
print(
    f"Total events stored: {len(step_workflow.run_response.events) if step_workflow.run_response and step_workflow.run_response.events else 0}"
)

