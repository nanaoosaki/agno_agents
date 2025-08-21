"""
Specialized agents for the structured onboarding workflow.

This module provides helper functions to create step-specific agents
for the 6-step onboarding process with structured outputs.
"""

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from pydantic import BaseModel
from typing import Type, Optional
import os
from dotenv import load_dotenv

load_dotenv()

def create_onboarding_agent(prompt_context: str, response_model: Type[BaseModel], step_number: Optional[int] = None) -> Agent:
    """
    Create a specialized onboarding agent for a specific step.
    
    Args:
        prompt_context: Context-specific instructions for this step
        response_model: Pydantic model for structured output
        step_number: Optional step number for context
        
    Returns:
        Configured Agent instance
    """
    
    base_instructions = [
        "You are a compassionate health companion helping users set up their health profile.",
        "Your goal is to collect accurate, structured information while being supportive and empathetic.",
        "Ask clarifying questions if needed, but keep the conversation focused and moving forward.",
        "Be encouraging and normalize health challenges - many people deal with similar issues.",
        "If users seem hesitant to share something, reassure them about privacy and that all fields are optional.",
    ]
    
    step_specific_instructions = [
        prompt_context,
        "Extract the information into the required structured format.",
        "If the user doesn't provide complete information, use what they give you and note gaps for later.",
    ]
    
    if step_number:
        step_specific_instructions.insert(0, f"This is step {step_number} of the 6-step onboarding process.")
    
    all_instructions = base_instructions + step_specific_instructions
    
    return Agent(
        model=OpenAIChat(
            id="gpt-4o-mini-2024-07-18",
            api_key=os.getenv("OPENAI_API_KEY")
        ),
        name=f"OnboardingStep{step_number}Agent" if step_number else "OnboardingAgent",
        instructions=all_instructions,
        response_model=response_model,
        markdown=True
    )

def create_conditions_agent():
    """Create agent for Step 1: Health Conditions."""
    from data.schemas import OnboardingConditions
    
    return create_onboarding_agent(
        prompt_context="""Ask about the health conditions they are currently managing or want to track. 
        Common conditions include migraines, back pain, anxiety, depression, arthritis, diabetes, etc.
        Also try to identify which condition is most concerning or primary for them.
        Encourage them to include any condition that affects their daily life.""",
        response_model=OnboardingConditions,
        step_number=1
    )

def create_goals_agent():
    """Create agent for Step 2: Health Goals."""
    from data.schemas import OnboardingGoals
    
    return create_onboarding_agent(
        prompt_context="""Ask about their primary health management goals. 
        This could include reducing symptoms, better tracking, medication management, 
        lifestyle improvements, or preparing for doctor visits.
        Also ask about any specific, measurable targets they have.""",
        response_model=OnboardingGoals,
        step_number=2
    )

def create_symptoms_agent():
    """Create agent for Step 3: Symptoms and Patterns."""
    from data.schemas import OnboardingSymptoms
    
    return create_onboarding_agent(
        prompt_context="""Ask about the symptoms they experience with their conditions.
        Try to organize symptoms by condition when possible.
        Also ask about any patterns they've noticed - triggers, timing, severity changes.
        Help them think about environmental, dietary, stress, or other potential triggers.""",
        response_model=OnboardingSymptoms,
        step_number=3
    )

def create_medications_agent():
    """Create agent for Step 4: Medications and Treatments."""
    from data.schemas import OnboardingMedications
    
    return create_onboarding_agent(
        prompt_context="""Ask about current medications, including dosages and schedules if they're comfortable sharing.
        Also ask about any allergies to medications, foods, or other substances.
        Include any non-medication treatments like physical therapy, counseling, etc.
        Remind them this helps with tracking interactions and effectiveness.""",
        response_model=OnboardingMedications,
        step_number=4
    )

def create_routines_agent():
    """Create agent for Step 5: Daily Routines and Lifestyle."""
    from data.schemas import OnboardingRoutines
    
    return create_onboarding_agent(
        prompt_context="""Ask about their daily health routines and lifestyle factors.
        This includes exercise habits, sleep patterns, stress management techniques,
        meal timing, supplement routines, or any other health-related habits.
        Focus on routines that might affect their health conditions.""",
        response_model=OnboardingRoutines,
        step_number=5
    )

def create_style_agent():
    """Create agent for Step 6: Communication and Preferences."""
    from data.schemas import OnboardingStyle
    
    return create_onboarding_agent(
        prompt_context="""Ask about their communication preferences and interaction style.
        Do they prefer detailed explanations or brief summaries? 
        Formal or casual tone? How much medical detail do they want?
        Also ask about notification preferences and privacy comfort level.""",
        response_model=OnboardingStyle,
        step_number=6
    )