---
title: Agent with Structured Output
category: misc
source_lines: 43240-43281
line_count: 41
---

# Agent with Structured Output
Source: https://docs.agno.com/examples/models/ibm/structured_output



## Code

```python cookbook/models/ibm/watsonx/structured_output.py
from typing import List

from agno.agent import Agent, RunResponse
from agno.models.ibm import WatsonX
from pydantic import BaseModel, Field
from rich.pretty import pprint


class MovieScript(BaseModel):
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
    name: str = Field(..., description="Give a name to this movie")
    characters: List[str] = Field(..., description="Name of characters for this movie.")
    storyline: str = Field(
        ..., description="3 sentence storyline for the movie. Make it exciting!"
    )


movie_agent = Agent(
    model=WatsonX(id="ibm/granite-20b-code-instruct"),
    description="You help people write movie scripts.",
    response_model=MovieScript,
)

