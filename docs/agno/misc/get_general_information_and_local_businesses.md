---
title: Get general information and local businesses
category: misc
source_lines: 74638-74669
line_count: 31
---

# Get general information and local businesses
agent.print_response(
    """
    I'm traveling to Tokyo next month.
    1. Research the best time to visit and major attractions
    2. Find one good rated sushi restaurants near Shinjuku
    Compile a comprehensive travel guide with this information.
    """,
    markdown=True
)
```

## Toolkit Params

| Parameter         | Type                 | Default | Description                                                         |
| ----------------- | -------------------- | ------- | ------------------------------------------------------------------- |
| `apify_api_token` | `str`                | `None`  | Apify API token (or set via APIFY\_API\_TOKEN environment variable) |
| `actors`          | `str` or `List[str]` | `None`  | Single Actor ID or list of Actor IDs to register                    |

## Developer Resources

* View [Tools](https://github.com/agno-agi/agno/blob/main/libs/agno/agno/tools/apify.py)
* View [Cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/tools/apify_tools.py)

## Resources

* [Apify Actor Documentation](https://docs.apify.com/Actors)
* [Apify Store - Browse available Actors](https://apify.com/store)
* [How to build and monetize an AI agent on Apify](https://blog.apify.com/how-to-build-an-ai-agent/)


