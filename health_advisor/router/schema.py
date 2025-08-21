# health_advisor/router/schema.py
# Following the developer_mode_implementation_plan.md enhanced schema design

from pydantic import BaseModel, Field
from typing import List, Literal, Optional, Dict, Any

class RouterDecision(BaseModel):
    """Enhanced structured output from the Router Agent with secondary intents and control flow."""
    primary: Literal["log", "recall", "coach", "profile", "unknown"] = Field(
        ...,
        description="The primary intent of the user's message."
    )
    secondary: Optional[Literal["log", "recall", "coach", "profile", "none"]] = Field(
        default="none",
        description="A secondary intent for combo utterances (e.g., 'I have a migraine—what should I do?' → log + coach)."
    )
    control: Literal["none", "clarify", "action_confirm"] = Field(
        default="none",
        description="Control flow indicators: clarify for ambiguous input, action_confirm for pending approvals."
    )
    targets: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Optional routing targets like episode_id or condition if the Router can infer them."
    )
    confidence: float = Field(
        ...,
        description="The confidence of the primary intent classification (0.0 to 1.0)."
    )
    rationale: str = Field(
        ...,
        description="A brief explanation for the chosen primary intent and routing decision."
    )

# Legacy support for existing router implementations
class SimpleRouterDecision(BaseModel):
    """Simplified router decision for backward compatibility."""
    primary_intent: Literal["log", "recall", "coach", "profile", "unknown"] = Field(
        ...,
        description="The primary intent of the user's message."
    )
    confidence: float = Field(
        ...,
        description="The confidence of the intent classification (0.0 to 1.0)."
    )
    rationale: str = Field(
        ...,
        description="A brief explanation for the chosen intent."
    )