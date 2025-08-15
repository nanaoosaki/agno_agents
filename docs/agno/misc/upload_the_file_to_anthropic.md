---
title: Upload the file to Anthropic
category: misc
source_lines: 36936-36957
line_count: 21
---

# Upload the file to Anthropic
uploaded_file = client.beta.files.upload(
    file=Path(pdf_path),
)

if uploaded_file is not None:
    agent = Agent(
        model=Claude(
            id="claude-opus-4-20250514",
            default_headers={"anthropic-beta": "files-api-2025-04-14"},
        ),
        markdown=True,
    )

    agent.print_response(
        "Summarize the contents of the attached file.",
        files=[File(external=uploaded_file)],
    )
```


