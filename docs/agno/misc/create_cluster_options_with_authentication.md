---
title: Create cluster options with authentication
category: misc
source_lines: 80384-80409
line_count: 25
---

# Create cluster options with authentication
auth = PasswordAuthenticator(username, password)
cluster_options = ClusterOptions(auth)
cluster_options.apply_profile(KnownConfigProfiles.WanDevelopment)


knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=CouchbaseSearch(
        bucket_name="recipe_bucket",
        scope_name="recipe_scope",
        collection_name="recipes",
        couchbase_connection_string=connection_string,
        cluster_options=cluster_options,
        search_index="vector_search_fts_index",
        embedder=OpenAIEmbedder(
            id="text-embedding-3-large", 
            dimensions=3072, 
            api_key=os.getenv("OPENAI_API_KEY")
        ),
        wait_until_index_ready=60,
        overwrite=True
    ),
)

