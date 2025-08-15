from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.tools.reasoning import ReasoningTools
from agno.tools.yfinance import YFinanceTools

# Claude with reasoning tools for complex analysis
reasoning_agent = Agent(
    model=Claude(id="claude-3-7-sonnet-latest"),
    tools=[
        ReasoningTools(
            think=True,
            analyze=True,
            add_instructions=True,
        ),
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            company_info=True,
        ),
    ],
    instructions="Use structured reasoning for complex problems",
    stream_intermediate_steps=True,
    show_tool_calls=True,
    markdown=True,
)

# This question will trigger multiple intermediate steps
response_stream = reasoning_agent.run(
    "What is the stock price of NVDA and should I invest in it? "
    "Consider market trends, financial health, and risk factors.",
    stream=True,
    stream_intermediate_steps=True
)

# for chunk in response_stream:
#     print(chunk)
#     print("---" * 20)

# response_stream = agent.run("Your prompt", stream=True, stream_intermediate_steps=True)

for event in response_stream:
    if event.event == "RunResponseContent":
        print(f"Content: {event.content}")
    elif event.event == "ToolCallStarted":
        print(f"Tool call started: {event.tool}")
    elif event.event == "ReasoningStep":
        print(f"Reasoning step: {event.content}")
    ...