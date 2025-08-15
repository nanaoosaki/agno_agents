---
title: Get sample videos from https://www.pexels.com/search/videos/sample/
category: misc
source_lines: 42105-42142
line_count: 37
---

# Get sample videos from https://www.pexels.com/search/videos/sample/
video_path = Path(__file__).parent.joinpath("sample_video.mp4")

agent.print_response("Tell me about this video?", videos=[Video(filepath=video_path)])
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export GOOGLE_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U google-genai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/models/google/gemini/video_input_local_file_upload.py
      ```

      ```bash Windows
      python cookbook/models/google/gemini/video_input_local_file_upload.py
      ```
    </CodeGroup>
  </Step>
</Steps>


