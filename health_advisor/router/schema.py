# health_advisor/router/schema.py
# Following the router_agent_implementation_plan.md schema design

from pydantic import BaseModel, Field
from typing import List, Literal, Optional

class RouterDecision(BaseModel):
    """The structured output from the Router Agent."""
    primary_intent: Literal["log", "recall", "coach", "profile_update", "onboarding", "profile_view", "clarify_response", "control_action", "unknown"] = Field(
        ...,
        description="The primary intent of the user's message."
    )
    secondary_intent: Optional[Literal["log", "recall", "coach", "profile_update"]] = Field(
        None,
        description="A secondary intent if the user's message contains multiple requests (e.g., logging and then asking for advice)."
    )
    profile_action: Optional[Literal["start_onboarding", "update_profile", "view_profile", "edit_profile"]] = Field(
        None,
        description="Specific profile action when primary_intent is profile-related."
    )
    confidence: float = Field(
        ...,
        description="The confidence of the primary intent classification (0.0 to 1.0)."
    )
    rationale: str = Field(
        ...,
        description="A brief explanation for the chosen primary intent."
    )