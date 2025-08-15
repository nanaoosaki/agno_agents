---
title: Startup Idea Validator
category: misc
source_lines: 58049-58095
line_count: 46
---

# Startup Idea Validator
Source: https://docs.agno.com/examples/workflows_2/startup-idea-validator

This example demonstrates how to migrate from the similar workflows 1.0 example to workflows 2.0 structure.

This workflow helps entrepreneurs validate their startup ideas by:

1. Clarifying and refining the core business concept
2. Evaluating originality compared to existing solutions
3. Defining clear mission and objectives
4. Conducting comprehensive market research and analysis

**Why is this helpful:**

* Get objective feedback on your startup idea before investing resources
* Understand your total addressable market and target segments
* Validate assumptions about market opportunity and competition
* Define clear mission and objectives to guide execution

**Example use cases:**

* New product/service validation
* Market opportunity assessment
* Competitive analysis
* Business model validation
* Target customer segmentation
* Mission/vision refinement

Run `pip install openai agno googlesearch-python` to install dependencies.

The workflow will guide you through validating your startup idea with AI-powered
analysis and research. Use the insights to refine your concept and business plan!

```python startup_idea_validator.py
import asyncio
from typing import Any

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.googlesearch import GoogleSearchTools
from agno.utils.pprint import pprint_run_response
from agno.workflow.v2.types import WorkflowExecutionInput
from agno.workflow.v2.workflow import Workflow
from pydantic import BaseModel, Field


