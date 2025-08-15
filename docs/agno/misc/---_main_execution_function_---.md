---
title: --- Main Execution Function ---
category: misc
source_lines: 83791-83881
line_count: 90
---

# --- Main Execution Function ---
async def blog_generation_execution(
    workflow: Workflow,
    topic: str = None,
    use_search_cache: bool = True,
    use_scrape_cache: bool = True,
    use_blog_cache: bool = True,
) -> str:
    """
    Blog post generation workflow execution function.

    Args:
        workflow: The workflow instance
        execution_input: Standard workflow execution input
        topic: Blog post topic (if not provided, uses execution_input.message)
        use_search_cache: Whether to use cached search results
        use_scrape_cache: Whether to use cached scraped articles
        use_blog_cache: Whether to use cached blog posts
        **kwargs: Additional parameters
    """

    blog_topic = topic

    if not blog_topic:
        return "❌ No blog topic provided. Please specify a topic."

    print(f"🎨 Generating blog post about: {blog_topic}")
    print("=" * 60)

    # Check for cached blog post first
    if use_blog_cache:
        cached_blog = get_cached_blog_post(workflow, blog_topic)
        if cached_blog:
            print("📋 Found cached blog post!")
            return cached_blog

    # Phase 1: Research and gather sources
    print(f"\n🔍 PHASE 1: RESEARCH & SOURCE GATHERING")
    print("=" * 50)

    search_results = await get_search_results(workflow, blog_topic, use_search_cache)

    if not search_results or len(search_results.articles) == 0:
        return f"❌ Sorry, could not find any articles on the topic: {blog_topic}"

    print(f"📊 Found {len(search_results.articles)} relevant sources:")
    for i, article in enumerate(search_results.articles, 1):
        print(f"   {i}. {article.title[:60]}...")

    # Phase 2: Content extraction
    print(f"\n📄 PHASE 2: CONTENT EXTRACTION")
    print("=" * 50)

    scraped_articles = await scrape_articles(
        workflow, blog_topic, search_results, use_scrape_cache
    )

    if not scraped_articles:
        return f"❌ Could not extract content from any articles for topic: {blog_topic}"

    print(f"📖 Successfully extracted content from {len(scraped_articles)} articles")

    # Phase 3: Blog post writing
    print(f"\n✍️ PHASE 3: BLOG POST CREATION")
    print("=" * 50)

    # Prepare input for the writer
    writer_input = {
        "topic": blog_topic,
        "articles": [article.model_dump() for article in scraped_articles.values()],
    }

    print("🤖 AI is crafting your blog post...")
    writer_response = await blog_writer_agent.arun(json.dumps(writer_input, indent=2))

    if not writer_response or not writer_response.content:
        return f"❌ Failed to generate blog post for topic: {blog_topic}"

    blog_post = writer_response.content

    # Cache the blog post
    cache_blog_post(workflow, blog_topic, blog_post)

    print("✅ Blog post generated successfully!")
    print(f"📝 Length: {len(blog_post)} characters")
    print(f"📚 Sources: {len(scraped_articles)} articles")

    return blog_post


