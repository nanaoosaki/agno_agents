---
title: Research Agent using Exa
category: misc
source_lines: 7337-7373
line_count: 36
---

# Research Agent using Exa
Source: https://docs.agno.com/examples/agents/research-agent-exa



This example shows how to create a sophisticated research agent that combines
academic search capabilities with scholarly writing expertise. The agent performs
thorough research using Exa's academic search, analyzes recent publications, and delivers
well-structured, academic-style reports on any topic.

Key capabilities:

* Advanced academic literature search
* Recent publication analysis
* Cross-disciplinary synthesis
* Academic writing expertise
* Citation management

Example prompts to try:

* "Explore recent advances in quantum machine learning"
* "Analyze the current state of fusion energy research"
* "Investigate the latest developments in CRISPR gene editing"
* "Research the intersection of blockchain and sustainable energy"
* "Examine recent breakthroughs in brain-computer interfaces"

## Code

```python research_agent_exa.py
from datetime import datetime
from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.exa import ExaTools

