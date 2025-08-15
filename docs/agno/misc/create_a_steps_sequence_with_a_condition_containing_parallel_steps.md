---
title: Create a Steps sequence with a Condition containing Parallel steps
category: misc
source_lines: 54954-54980
line_count: 26
---

# Create a Steps sequence with a Condition containing Parallel steps
article_creation_sequence = Steps(
    name="ArticleCreation",
    description="Complete article creation workflow from research to final edit",
    steps=[
        initial_research_step,
        # Condition with Parallel steps inside
        Condition(
            name="TechResearchCondition",
            description="If topic is tech-related, do specialized parallel research",
            evaluator=is_tech_topic,
            steps=[
                Parallel(
                    tech_research_step,
                    news_research_step,
                    name="SpecializedResearch",
                    description="Parallel tech and news research",
                ),
                content_prep_step,
            ],
        ),
        writing_step,
        editing_step,
    ],
)

