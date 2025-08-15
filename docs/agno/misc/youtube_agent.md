---
title: Youtube Agent
category: misc
source_lines: 7988-8060
line_count: 72
---

# Youtube Agent
Source: https://docs.agno.com/examples/agents/youtube-agent



This example shows how to create an intelligent YouTube content analyzer that provides
detailed video breakdowns, timestamps, and summaries. Perfect for content creators,
researchers, and viewers who want to efficiently navigate video content.

Example prompts to try:

* "Analyze this tech review: \[video\_url]"
* "Get timestamps for this coding tutorial: \[video\_url]"
* "Break down the key points of this lecture: \[video\_url]"
* "Summarize the main topics in this documentary: \[video\_url]"
* "Create a study guide from this educational video: \[video\_url]"

## Code

```python youtube_agent.py
from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.youtube import YouTubeTools

youtube_agent = Agent(
    name="YouTube Agent",
    model=OpenAIChat(id="gpt-4o"),
    tools=[YouTubeTools()],
    show_tool_calls=True,
    instructions=dedent("""\
        You are an expert YouTube content analyst with a keen eye for detail! 🎓
        Follow these steps for comprehensive video analysis:
        1. Video Overview
           - Check video length and basic metadata
           - Identify video type (tutorial, review, lecture, etc.)
           - Note the content structure
        2. Timestamp Creation
           - Create precise, meaningful timestamps
           - Focus on major topic transitions
           - Highlight key moments and demonstrations
           - Format: [start_time, end_time, detailed_summary]
        3. Content Organization
           - Group related segments
           - Identify main themes
           - Track topic progression

        Your analysis style:
        - Begin with a video overview
        - Use clear, descriptive segment titles
        - Include relevant emojis for content types:
          📚 Educational
          💻 Technical
          🎮 Gaming
          📱 Tech Review
          🎨 Creative
        - Highlight key learning points
        - Note practical demonstrations
        - Mark important references

        Quality Guidelines:
        - Verify timestamp accuracy
        - Avoid timestamp hallucination
        - Ensure comprehensive coverage
        - Maintain consistent detail level
        - Focus on valuable content markers
    """),
    add_datetime_to_instructions=True,
    markdown=True,
)

