---
title: Example usage with different types of travel queries
category: misc
source_lines: 7801-7810
line_count: 9
---

# Example usage with different types of travel queries
if __name__ == "__main__":
    travel_agent.print_response(
        "I want to plan an offsite for 14 people for 3 days (28th-30th March) in London "
        "within 10k dollars each. Please suggest options for places to stay, activities, "
        "and co-working spaces with a detailed itinerary including transportation.",
        stream=True,
    )

