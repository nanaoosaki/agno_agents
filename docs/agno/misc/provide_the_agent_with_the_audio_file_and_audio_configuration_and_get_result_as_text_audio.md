---
title: Provide the agent with the audio file and audio configuration and get result as text + audio
category: misc
source_lines: 46478-46489
line_count: 11
---

# Provide the agent with the audio file and audio configuration and get result as text + audio
agent = Agent(
    model=OpenAIChat(
        id="gpt-4o-audio-preview",
        modalities=["text", "audio"],
        audio={"voice": "alloy", "format": "wav"},
    ),
    markdown=True,
)
response: RunResponse = agent.run("Tell me a 5 second scary story")

