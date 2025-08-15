---
title: Sleep
category: misc
source_lines: 73996-74009
line_count: 13
---

# Sleep
Source: https://docs.agno.com/tools/toolkits/local/sleep



## Example

The following agent will use the `sleep` tool to pause execution for a given number of seconds.

```python cookbook/tools/sleep_tools.py
from agno.agent import Agent
from agno.tools.sleep import SleepTools

