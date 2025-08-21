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
    Create the multi-modal Extractor Agent with conversation history and vision support.
    This agent converts natural language and visual data to structured health data.
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
        
        # Comprehensive instructions with multi-modal and unified input support
        instructions=[
            get_extractor_system_prompt(),
            "CRITICAL CONTEXT: The user's message may be a combination of transcribed voice audio and typed text notes. The prompt will be formatted like: 'User said via voice: '...'. User typed: '...'.'",
            "You must synthesize information from ALL parts of the prompt (voice, text, and any attached images) to create a single, comprehensive log entry.",
            "IMPORTANT: You must analyze the user's LATEST message and ANY ATTACHED IMAGES in context of the chat history.",
            "Look for continuity signals like 'still', 'now', 'it', 'the pain' that refer to previous messages.",
            "When in doubt about episode linking, use 'unknown' and let deterministic rules decide.",
            "Always include the original user input (both voice and text) in fields.notes.",
            "",
            "# MULTI-MODAL IMAGE ANALYSIS INSTRUCTIONS:",
            "",
            "If images are attached, their metadata (like tags) will be in the prompt. Prioritize your analysis based on these tags:",
            "",
            "**For MedLabel tagged images:**",
            "- Extract the medication name, strength/dosage, and frequency from prescription labels",
            "- Look for active ingredients, NDC numbers, prescriber information",
            "- Note any warnings, side effects, or special instructions",
            "- Record the pharmacy name and prescription number if visible",
            "",
            "**For Food tagged images:**", 
            "- Extract key nutrition facts: calories, sugar, sodium, carbohydrates, protein, fat",
            "- Note serving size and number of servings per container",
            "- Identify allergen information and ingredients list",
            "- Look for added vitamins, minerals, or supplements",
            "",
            "**For all images:**",
            "- Describe what you see and incorporate details into the 'notes' field",
            "- If text in the image contradicts user's spoken text, TRUST THE IMAGE and note the discrepancy",
            "- If an image is blurry, unclear, or unreadable, state this and set confidence score lower",
            "- Extract any visible dates, batch numbers, or expiration dates",
            "",
            "**Image Analysis Priority:**",
            "1. First, analyze the text content for health information",
            "2. Then, examine attached images for additional or correcting information", 
            "3. Combine insights from both sources into a comprehensive health log entry",
            "4. Use image data to verify or correct text-based information",
            "5. Note any discrepancies between text and image data in your rationale"
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