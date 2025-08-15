---
title: Define agents with response models
category: misc
source_lines: 82868-82881
line_count: 13
---

# Define agents with response models
research_agent = Agent(
    name="Research Specialist",
    model=OpenAIChat(id="gpt-4"),
    response_model=ResearchFindings,  # <-- Set on Agent
)

analysis_agent = Agent(
    name="Analysis Expert", 
    model=OpenAIChat(id="gpt-4"),
    response_model=AnalysisResults,  # <-- Set on Agent
)

