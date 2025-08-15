---
title: MoviePy Video Tools
category: tools
source_lines: 76483-76570
line_count: 87
---

# MoviePy Video Tools
Source: https://docs.agno.com/tools/toolkits/others/moviepy

Agno MoviePyVideoTools enable an Agent to process videos, extract audio, generate SRT caption files, and embed rich, word-highlighted captions.

## Prerequisites

To use `MoviePyVideoTools`, you need to install `moviepy` and its dependency `ffmpeg`:

```shell
pip install moviepy ffmpeg
```

**Important for Captioning Workflow:**
The `create_srt` and `embed_captions` tools require a transcription of the video's audio. `MoviePyVideoTools` itself does not perform speech-to-text. You'll typically use another tool, such as `OpenAITools` with its `transcribe_audio` function, to generate the transcription (often in SRT format) which is then used by these tools.

## Example

The following example demonstrates a complete workflow where an agent uses `MoviePyVideoTools` in conjunction with `OpenAITools` to:

1. Extract audio from a video file
2. Transcribe the audio using OpenAI's speech-to-text
3. Generate an SRT caption file from the transcription
4. Embed the captions into the video with word-level highlighting

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.moviepy_video import MoviePyVideoTools
from agno.tools.openai import OpenAITools

video_tools = MoviePyVideoTools(
    process_video=True, generate_captions=True, embed_captions=True
)

openai_tools = OpenAITools()

video_caption_agent = Agent(
    name="Video Caption Generator Agent",
    model=OpenAIChat(
        id="gpt-4o",
    ),
    tools=[video_tools, openai_tools],
    description="You are an AI agent that can generate and embed captions for videos.",
    instructions=[
        "When a user provides a video, process it to generate captions.",
        "Use the video processing tools in this sequence:",
        "1. Extract audio from the video using extract_audio",
        "2. Transcribe the audio using transcribe_audio",
        "3. Generate SRT captions using create_srt",
        "4. Embed captions into the video using embed_captions",
    ],
    markdown=True,
)


video_caption_agent.print_response(
    "Generate captions for {video with location} and embed them in the video"
)
```

## Toolkit Functions

These are the functions exposed by `MoviePyVideoTools`:

| Function         | Description                                                                                            |
| ---------------- | ------------------------------------------------------------------------------------------------------ |
| `extract_audio`  | Extracts the audio track from a video file and saves it to a specified output path.                    |
| `create_srt`     | Saves a given transcription (expected in SRT format) to a `.srt` file at the specified output path.    |
| `embed_captions` | Embeds captions from an SRT file into a video, creating a new video file with word-level highlighting. |

## Toolkit Parameters

These parameters are passed to the `MoviePyVideoTools` constructor:

| Parameter           | Type   | Default | Description                        |
| ------------------- | ------ | ------- | ---------------------------------- |
| `process_video`     | `bool` | `True`  | Enables the `extract_audio` tool.  |
| `generate_captions` | `bool` | `True`  | Enables the `create_srt` tool.     |
| `embed_captions`    | `bool` | `True`  | Enables the `embed_captions` tool. |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/moviepy_video.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/moviepy_video_tools.py)


