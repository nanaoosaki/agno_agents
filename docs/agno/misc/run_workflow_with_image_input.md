---
title: Run workflow with image input
category: misc
source_lines: 82970-83006
line_count: 36
---

# Run workflow with image input
if __name__ == "__main__":
    media_workflow.print_response(
        message="Please analyze this image and find related news",
        images=[
            Image(url="https://upload.wikimedia.org/wikipedia/commons/0/0c/GoldenGateBridge-001.jpg")
        ],
        markdown=True,
    )
```

<Note>
  If you are using `Workflow.run()`, you need to use `WorkflowRunResponse` to access the images, videos, and audio.

  ```python
  from agno.run.v2.workflow import WorkflowRunResponse

  response: WorkflowRunResponse = media_workflow.run(
      message="Please analyze this image and find related news",
      images=[
          Image(url="https://upload.wikimedia.org/wikipedia/commons/0/0c/GoldenGateBridge-001.jpg")
      ],
      markdown=True,
  )

  print(response.images)
  ```
</Note>

Similarly, you can pass `Video` and `Audio` as input.

**More Examples**:

* [Image/Video Selection Sequence](/examples/workflows_2/05-workflows-conditional-branching/selector_for_image_video_generation_pipelines)


