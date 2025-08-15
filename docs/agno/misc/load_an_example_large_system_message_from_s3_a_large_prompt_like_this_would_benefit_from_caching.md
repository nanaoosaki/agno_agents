---
title: Load an example large system message from S3. A large prompt like this would benefit from caching.
category: misc
source_lines: 37421-37442
line_count: 21
---

# Load an example large system message from S3. A large prompt like this would benefit from caching.
txt_path = Path(__file__).parent.joinpath("system_promt.txt")
download_file(
    "https://agno-public.s3.amazonaws.com/prompts/system_promt.txt",
    str(txt_path),
)
system_message = txt_path.read_text()

agent = Agent(
    model=Claude(
        id="claude-sonnet-4-20250514",
        default_headers={"anthropic-beta": "extended-cache-ttl-2025-04-11"}, # Set the beta header to use the extended cache time
        system_prompt=system_message,
        cache_system_prompt=True,  # Activate prompt caching for Anthropic to cache the system prompt
        extended_cache_time=True,  # Extend the cache time from the default to 1 hour
    ),
    system_message=system_message,
    markdown=True,
)


