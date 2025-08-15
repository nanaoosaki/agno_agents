---
title: Download the video file from the URL as bytes
category: misc
source_lines: 41955-41996
line_count: 41
---

# Download the video file from the URL as bytes
response = requests.get(url)
video_content = response.content

agent.print_response(
    "Tell me about this video",
    videos=[Video(content=video_content)],
)
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
      python cookbook/models/google/gemini/video_input_bytes_content.py
      ```

      ```bash Windows
      python cookbook/models/google/gemini/video_input_bytes_content.py
      ```
    </CodeGroup>
  </Step>
</Steps>


