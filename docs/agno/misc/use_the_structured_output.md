---
title: Use the structured output
category: misc
source_lines: 2400-2462
line_count: 62
---

# Use the structured output
MovieScript(
│   setting='In the bustling streets and iconic skyline of New York City.',
│   ending='Isabella and Alex, having narrowly escaped the clutches of the Syndicate, find themselves standing at the top of the Empire State Building. As the glow of the setting sun bathes the city, they share a victorious kiss. Newly emboldened and as an unstoppable duo, they vow to keep NYC safe from any future threats.',
│   genre='Action Thriller',
│   name='The NYC Chronicles',
│   characters=['Isabella Grant', 'Alex Chen', 'Marcus Kane', 'Detective Ellie Monroe', 'Victor Sinclair'],
│   storyline='Isabella Grant, a fearless investigative journalist, uncovers a massive conspiracy involving a powerful syndicate plotting to control New York City. Teaming up with renegade cop Alex Chen, they must race against time to expose the culprits before the city descends into chaos. Dodging danger at every turn, they fight to protect the city they love from imminent destruction.'
)
```

## Using a Parser Model

You can use an additional model to parse and structure the output from your primary model. This approach is particularly effective when the primary model is optimized for reasoning tasks, as such models may not consistently produce detailed structured responses.

```python
agent = Agent(
    model=Claude(id="claude-sonnet-4-20250514"),
    description="You write movie scripts.",
    response_model=MovieScript,
    parser_model=OpenAIChat(id="gpt-4o"),
)
```

You can also provide a custom `parser_model_prompt` to your Parser Model.

## Streaming Structured Output

Streaming can be used in combination with `response_model`. This returns the structured output as a single event in the stream of events.

```python streaming_agent.py
import asyncio
from typing import Dict, List

from agno.agent import Agent
from agno.models.openai.chat import OpenAIChat
from pydantic import BaseModel, Field


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
    rating: Dict[str, int] = Field(
        ...,
        description="Your own rating of the movie. 1-10. Return a dictionary with the keys 'story' and 'acting'.",
    )


