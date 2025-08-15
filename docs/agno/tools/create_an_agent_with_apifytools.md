---
title: Create an agent with ApifyTools
category: tools
source_lines: 74539-74551
line_count: 12
---

# Create an agent with ApifyTools
agent = Agent(
    tools=[
        ApifyTools(
            actors=["apify/rag-web-browser"],  # Specify which Apify Actors to use, use multiple ones if needed
            apify_api_token="your_apify_api_key"  # Or set the APIFY_API_TOKEN environment variable 
        )
    ],
    show_tool_calls=True,
    markdown=True
)

