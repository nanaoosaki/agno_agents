---
title: File Upload
category: misc
source_lines: 36861-36928
line_count: 67
---

# File Upload
Source: https://docs.agno.com/examples/models/anthropic/file_upload

Learn how to use Anthropic's Files API with Agno.

With Anthropic's [Files API](https://docs.anthropic.com/en/docs/build-with-claude/files), you can upload files and later reference them in other API calls.
This is handy when a file is referenced multiple times in the same flow.

## Usage

<Steps>
  <Step title="Upload a file">
    Initialize the Anthropic client and use `client.beta.files.upload`:

    ```python
    from anthropic import Anthropic

    file_path = Path("path/to/your/file.pdf")

    client = Anthropic()
    uploaded_file = client.beta.files.upload(file=file_path)
    ```
  </Step>

  <Step title="Initialize the Claude model">
    When initializing the `Claude` model, pass the necessary beta header:

    ```python
    from agno.agent import Agent
    from agno.models.anthropic import Claude

    agent = Agent(
        model=Claude(
            id="claude-opus-4-20250514",
            default_headers={"anthropic-beta": "files-api-2025-04-14"},
        )
    )
    ```
  </Step>

  <Step title="Reference the file">
    You can now reference the uploaded file when interacting with your Agno agent:

    ```python
    agent.print_response(
        "Summarize the contents of the attached file.",
        files=[File(external=uploaded_file)],
    )
    ```
  </Step>
</Steps>

Notice there are some storage limits attached to this feature. You can read more about that on Anthropic's [docs](https://docs.anthropic.com/en/docs/build-with-claude/files#file-storage-and-limits).

## Working example

```python cookbook/models/anthropic/pdf_input_file_upload.py
from pathlib import Path

from agno.agent import Agent
from agno.media import File
from agno.models.anthropic import Claude
from agno.utils.media import download_file
from anthropic import Anthropic

pdf_path = Path(__file__).parent.joinpath("ThaiRecipes.pdf")

