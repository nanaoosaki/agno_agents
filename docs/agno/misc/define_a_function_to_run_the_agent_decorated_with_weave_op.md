---
title: Define a function to run the agent, decorated with weave.op()
category: misc
source_lines: 66482-66487
line_count: 5
---

# Define a function to run the agent, decorated with weave.op()
@weave.op()
def run(content: str):
    return agent.run(content)

