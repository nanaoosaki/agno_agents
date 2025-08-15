---
title: Structured Output Agent
category: misc
source_lines: 49490-49526
line_count: 36
---

# Structured Output Agent
Source: https://docs.agno.com/examples/models/xai/structured_output



## Code

```python cookbook/models/xai/structured_output.py
import asyncio
from typing import List

from agno.agent import Agent
from agno.models.xai import xAI
from agno.run.response import RunResponse
from pydantic import BaseModel, Field


class MovieScript(BaseModel):
    name: str = Field(..., description="Give a name to this movie")
    setting: str = Field(
        ..., description="Provide a nice setting for a blockbuster movie."
    )
    ending: str = Field(
        ...,
        description="Ending of the movie. If not available, provide a happy ending.",
    )
    genre: str = Field(
        ...,
        description="Genre of the movie. If not available, select action, thriller or romantic comedy.",
    )
    characters: List[str] = Field(..., description="Name of characters for this movie.")
    storyline: str = Field(
        ..., description="3 sentence storyline for the movie. Make it exciting!"
    )


