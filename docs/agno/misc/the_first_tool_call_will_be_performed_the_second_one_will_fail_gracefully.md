---
title: The first tool call will be performed. The second one will fail gracefully.
category: misc
source_lines: 73068-73082
line_count: 14
---

# The first tool call will be performed. The second one will fail gracefully.
agent.print_response(
    "Find me the current price of TSLA, then after that find me the latest news about Tesla.",
    stream=True,
)

```

## To consider

* If the Agent tries to run a number of tool calls that exceeds the limit **all at once**, the limit will remain effective. Only as many tool calls as allowed will be performed.
* The limit is enforced **across a full run**, and not per individual requests triggered by the Agent.


