---
title: Example usage with a famous landmark
category: misc
source_lines: 35182-35193
line_count: 11
---

# Example usage with a famous landmark
agent.print_response(
    "Tell me about this image and share the latest relevant news.",
    images=[
        Image(
            url="https://upload.wikimedia.org/wikipedia/commons/0/0c/GoldenGateBridge-001.jpg"
        )
    ],
    stream=True,
)

