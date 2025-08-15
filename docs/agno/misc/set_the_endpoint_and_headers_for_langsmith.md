---
title: Set the endpoint and headers for LangSmith
category: misc
source_lines: 66265-66272
line_count: 7
---

# Set the endpoint and headers for LangSmith
endpoint = "https://eu.api.smith.langchain.com/otel/v1/traces"
headers = {
    "x-api-key": os.getenv("LANGSMITH_API_KEY"),
    "Langsmith-Project": os.getenv("LANGSMITH_PROJECT"),
}

