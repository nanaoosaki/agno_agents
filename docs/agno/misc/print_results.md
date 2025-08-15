---
title: Print results
category: misc
source_lines: 19494-19546
line_count: 52
---

# Print results
print("\n--- Generated Shorts ---")
for short in shorts:
    print(f"Short at {short['path']}")
    print(f"Description: {short['description']}")
    print(f"Engagement Score: {short['score']}/10\n")
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
    pip install -U opencv-python google-generativeai sqlalchemy ffmpeg-python agno
    ```
  </Step>

  <Step title="Install ffmpeg">
    <CodeGroup>
      ```bash Mac
      brew install ffmpeg
      ```

      ```bash Windows
      # Install ffmpeg using chocolatey or download from https://ffmpeg.org/download.html
      choco install ffmpeg
      ```
    </CodeGroup>
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/agent_concepts/multimodal/video_to_shorts.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/multimodal/video_to_shorts.py
      ```
    </CodeGroup>
  </Step>
</Steps>


