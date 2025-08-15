---
title: Condition evaluator function
category: misc
source_lines: 54905-54922
line_count: 17
---

# Condition evaluator function
def is_tech_topic(step_input) -> bool:
    """Check if the topic is tech-related and needs specialized research"""
    message = step_input.message.lower() if step_input.message else ""
    tech_keywords = [
        "ai",
        "machine learning",
        "technology",
        "software",
        "programming",
        "tech",
        "startup",
        "blockchain",
    ]
    return any(keyword in message for keyword in tech_keywords)


