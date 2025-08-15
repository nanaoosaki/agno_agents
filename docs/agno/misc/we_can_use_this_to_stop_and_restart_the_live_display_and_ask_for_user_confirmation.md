---
title: We can use this to stop and restart the live display and ask for user confirmation
category: misc
source_lines: 71381-71448
line_count: 67
---

# We can use this to stop and restart the live display and ask for user confirmation
console = Console()


def confirmation_hook(
    function_name: str, function_call: Callable, arguments: Dict[str, Any]
):
    # Get the live display instance from the console
    live = console._live

    # Stop the live display temporarily so we can ask for user confirmation
    live.stop()  # type: ignore

    # Ask for confirmation
    console.print(f"\nAbout to run [bold blue]{function_name}[/]")
    message = (
        Prompt.ask("Do you want to continue?", choices=["y", "n"], default="y")
        .strip()
        .lower()
    )

    # Restart the live display
    live.start()  # type: ignore

    # If the user does not want to continue, raise a StopExecution exception
    if message != "y":
        raise StopAgentRun(
            "Tool call cancelled by user",
            agent_message="Stopping execution as permission was not granted.",
        )
    
    # Call the function
    result = function_call(**arguments)

    # Optionally transform the result

    return result


@tool(tool_hooks=[confirmation_hook])
def get_top_hackernews_stories(num_stories: int) -> Iterator[str]:
    """Fetch top stories from Hacker News.

    Args:
        num_stories (int): Number of stories to retrieve

    Returns:
        str: JSON string containing story details
    """
    # Fetch top story IDs
    response = httpx.get("https://hacker-news.firebaseio.com/v0/topstories.json")
    story_ids = response.json()

    # Yield story details
    final_stories = []
    for story_id in story_ids[:num_stories]:
        story_response = httpx.get(
            f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        )
        story = story_response.json()
        if "text" in story:
            story.pop("text", None)
        final_stories.append(story)

    return json.dumps(final_stories)


