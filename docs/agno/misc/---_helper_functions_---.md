---
title: --- Helper Functions ---
category: misc
source_lines: 83629-83791
line_count: 162
---

# --- Helper Functions ---
def get_cached_blog_post(workflow: Workflow, topic: str) -> Optional[str]:
    """Get cached blog post from workflow session state"""
    logger.info("Checking if cached blog post exists")
    return workflow.workflow_session_state.get("blog_posts", {}).get(topic)


def cache_blog_post(workflow: Workflow, topic: str, blog_post: str):
    """Cache blog post in workflow session state"""
    logger.info(f"Saving blog post for topic: {topic}")
    if "blog_posts" not in workflow.workflow_session_state:
        workflow.workflow_session_state["blog_posts"] = {}
    workflow.workflow_session_state["blog_posts"][topic] = blog_post


def get_cached_search_results(
    workflow: Workflow, topic: str
) -> Optional[SearchResults]:
    """Get cached search results from workflow session state"""
    logger.info("Checking if cached search results exist")
    search_results = workflow.workflow_session_state.get("search_results", {}).get(
        topic
    )
    if search_results and isinstance(search_results, dict):
        try:
            return SearchResults.model_validate(search_results)
        except Exception as e:
            logger.warning(f"Could not validate cached search results: {e}")
    return search_results if isinstance(search_results, SearchResults) else None


def cache_search_results(workflow: Workflow, topic: str, search_results: SearchResults):
    """Cache search results in workflow session state"""
    logger.info(f"Saving search results for topic: {topic}")
    if "search_results" not in workflow.workflow_session_state:
        workflow.workflow_session_state["search_results"] = {}
    workflow.workflow_session_state["search_results"][topic] = (
        search_results.model_dump()
    )


def get_cached_scraped_articles(
    workflow: Workflow, topic: str
) -> Optional[Dict[str, ScrapedArticle]]:
    """Get cached scraped articles from workflow session state"""
    logger.info("Checking if cached scraped articles exist")
    scraped_articles = workflow.workflow_session_state.get("scraped_articles", {}).get(
        topic
    )
    if scraped_articles and isinstance(scraped_articles, dict):
        try:
            return {
                url: ScrapedArticle.model_validate(article)
                for url, article in scraped_articles.items()
            }
        except Exception as e:
            logger.warning(f"Could not validate cached scraped articles: {e}")
    return scraped_articles if isinstance(scraped_articles, dict) else None


def cache_scraped_articles(
    workflow: Workflow, topic: str, scraped_articles: Dict[str, ScrapedArticle]
):
    """Cache scraped articles in workflow session state"""
    logger.info(f"Saving scraped articles for topic: {topic}")
    if "scraped_articles" not in workflow.workflow_session_state:
        workflow.workflow_session_state["scraped_articles"] = {}
    workflow.workflow_session_state["scraped_articles"][topic] = {
        url: article.model_dump() for url, article in scraped_articles.items()
    }


async def get_search_results(
    workflow: Workflow, topic: str, use_cache: bool = True, num_attempts: int = 3
) -> Optional[SearchResults]:
    """Get search results with caching support"""

    # Check cache first
    if use_cache:
        cached_results = get_cached_search_results(workflow, topic)
        if cached_results:
            logger.info(f"Found {len(cached_results.articles)} articles in cache.")
            return cached_results

    # Search for new results
    for attempt in range(num_attempts):
        try:
            print(
                f"🔍 Searching for articles about: {topic} (attempt {attempt + 1}/{num_attempts})"
            )
            response = await research_agent.arun(topic)

            if (
                response
                and response.content
                and isinstance(response.content, SearchResults)
            ):
                article_count = len(response.content.articles)
                logger.info(f"Found {article_count} articles on attempt {attempt + 1}")
                print(f"✅ Found {article_count} relevant articles")

                # Cache the results
                cache_search_results(workflow, topic, response.content)
                return response.content
            else:
                logger.warning(
                    f"Attempt {attempt + 1}/{num_attempts} failed: Invalid response type"
                )

        except Exception as e:
            logger.warning(f"Attempt {attempt + 1}/{num_attempts} failed: {str(e)}")

    logger.error(f"Failed to get search results after {num_attempts} attempts")
    return None


async def scrape_articles(
    workflow: Workflow,
    topic: str,
    search_results: SearchResults,
    use_cache: bool = True,
) -> Dict[str, ScrapedArticle]:
    """Scrape articles with caching support"""

    # Check cache first
    if use_cache:
        cached_articles = get_cached_scraped_articles(workflow, topic)
        if cached_articles:
            logger.info(f"Found {len(cached_articles)} scraped articles in cache.")
            return cached_articles

    scraped_articles: Dict[str, ScrapedArticle] = {}

    print(f"📄 Scraping {len(search_results.articles)} articles...")

    for i, article in enumerate(search_results.articles, 1):
        try:
            print(
                f"📖 Scraping article {i}/{len(search_results.articles)}: {article.title[:50]}..."
            )
            response = await content_scraper_agent.arun(article.url)

            if (
                response
                and response.content
                and isinstance(response.content, ScrapedArticle)
            ):
                scraped_articles[response.content.url] = response.content
                logger.info(f"Scraped article: {response.content.url}")
                print(f"✅ Successfully scraped: {response.content.title[:50]}...")
            else:
                print(f"❌ Failed to scrape: {article.title[:50]}...")

        except Exception as e:
            logger.warning(f"Failed to scrape {article.url}: {str(e)}")
            print(f"❌ Error scraping: {article.title[:50]}...")

    # Cache the scraped articles
    cache_scraped_articles(workflow, topic, scraped_articles)
    return scraped_articles


