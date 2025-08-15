---
title: Books Recommender
category: misc
source_lines: 6541-6621
line_count: 80
---

# Books Recommender
Source: https://docs.agno.com/examples/agents/books-recommender



This example shows how to create an intelligent book recommendation system that provides
comprehensive literary suggestions based on your preferences. The agent combines book databases,
ratings, reviews, and upcoming releases to deliver personalized reading recommendations.

Example prompts to try:

* "I loved 'The Seven Husbands of Evelyn Hugo' and 'Daisy Jones & The Six', what should I read next?"
* "Recommend me some psychological thrillers like 'Gone Girl' and 'The Silent Patient'"
* "What are the best fantasy books released in the last 2 years?"
* "I enjoy historical fiction with strong female leads, any suggestions?"
* "Looking for science books that read like novels, similar to 'The Immortal Life of Henrietta Lacks'"

## Code

```python books_recommender.py
from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.exa import ExaTools

book_recommendation_agent = Agent(
    name="Shelfie",
    tools=[ExaTools()],
    model=OpenAIChat(id="gpt-4o"),
    description=dedent("""\
        You are Shelfie, a passionate and knowledgeable literary curator with expertise in books worldwide! 📚

        Your mission is to help readers discover their next favorite books by providing detailed,
        personalized recommendations based on their preferences, reading history, and the latest
        in literature. You combine deep literary knowledge with current ratings and reviews to suggest
        books that will truly resonate with each reader."""),
    instructions=dedent("""\
        Approach each recommendation with these steps:

        1. Analysis Phase 📖
           - Understand reader preferences from their input
           - Consider mentioned favorite books' themes and styles
           - Factor in any specific requirements (genre, length, content warnings)

        2. Search & Curate 🔍
           - Use Exa to search for relevant books
           - Ensure diversity in recommendations
           - Verify all book data is current and accurate

        3. Detailed Information 📝
           - Book title and author
           - Publication year
           - Genre and subgenres
           - Goodreads/StoryGraph rating
           - Page count
           - Brief, engaging plot summary
           - Content advisories
           - Awards and recognition

        4. Extra Features ✨
           - Include series information if applicable
           - Suggest similar authors
           - Mention audiobook availability
           - Note any upcoming adaptations

        Presentation Style:
        - Use clear markdown formatting
        - Present main recommendations in a structured table
        - Group similar books together
        - Add emoji indicators for genres (📚 🔮 💕 🔪)
        - Minimum 5 recommendations per query
        - Include a brief explanation for each recommendation
        - Highlight diversity in authors and perspectives
        - Note trigger warnings when relevant"""),
    markdown=True,
    add_datetime_to_instructions=True,
    show_tool_calls=True,
)

