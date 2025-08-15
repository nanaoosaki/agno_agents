---
title: Selector for Image Video Generation Pipelines
category: misc
source_lines: 56065-56099
line_count: 34
---

# Selector for Image Video Generation Pipelines
Source: https://docs.agno.com/examples/workflows_2/05-workflows-conditional-branching/selector_for_image_video_generation_pipelines

This example demonstrates **Workflows 2.0** router pattern for dynamically selecting between image and video generation pipelines.

This example demonstrates **Workflows 2.0** router pattern for dynamically selecting between image and video generation pipelines. It uses `Steps` to encapsulate each media type's workflow and a `Router` to intelligently choose the pipeline based on input analysis.

## Key Features:

* **Dynamic Routing**: Selects pipelines (`Steps`) based on input keywords (e.g., "image" or "video").
* **Modular Pipelines**: Encapsulates image/video workflows as reusable `Steps` objects.
* **Structured Inputs**: Uses Pydantic models for type-safe configuration (e.g., resolution, style).

## Key Features:

* **Nested Logic**: Embeds `Condition` and `Parallel` within a `Steps` sequence.
* **Topic-Specialized Research**: Uses `Condition` to trigger parallel tech/news research for tech topics.
* **Modular Design**: Encapsulates the entire workflow as a reusable `Steps` object.

```python selector_for_image_video_generation_pipelines.py
rom typing import Any, Dict, List, Optional

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.models.gemini import GeminiTools
from agno.tools.openai import OpenAITools
from agno.workflow.v2.router import Router
from agno.workflow.v2.step import Step
from agno.workflow.v2.steps import Steps
from agno.workflow.v2.types import StepInput
from agno.workflow.v2.workflow import Workflow
from pydantic import BaseModel


