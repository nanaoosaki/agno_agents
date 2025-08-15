---
title: MLX Transcribe
category: misc
source_lines: 76333-76374
line_count: 41
---

# MLX Transcribe
Source: https://docs.agno.com/tools/toolkits/others/mlx_transcribe



**MLX Transcribe** is a tool for transcribing audio files using MLX Whisper.

## Prerequisites

1. **Install ffmpeg**

   * macOS: `brew install ffmpeg`
   * Ubuntu: `sudo apt-get install ffmpeg`
   * Windows: Download from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)

2. **Install mlx-whisper library**

   ```shell
   pip install mlx-whisper
   ```

3. **Prepare audio files**

   * Create a 'storage/audio' directory
   * Place your audio files in this directory
   * Supported formats: mp3, mp4, wav, etc.

4. **Download sample audio** (optional)
   * Visit the [audio-samples](https://audio-samples.github.io/) (as an example) and save the audio file to the `storage/audio` directory.

## Example

The following agent will use MLX Transcribe to transcribe audio files.

```python cookbook/tools/mlx_transcribe_tools.py

from pathlib import Path
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.mlx_transcribe import MLXTranscribeTools

