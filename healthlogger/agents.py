# healthlogger/agents.py
# Agno agents for Health Logger v3

from typing import Optional

try:
    from agno.agent import Agent
    from agno.models.openai import OpenAIChat
    AGNO_AVAILABLE = True
except ImportError:
    AGNO_AVAILABLE = False
    Agent = object
    OpenAIChat = object

from healthlogger.schema_router import RouterOutput, SimpleRouterOutput
from data.schemas.episodes import ProcessingResult
from .prompts import get_extractor_system_prompt, get_reply_system_prompt

def create_extractor_agent():
    """
    Create the Extractor Agent with conversation history support.
    This agent converts natural language to structured health data.
    """
    if not AGNO_AVAILABLE:
        raise ImportError("Agno library not available")
    
    return Agent(
        name="HealthExtractorAgent",
        model=OpenAIChat(id="gpt-4o-mini-2024-07-18"),
        
        # KEY FIX: Enable conversation history
        add_history_to_messages=True,
        num_history_runs=5,  # Include last 5 conversation turns
        
        # Enforce structured output - use SimpleRouterOutput for OpenAI compatibility
        response_model=SimpleRouterOutput,
        
        # Comprehensive instructions
        instructions=[
            get_extractor_system_prompt(),
            "IMPORTANT: You must analyze the LATEST message in context of CHAT HISTORY.",
            "Look for continuity signals like 'still', 'now', 'it', 'the pain' that refer to previous messages.",
            "When in doubt about episode linking, use 'unknown' and let deterministic rules decide.",
            "Always include the original user text in fields.notes."
        ],
        
        # Disable markdown for structured output
        markdown=False,
        
        # Don't show tool calls in this agent
        show_tool_calls=False
    )

def create_reply_agent():
    """
    Create the Reply Agent for user-friendly responses.
    This agent converts processing results to natural language.
    """
    if not AGNO_AVAILABLE:
        raise ImportError("Agno library not available")
    
    return Agent(
        name="HealthReplyAgent", 
        model=OpenAIChat(id="gpt-4o-mini-2024-07-18"),
        
        # No history needed - just process current result
        add_history_to_messages=False,
        
        # Instructions for empathetic responses
        instructions=[
            get_reply_system_prompt(),
            "Convert the structured processing result into a warm, empathetic response.",
            "Be supportive and show you understand their health situation.",
            "Keep responses brief but caring."
        ],
        
        # Enable markdown for nice formatting
        markdown=True,
        
        # Don't show tool calls
        show_tool_calls=False
    )