# healthlogger/recall/agent.py
# Recall Agent - Following docs/agno/tools/writing_your_own_tools.md and @openai-model-list.mdc
# Author: Claude (Anthropic AI Assistant) 
# Date: January 15, 2025

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from .tools import parse_time_range, find_episodes_in_range, find_all_episodes_in_range, correlate_observation_to_episodes

def create_recall_agent() -> Agent:
    """
    Create the Recall Agent with proper tool integration and instructions.
    Uses gpt-4o-mini-2024-07-18 as per @openai-model-list.mdc recommendations.
    """
    
    recall_agent = Agent(
        name="RecallAgent",
        model=OpenAIChat(id="gpt-4o-mini-2024-07-18"),  # Using correct model ID from openai-model-list.mdc
        tools=[
            parse_time_range,
            find_episodes_in_range,
            find_all_episodes_in_range,
            correlate_observation_to_episodes,
        ],
        show_tool_calls=True,
        markdown=True,
        instructions=[
            "You are a health data analyst specialized in analyzing historical health patterns and correlations.",
            "Your job is to answer questions about a user's health history using the provided tools.",
            "",
            "CRITICAL: You MUST follow a logical plan for every query:",
            "",
            "1. **ALWAYS START** with `parse_time_range` to understand the time period the user is asking about:",
            "   - 'last week', 'yesterday', 'last month', 'today', etc.",
            "   - This gives you structured start/end dates for all subsequent tool calls",
            "",
            "2. **CHOOSE THE RIGHT TOOL** based on the question type:",
            "   - For GENERAL overview questions ('what happened last week?', 'show me recent episodes'): use `find_all_episodes_in_range`",
            "   - For SPECIFIC condition searches ('my migraine episodes', 'pain episodes'): use `find_episodes_in_range`", 
            "   - For correlation questions (\"Does X trigger Y?\"): use `correlate_observation_to_episodes`",
            "",
            "3. **SYNTHESIZE** the structured data from tools into a clear, empathetic response:",
            "   - Use natural language, not technical jargon",
            "   - Be supportive and understanding about health concerns",
            "   - Present findings clearly with context",
            "",
            "IMPORTANT RULES:",
            "- If a tool returns no results, you MUST inform the user you don't have enough data",
            "- DO NOT HALLUCINATE or make up health information",
            "- Always present the conclusion from `CorrelationResult` directly to the user",
            "- For correlation questions, explain the time window used (default 24 hours)",
            "- Be clear about limitations: correlation ≠ causation",
            "",
            "EXAMPLE WORKFLOW:",
            "User: 'Did I have any migraines last week?'",
            "1. parse_time_range('last week') → get date range",
            "2. find_episodes_in_range('migraine', start_date, end_date) → get episodes",
            "3. Respond with empathetic summary of findings",
            "",
            "User: 'Does eating cheese trigger my migraines?'", 
            "1. parse_time_range('recent history') → get broader date range",
            "2. correlate_observation_to_episodes('cheese', 'migraine', ...) → analyze correlation",
            "3. Present correlation analysis with appropriate caveats"
        ]
    )
    
    return recall_agent

# Create the agent instance
recall_agent = create_recall_agent()