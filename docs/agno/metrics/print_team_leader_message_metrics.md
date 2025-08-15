---
title: Print team leader message metrics
category: metrics
source_lines: 69994-70007
line_count: 13
---

# Print team leader message metrics
print("---" * 5, "Team Leader Message Metrics", "---" * 5)
if team.run_response.messages:
    for message in team.run_response.messages:
        if message.role == "assistant":
            if message.content:
                print(f"Message: {message.content}")
            elif message.tool_calls:
                print(f"Tool calls: {message.tool_calls}")
            print("---" * 5, "Metrics", "---" * 5)
            pprint(message.metrics)
            print("---" * 20)

