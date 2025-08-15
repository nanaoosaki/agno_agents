---
title: Upload the video file if it doesn't exist
category: misc
source_lines: 42029-42086
line_count: 57
---

# Upload the video file if it doesn't exist
if not video_file:
    try:
        logger.info(f"Uploading video: {video_path}")
        video_file = model.get_client().files.upload(
            file=video_path,
            config=dict(name=video_path.stem, display_name=video_path.stem),
        )

        # Check whether the file is ready to be used.
        while video_file.state.name == "PROCESSING":
            time.sleep(2)
            video_file = model.get_client().files.get(name=video_file.name)

        logger.info(f"Uploaded video: {video_file}")
    except Exception as e:
        logger.error(f"Error uploading video: {e}")

if __name__ == "__main__":
    agent.print_response(
        "Tell me about this video",
        videos=[Video(content=video_file)],
        stream=True,
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
      python cookbook/models/google/gemini/video_input_file_upload.py
      ```

      ```bash Windows
      python cookbook/models/google/gemini/video_input_file_upload.py
      ```
    </CodeGroup>
  </Step>
</Steps>


