---
title: Print team member message metrics
category: metrics
source_lines: 70015-70030
line_count: 15
---

# Print team member message metrics
print("---" * 5, "Team Member Message Metrics", "---" * 5)
if team.run_response.member_responses:
    for member_response in team.run_response.member_responses:
        if member_response.messages:
            for message in member_response.messages:
                if message.role == "assistant":
                    if message.content:
                        print(f"Message: {message.content}")
                    elif message.tool_calls:
                        print(f"Tool calls: {message.tool_calls}")
                    print("---" * 5, "Metrics", "---" * 5)
                    pprint(message.metrics)
                    print("---" * 20)

