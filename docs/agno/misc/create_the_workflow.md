---
title: Create the workflow
category: misc
source_lines: 82274-82322
line_count: 48
---

# Create the workflow
generate_blog_post = BlogPostGenerator(
    # Fix the session_id for this demo
    session_id="my-session-id",
    storage=SqliteWorkflowStorage(
        table_name="generate_blog_post_workflows",
        db_file="tmp/workflows.db",
    ),
)
```

Then in the `run()` method, you can read from and add to the `session_state` as needed.

```python

class BlogPostGenerator(Workflow):
    # ... agents
    def run(self, topic: str, use_cache: bool = True) -> Iterator[RunResponse]:
        # Read from the session state cache
        if use_cache and "blog_posts" in self.session_state:
            logger.info("Checking if cached blog post exists")
            for cached_blog_post in self.session_state["blog_posts"]:
                if cached_blog_post["topic"] == topic:
                    logger.info("Found cached blog post")
                    yield RunResponse(
                        run_id=self.run_id,
                        event=RunEvent.workflow_completed,
                        content=cached_blog_post["blog_post"],
                    )
                    return

        # ... generate the blog post

        # Save to session state for future runs
        if "blog_posts" not in self.session_state:
            self.session_state["blog_posts"] = []
        self.session_state["blog_posts"].append({"topic": topic, "blog_post": self.writer.run_response.content})
```

When the workflow starts, the `session_state` for that particular `session_id` is read from the database and when the workflow ends, the `session_state` is stored in the database.

<Tip>
  You can always call `self.write_to_storage()` to save the `session_state` to the database at any time. In case you need to abort the workflow but want to store the intermediate results.
</Tip>

View the [Blog Post Generator](/workflows/introduction#full-example-blog-post-generator) for an example of how to use session state for caching.


