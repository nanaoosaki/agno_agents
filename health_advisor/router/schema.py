# health_advisor/router/schema.py
# Following the router_agent_implementation_plan.md schema design

from pydantic import BaseModel, Field
from typing import List, Literal, Optional

class RouterDecision(BaseModel):
    """The structured output from the Router Agent."""
    primary_intent: Literal["log", "recall", "coach", "clarify_response", "control_action", "unknown"] = Field(
        ...,
        description="The primary intent of the user's message."
    )
    secondary_intent: Optional[Literal["log", "recall", "coach"]] = Field(
        None,
        description="A secondary intent if the user's message contains multiple requests (e.g., logging and then asking for advice)."
    )
    confidence: float = Field(
        ...,
        description="The confidence of the primary intent classification (0.0 to 1.0)."
    )
    rationale: str = Field(
        ...,
        description="A brief explanation for the chosen primary intent."
    )