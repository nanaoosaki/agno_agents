---
title: Initialize LangDB tracing - must be called before creating agents
category: misc
source_lines: 65981-65988
line_count: 7
---

# Initialize LangDB tracing - must be called before creating agents
init()

from agno.agent import Agent
from agno.models.langdb import LangDB
from agno.tools.duckduckgo import DuckDuckGoTools

