from typing import List

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.hackernews import HackerNewsTools
from pydantic import BaseModel, Field

#load environment variables
from dotenv import load_dotenv
load_dotenv()
import os


class ResearchTopic(BaseModel):
    """Structured research topic with specific requirements"""

    topic: str
    focus_areas: List[str] = Field(description="Specific areas to focus on")
    target_audience: str = Field(description="Who this research is for")
    sources_required: int = Field(description="Number of sources needed", default=5)


# Define agents
hackernews_agent = Agent(
    name="Hackernews Agent",
    model=OpenAIChat(id="gpt-4o-mini-2024-07-18", api_key=os.getenv("OPENAI_API_KEY")),
    tools=[HackerNewsTools()],
    role="Extract key insights and content from Hackernews posts",
)

hackernews_agent.print_response(
    message=ResearchTopic(
        topic="AI",
        focus_areas=["AI", "Machine Learning"],
        target_audience="Developers",
        sources_required=5,
    )
)