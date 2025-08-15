from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.reasoning import ReasoningTools
#load environment variables
from dotenv import load_dotenv
load_dotenv()
import os


# Gemini with structured reasoning
reasoning_agent = Agent(
    model=Gemini(id="gemini-2.5-pro-preview-03-25", api_key=os.getenv("GEMINI_API_KEY")),
    tools=[
        ReasoningTools(
            think=True,
            analyze=True,
            add_instructions=True,
        )
    ],
    instructions="Use structured reasoning for complex problems",
    stream_intermediate_steps=True,
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

# Stream with intermediate steps for your lion story
response_stream = reasoning_agent.run(
    "Tell me a 5 second short story about a lion",
    stream=True,
    stream_intermediate_steps=True
)

for chunk in response_stream:
    print(chunk)
    print("---" * 20)