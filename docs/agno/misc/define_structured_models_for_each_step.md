---
title: Define structured models for each step
category: misc
source_lines: 57008-57056
line_count: 48
---

# Define structured models for each step
class ResearchFindings(BaseModel):
    """Structured research findings with key insights"""

    topic: str = Field(description="The research topic")
    key_insights: List[str] = Field(description="Main insights discovered", min_items=3)
    trending_technologies: List[str] = Field(
        description="Technologies that are trending", min_items=2
    )
    market_impact: str = Field(description="Potential market impact analysis")
    sources_count: int = Field(description="Number of sources researched")
    confidence_score: float = Field(
        description="Confidence in findings (0.0-1.0)", ge=0.0, le=1.0
    )


class ContentStrategy(BaseModel):
    """Structured content strategy based on research"""

    target_audience: str = Field(description="Primary target audience")
    content_pillars: List[str] = Field(description="Main content themes", min_items=3)
    posting_schedule: List[str] = Field(description="Recommended posting schedule")
    key_messages: List[str] = Field(
        description="Core messages to communicate", min_items=3
    )
    hashtags: List[str] = Field(description="Recommended hashtags", min_items=5)
    engagement_tactics: List[str] = Field(
        description="Ways to increase engagement", min_items=2
    )


class FinalContentPlan(BaseModel):
    """Final content plan with specific deliverables"""

    campaign_name: str = Field(description="Name for the content campaign")
    content_calendar: List[str] = Field(
        description="Specific content pieces planned", min_items=6
    )
    success_metrics: List[str] = Field(
        description="How to measure success", min_items=3
    )
    budget_estimate: str = Field(description="Estimated budget range")
    timeline: str = Field(description="Implementation timeline")
    risk_factors: List[str] = Field(
        description="Potential risks and mitigation", min_items=2
    )


