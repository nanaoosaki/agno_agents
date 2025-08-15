---
title: OpenBB
category: misc
source_lines: 76570-76584
line_count: 14
---

# OpenBB
Source: https://docs.agno.com/tools/toolkits/others/openbb



**OpenBBTools** enable an Agent to provide information about stocks and companies.

```python cookbook/tools/openbb_tools.py
from agno.agent import Agent
from agno.tools.openbb import OpenBBTools


agent = Agent(tools=[OpenBBTools()], debug_mode=True, show_tool_calls=True)

