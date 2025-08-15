---
title: --- Workflow Definition ---
category: misc
source_lines: 83881-83937
line_count: 56
---

# --- Workflow Definition ---
blog_generator_workflow = Workflow(
    name="Blog Post Generator v2.0",
    description="Advanced blog post generator with research and content creation capabilities",
    storage=SqliteStorage(
        table_name="blog_generator_v2",
        db_file="tmp/blog_generator_v2.db",
        mode="workflow_v2",
    ),
    steps=blog_generation_execution,
    workflow_session_state={},  # Initialize empty session state for caching
)


if __name__ == "__main__":
    import random

    async def main():
        # Fun example topics to showcase the generator's versatility
        example_topics = [
            "The Rise of Artificial General Intelligence: Latest Breakthroughs",
            "How Quantum Computing is Revolutionizing Cybersecurity",
            "Sustainable Living in 2024: Practical Tips for Reducing Carbon Footprint",
            "The Future of Work: AI and Human Collaboration",
            "Space Tourism: From Science Fiction to Reality",
            "Mindfulness and Mental Health in the Digital Age",
            "The Evolution of Electric Vehicles: Current State and Future Trends",
            "Why Cats Secretly Run the Internet",
            "The Science Behind Why Pizza Tastes Better at 2 AM",
            "How Rubber Ducks Revolutionized Software Development",
        ]

        # Test with a random topic
        topic = random.choice(example_topics)

        print("🧪 Testing Blog Post Generator v2.0")
        print("=" * 60)
        print(f"📝 Topic: {topic}")
        print()

        # Generate the blog post
        resp = await blog_generator_workflow.arun(
            topic=topic,
            use_search_cache=True,
            use_scrape_cache=True,
            use_blog_cache=True,
        )

        pprint_run_response(resp, markdown=True, show_time=True)

    asyncio.run(main())
```

For more examples and advanced patterns, see [here](/examples/workflows_2). Each file demonstrates a specific pattern with detailed comments and real-world use cases.


