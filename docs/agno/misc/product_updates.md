---
title: Product updates
category: misc
source_lines: 3715-5316
line_count: 1601
---

# Product updates
Source: https://docs.agno.com/changelog/overview



<Update label="2025-08-08" description="v1.7.9">
  ## **Improvements:**

  * **Reranker in Hybrid Search**: Added support for Reranker in Pgvector hybrid search
  * **Output Model**: Added support for `stream_intermediate_steps` with output model
  * **PDF page split**: Refactor of PDF Readers and addition of Page Number Handling

  ## **Bug Fixes:**

  * **LanceDb Remote Connection**: Fixed a bug preventing connection to a remote LanceDb connection.
  * **Messages**: Fixed the order when using both `message` and `messages`.
</Update>

<Update label="2025-08-07" description="v1.7.8">
  ## Improvements:

  * **Support for OpenAI Flex Processing**: Added `service_tier` to `OpenAIChat` and `OpenAIResponses`.

  ## Bug Fixes:

  * **Print Response:**
    * Fixed `show_member_responses` not working correctly on `Team`
    * Fixed printing of MCP responses on streamable HTTP
  * **Session State on Team**: Fixed precedence for session state from sessions DB.
  * **`YouTubeTranscriptApi` has no attribute `get_transcript` :**
    * The `YoutubeTranscriptApi` is updated and now uses `.fetch(video_id)` for getting transcripts.
  * **HITL streaming:**
    * Added the required attributes- `tools_requiring_confirmation`, `tools_requiring_user_input`, `tools_awaiting_external_execution` on the class `BaseAgentRunResponseEvent`
    * If you are using streaming, it is recommended to pass the `run_id` and a list of `updated_tools` to the `continue_run` or `acontinue_run` method.
</Update>

<Update label="2025-08-01" description="v1.7.7">
  ## New Features:

  * **Updated MCP Tools:** Our \*\*\*\*`MCPTools` and `MultiMCPTools` classes can now be initialized and used without an async context manager, providing a much easier experience. See the updated [docs](https://docs.agno.com/tools/mcp/mcp).
  * **Morph Tools:** Morph’s Fast Apply model as a Tool, it intelligently merges your original code with update snippets at 98% accuracy and 4500+ tokens/second.

  ## Improvements:

  * **LiteLLM File & Image Understanding**: Added support for file and image inputs for `LiteLLM`.
  * **Upgrade ZepTools to v3 Zep**: `ZepTools` are now compatible with Zep v3.

  ## Bug Fixes:

  * **OpenAIEmbedder() wrong dimensions for text-embedding-3-large:** Automatically handles default `dimensions` length for `text-embedding-3-small` as 1536 and `text-embedding-3-large` as 3072.
</Update>

<Update label="2025-07-24" description="v1.7.6">
  ## New Features:

  * **Portkey Model Support**: Added support for Portkey hosted models.
  * **Bitbucket Tool**: Added `BitbucketTools` with a variety of Bitbucket repository actions.
  * **Jina Embedder:** Added `JinaEmbedder` for using embedding models via Jina.
  * **Row Chunking**: Added `RowChunking` as a CSV chunking strategy.
  * **EVM Toolkit**: Added `EvmTools` to do transactions on EVM compatible blockchains using `web3`.
  * **LinkUp Toolkit**: Added `LinkupTools` for powerful search.
  * **Background Execution Support for Workflows 2.0:** Introduced background execution capabilities for Workflows 2.0, enabling non-blocking workflow execution with polling support. See docs [here](https://docs.agno.com/workflows_2/background-execution).

  ## Improvements:

  * **Async Bedrock Support**: Added async execution support for the AWS bedrock implementation.
  * **PostgreSQL Tools Updates:** Various security and stability overhauls made to the `PostgresTools` toolkit.
  * **Daytona Toolkit Updates:** Added new tools for `Daytona`  agent Toolkit

  ## Bug Fixes:

  * **LiteLLM Metrics**: Fixed issue with metrics on streaming responses from LiteLLM.
  * **Team Expected Output**: Fixed issue where expected\_output of members were overwritten by the team leader agent.
  * **Workflows Async Generators**: Fixed how async generator `arun` functions are treated. It now correctly keeps async generators as async generators and doesn't convert it to a coroutine.
    * **Before:** Workflows with Async generator `arun` functions were incorrectly awaited as coroutines, which could cause runtime errors or prevent proper iteration through the yielded asynchronous values.
    * **After:** Async generator workflows are now properly recognised and handled as async generators, allowing for correct iteration over their yielded values using `async for`. This ensures all yielded results are processed as intended within asynchronous workflows.
  * **LiteLLM Multiple Streaming Tool Calls:** When Agno is run through LiteLLM against OpenAI chat models (eg. GPT4.1), multiple streamed tool\_calls lost their individual argument streams. This has been resolved.
</Update>

<Update label="2025-07-17" description="v1.7.5">
  ## New Features:

  * **SurrealDB:** Added SurrealDB support as a vector DB for knowledge bases.

  ## Improvements:

  * **Session Caching:** Added `cache_session` attribute to allow users to switch off session caching, which improves on memory management.
  * **Workflows 2.0 FastAPI Support**: Added support for running the new workflows in `FastAPIApp` .

  ## Bug Fixes:

  * **Nested Tool Hooks**: Fixed bug with nested tool hooks.
</Update>

<Update label="2025-07-16" description="v1.7.4">
  ## Workflows 2.0

  <img height="200" src="https://mintlify.s3.us-west-1.amazonaws.com/agno/images/changelogs/release-1-7-4.png" />

  ## New Features:

  * **Workflows Revamped (beta):** Our new Workflows implementation (internally referred to as Workflows 2.0) is a complete redesign of the workflow system in Agno, introducing a step-based architecture that provides better structure, flexibility, and control over multi-stage AI agent processes
    * Core Concepts:
      * **Flexible Execution**: Sequential, parallel, conditional, and loop-based execution
      * **Smart Routing**: Dynamic step selection based on content analysis or user intent
      * **Mixed Components**: Combine agents, teams, and functions seamlessly
      * **State Management:** Share data across steps with session state
    * For a comprehensive guide to the new Workflows system, check out the [docs](https://docs.agno.com/workflows_2/overview).
  * **Pydantic Input for Agents/Teams:** Both Agent and Team now accepts structured input (i.e. a pydantic model) on run() and print\_response().
</Update>

<Update label="2025-07-15" description="v1.7.3">
  ## New Features:

  * **Session State on Run**: You can now pass `session_state` when running an agent or team. See [docs](https://docs.agno.com/agents/state) for more information.
  * **GCS Support for PDF Knowledge Base:** Added `GCSPDFKnowledgeBase` to support PDFs on Google Cloud Storage.

  ## Bug Fixes:

  * **Workflows Async + Storage**: Fixed issues where sessions was not correctly stored with async workflow executions.
  * **Session State Management**: Fixed issues around session state management in teams and agents. Session state and session name will now correctly reset and load from storage if sessions are switched.
  * **Metadata Support for Document Knowledge Base:** Adds metadata support for `DocumentKnowledgeBase`
  * **Session Metrics with History**: Fixed bug with session metrics on `Agent` where history is enabled.
</Update>

<Update label="2025-07-10" description="v1.7.2">
  ## New Features:

  * **MySQL Storage**: Added support for `MySQLStorage` as an agent/team/workflow session storage backend.
  * **XAi Live Search**: Added support for live search on the XAi model provider.
  * **OpenAI Deep Research**: Support added for `o4-mini-deep-research` and `o3-deep-research` models.
  * **Stagehand MCP example**: Added an example of using Stagehand MCP with Agno.
  * **Atla observability example**: Added an example of using Atla observability with Agno.
  * **Scrapegraph example**: Added an example of using Scrapegraph with Agno.

  ## Improvements:

  * **Memory Growth on Performance Evals**: Added `memory_growth_tracking` as an attribute on `PerformanceEval` to enable additional debug logs for memory growth.
  * **Agent/Team in Tool Hook**: Added `agent` and `team` as optional parameters in tool hooks, for more flexibility.

  ## Bug Fixes:

  * **Gemini 2.5 Metrics:** Fixed Gemini metrics to correctly include “thinking” tokens.
  * **Claude tool calling:** Fixed a bug related to parsing function call responses when using Claude models.
  * **Team Metrics**: Fixed a bug with team metrics when teams have history enabled.
</Update>

<Update label="2025-06-30" description="v1.7.1">
  ## New Features:

  * **Debug Level:** Added `debug_level` to both `Agent` and `Team`. This is an `int` value of either `1` (default) or `2` (more verbose logging). Currently this only enables more verbose model logs, but will be used more widely in future.

  ## Improvements:

  * **Parser Model on Teams**: Added `parser_model` support for `Team`. See docs [here](https://docs.agno.com/teams/structured-output#using-a-parser-model).
  * **Support for Gemini Thinking**: Added `thinking_budget` and `include_thoughts` parameters for `Gemini` model class.
  * **Serper Tools**: Made updates to the toolkit to include new tools `search_news` , `search_scholar` and `scrape_webpage`.
  * **Valyu Tools:** New Valyu toolkit for Deep Search capabilities of academic sources.
  * **Oxylabs:** Added `OxylabsTools` for adding more web-scraping capabilities to agents.

  ## Bug Fixes:

  * **DuckDB CSV parsing error:** For CSV files use the custom `read_csv` method for improved CSV parsing
  * **Full Team Metrics**: Fixed an issue with calculation of the `full_team_session_metrics` on Teams.
</Update>

<Update label="2025-06-26" description="v1.7.0">
  ## New Features:

  * **Agent/Team Add Tool**: Added convenience function to `Agent` and `Team` → `add_tool(tool)` to append new tools after inititialisation.
  * **Streaming Structured Output**: Implemented structured output during streaming. This means streaming won’t be turned off when `response_model` is passed. The structured output itself is not streamed, but it is part of the iterator response when running an agent/team with streaming. The response model is set on a single `RunResponseContentEvent` and on the final `RunResponseCompletedEvent`.

  ## Improvements:

  * **Linear Teams Tool**: Added tool to get the list of teams from Linear.

  ## Bug Fixes:

  * **Uppercase Structured Output**: Resolved cases where pydantic model fields contain field names with upper case characters.

  ## Breaking Change:

  * If you use `run(..., stream=True)` or `arun(..., stream=True)` on `Agent` or `Team` with a `response_model` set, the current behaviour would switch off streaming and respond with a single `RunResponse` object. After the changes mentioned above, you will get the `Iterator[RunResponseEvent]` / `AsyncIterator[RunResponseEvent]` response instead.
</Update>

<Update label="2025-06-23" description="v1.6.4">
  ## New Features:

  * **Brightdata Toolkit**: Added multiple web-based tools via Brightdata.
  * **OpenCV Video/Image Toolkit**: Added tools for capturing image/video via your webcam.
  * **DiscordClient App**: Added a DiscordClient app for connecting your agent or team with Discord in the form of a discord bot.

  ## Improvements:

  * **FileTools File Search**: Added `search` to `FileTools`.

  ## Bug Fixes:

  * **Fix User Control Flow with History**: Fixed issues where user control flow (HITL) flows failed with message history.
  * **Fix lance db upsert method for supporting knowledge filters:** Fixed function `upsert` not using the parameter `filters`
  * **Update mongo db hybrid search for filters:** Mongodb now correctly uses filters for hybrid search
  * **Fixed `team.rename_session(...)` that raises an `AttributeError`: Fixed** function `rename_session` not using the parameter `session_id`
</Update>

<Update label="2025-06-18" description="v1.6.3">
  ## New Features:

  * **User Control Flows on Playground**: The Agno Platform now support user control flows on the playground.
  * **Team & Agent Events on RunResponse:** Added `store_events` parameter to optionally add all events that happened during the course of an agent/team run on the `RunResponse`/`TeamRunResponse`.
  * **Team Member Responses on Playground**: The Agno Platform now shows member responses during team runs.
  * **Behind-the-scenes on Playground**: The Agno Platform now shows what is happening during runs, for both agents and teams.
  * **Metadata filtering support for `csv` and `csv_url` knowledge bases:** Add knowledge filters support for these knowledge base types.

  ## Updates

  * **Removed `a` prefix from async function names:** `asearch_knowledge_base`, etc will now be the same as their `sync` counterparts when sent to the model. The names of functions are important for accurate function calling.

  ## Bug Fixes:

  * **AG-UI Fix**: Fixed issue related to missing messages when using the Agno AG-UI app.
  * **Chat History Fix**: Fixed issue related to history not available when `agent_id` not set.
  * **MongoDB ObjectId serialization issue when using with agent:** Fixed issue while \*\*\*\*using mongodb vectordb with ObjectId present in the metadata it throws Object of type `ObjectId` is not JSON serializable
</Update>

<Update label="2025-06-13" description="v1.6.1">
  ## New Features:

  * **Nebius Embeddings**: Added support for embedding models on Nebius.
  * **Firestore Memory and Storage:** Added support for Firestore both as memory and storage provider for your agents.

  ## Improvements:

  * **Improved Event Payloads**: Added `agent_name` to agent events, and `team_name` to team events. Also added `team_session_id` to team-member events to indicate that it belongs to the top-level team session.
  * **Team Run Events**: Added `stream_member_events` to teams to optionally disable streaming of member events.
  * **DocumentKnowledgeBase Async**: Added `async` support on `DocumentKnowledgeBase`
  * **Enums on Custom Tools**: Added support for `enum` parameters in custom tools.

  ## Bug Fixes:

  * **Team Events:** Fixed issues related to team and member events not being part of the same session. Going forward a team and its members will all have the same session ID.
</Update>

<Update label="2025-06-10" description="v1.6.0">
  ## Improvements:

  * **New Streaming Events**: We have improved our streaming events system. See the details in “breaking changes” section at the bottom.
  * **Member Events in Teams**: The above change includes streaming of events from team members with the top-level team events.

  ## Bug Fixes:

  * **Apify Tools:** Fixed the ApifyTools initialize to correctly register functions.

  ## Breaking Changes:

  * **Updates to Run Without Streaming**:
    * `RunResponse` now does not have an `event` attribute. It still represents the responses of the entire run.
    * An additional attribute `RunResponse.status` now indicates whether the run response is `RUNNING`, `PAUSED`, or `CANCELLED`.
  * **Updates to Run Streaming:**
    * In the case of streaming you now get reformulated run events. These events are streamed if you do `agent.run(..., stream=True)` or `agent.arun(..., stream=True)` .
    * Agents have the following event types:
      * `RunResponseContent`
      * `RunError`
      * `RunCancelled`
      * `ToolCallStarted`
      * `ToolCallCompleted`
      * with `stream_intermediate_steps=True`:
        * `RunStarted`
        * `RunCompleted`
        * `ReasoningStarted`
        * `ReasoningStep`
        * `ReasoningCompleted`
        * `MemoryUpdateStarted`
        * `MemoryUpdateCompleted`
    * See detailed documentation [here](https://docs.agno.com/agents/run).
  * **Updates to Teams:**
    * Teams have the following event types:
      * `TeamRunResponseContent`
      * `TeamRunError`
      * `TeamRunCancelled`
      * `TeamToolCallStarted`
      * `TeamToolCallCompleted`
      * with `stream_intermediate_steps=True`:
        * `TeamRunStarted`
        * `TeamRunCompleted`
        * `TeamReasoningStarted`
        * `TeamReasoningStep`
        * `TeamReasoningCompleted`
        * `TeamMemoryUpdateStarted`
        * `TeamMemoryUpdateCompleted`
    * Teams will also yield events from team members as they are executed.
    * See detailed documentation [here](https://docs.agno.com/teams/run).
  * **Updates to Workflows:**
    * You should now yield `WorkflowRunResponseStartedEvent` and `WorkflowRunResponseCompletedEvent` events.
</Update>

<Update label="2025-06-06" description="v1.5.10">
  ## New Features:

  * **Playground File Upload**: We now support file upload via the Agno Playground. This will send PDF, CSV, Docx, etc files directly to the agents/teams for interpretation by the downstream LLMs.  If you have a knowledge base attached to the agent/team, it will upload the file to the knowledge base instead.
  * **Async Evals**: Support for `async` and evaluations. See examples [here](https://github.com/agno-agi/agno/tree/main/cookbook/evals).

  ## Improvements:

  * **Exa Research**: Added `research` tool on `ExaTools`. See more on their [docs](https://docs.exa.ai/reference/exa-research) about how research works.
  * **Whatsapp Type Indicator**: Add type indicator to Whatsapp responses.

  ## Bug Fixes:

  * **State in Messages Fixes**: Fixed issues around nested json inside messages and adding state into messages.
</Update>

<Update label="2025-06-05" description="v1.5.9">
  ## New Features:

  * **AG-UI App**: Expose your Agno Agents and Teams with an AG-UI compatible FastAPI APP.
  * **vLLM Support**: Added support for running vLLM models via Agno.
  * **Serper Toolkit:** Added `SerperTools` toolkit to search Google
  * **LangDB Support**: Added LangDB AI Gateway support into Agno.
  * **LightRAG server support:** Added LightRAG support which provides a fast, graph-based RAG system that enhances document retrieval and knowledge querying capabilities.
  * **Parser Model:** Added ability to use an external model to apply a structured output to a model response
  * **Pdf Bytes Knowledge: I**ntroduced a new knowledge base class: `PDFBytesKnowledgeBase`, which allows the ingestion of in-memory PDF content via bytes or IO streams instead of file paths.
  * **Qdrant Mcp Server:** Added MCP support for Qdrant
  * **Daytona integration:** Added `DaytonaTools` toolkit to let Agents execute code remotely on Daytona sandboxes
  * **Expand URL addition in Crawl4ai: I**ntroduced a new URL expansion feature directly into the Crawl4ai toolkit. Our agents frequently encounter shortened URLs that crawl4ai cannot scrape effectively, leading to incomplete data retrieval. With this update, shortened URLs are expanded to their final destinations before being processed by the crawler.
  * **AWS SES Tools**: Added `AWSSESTools` to send emails via AWS SES.
  * **Location Aware Agents:** Added `add_location_to_instructions` to automatically detect the current location where the agent is running and add that to the system message.

  ## Improvements:

  * **FastAPIApp Update**: FastAPIApp was updated and `agent` was replaced with `agents`, `team` with `teams` and `workflows` was added. This also now requires you to specify which agent/team/workflow to run.
    * E.g. `http://localhost:8001/runs?agent_id=my-agent`
  * **ZepTools Updates**: Updated `ZepTools` to remove deprecated features.
  * **GmailTools Attachments**: `GmailTools` now support attachments.
  * **Improve code reusability by using fetch with retry and async\_fetch\_with\_retry:** updated `fetch_with_retry` and `async_fetc_with_retry` to be reused in`url_reader.py`
  * **Add name to evaluation examples:** Included name param in evaluation examples
  * **XTools Search**: Added `search_posts` for `XTools`.

  ## Bug Fixes:

  * **Claude Prompt Tokens**: Fixed a bug with prompt tokens not propagating in Claude model class
  * **Add type in base App class for registry:** Can have different types of app like- `slack`, `whatsapp`, etc
  * **Accept empty array of pdf urls:** Fixed an issue where empty PDF URL arrays were not accepted, preventing knowledge base queries without adding new documents
  * **Anthropic cache metrics propagation:** Fixed a bug where Anthropic's prompt caching metrics were not propagating to Agent responses, despite the raw Anthropic API working correctly. This minimal fix ensures cache performance metrics are properly captured and reported.
  * **Handle non serializable objects on RunResponse dict parsing:**
    * Updated `RunResponse.to_dict()` to handle non-serializable fields, as Python enums
</Update>

<Update label="2025-06-03" description="v1.5.8">
  ## New Features:

  * **Slack App**: Introducing the `SlackApp` to allow you to create agents for Slack! The app allows agents to respond to individual messages or on group chats, and it creates threads to respond to messages.
  * **Visualization Tools**: Added `VisualizationTools` that uses `matplotlib` to give agents the ability to make graphs.
  * **Brave Search Tools:** Introduced a new toolkit for integrating `BraveSearch` that allows agent to search the web using brave search api.

  ## Improvements:

  * **Pass filters for traditional RAG:** Properly pass down `knowledge_filters` even if `self.add_references=True` which is a case for traditional RAG (diff from Agentic RAG)
  * **Add infer param to Mem0:** Added infer as a param to `Mem0Tools`

  ## Bug Fixes:

  * **Searxng tool initialization:**  Fixed Searxng tool initialization error

    ```
    AttributeError: 'Searxng' object has no attribute 'include_tools'
    ```

    and added comprehensive unit tests.

  * **Fix for enum as a response model for Gemini:** With 1.5.6, a [bug](https://discord.com/channels/965734768803192842/965734768803192845/1377999191632121926) was introduced now allowing enum as a data type for Gemini response model.

  * **OpenAI parsing structured output:** With the changes in the OpenAI library we don't need to parse the structured output separately.

  * **Fix accuracy evals monitoring:** Added logic to handle monitoring when evaluating Teams in the run function of AccuracyEval

  ## Updates

  * **Updates to Apps:**
    * `FastAPIApp` does not have a default `prefix` anymore and `/run` → `/runs` (i.e. the created run endpoint is now `<your_domain>/runs`)
    * `serve_fastapi_app` is now replaced with `.serve()` on the instance of `FastAPIApp`.
    * `serve_whatsapp_app` is now replaced with `.serve()` on the instance of `WhatsappAPI`.
</Update>

<Update label="2025-05-30" description="v1.5.6">
  ## New Features

  * **Team Evals**: All types of Evaluations now support Teams!

  ## Improvements:

  * **Async Workflows**: Added `arun` support for Workflows, so they can now be used with `async` Python.
  * **Parallel Memory Updates**: Made speed improvements when user memories and session summaries are generated.
  * **Reimplement `tool_call_limit`**: Revamp of `tool_call_limit` to make it work across a whole agent run.
  * **Gemini / OpenAI Structure Response:** Improved Gemini and OpenAI Structured Response support. Dict types can now be used when defining structured responses.

  ## Bug Fixes:

  * **Mistral Structured Outputs with Tools**: Fixed an issue preventing Mistral model use with structured output and tools.
  * **Images In Run Without Prompt**: Fixed issues related to images being ignored if there wasn’t a prompt provided on `run`.
  * **Pgvector Upsert Fix: Fixed** Pgvector upsert not copying metadata properly.
  * **Handle AgnoInstrumentor failing with OpenAIResponses:** PR merged in Arize’s openinference repo: [https://github.com/Arize-ai/openinference/pull/1701](https://github.com/Arize-ai/openinference/pull/1701).
  * **Pinecone Filters:** Enabled filters for pinecone vector db.
  * **Combined KB Async:** Add missing async method to Combined KB.
  * **Team Session State Fix**: **`team_session_state`** is now correctly propagated and shared between all members and sub-teams of a team.
  * **Gemini type fix for integers:**
    * Pydantic models with `Dict[str, int]` fields (and other Dict types) were failing when used as `response_schema` for both OpenAI and Gemini models due to schema format incompatibilities.
  * **Session Name**: `session_name` is now available after a run.
  * **Handle UUIDs while serialization in RedisStorage:** Fixed error object of type UUID is not JSON serializable.

  ## Updates:

  * For managing `team_session_state`, you now have to set `team_session_state` on the `Team` instead of `session_state`.
</Update>

<Update label="2025-05-27" description="v1.5.5">
  ## New Features:

  * **Claude File Upload:** We can now upload a file to Anthropic directly and then use it as an input to an agent.
  * **Claude 4 Code Execution Tool:** Updated Claude to execute Python code in a secure, sandboxed environment.
  * \*\*Prompt caching with Anthropic Models: \*\* Allowed resuming from specific prefixes in your prompts. This approach significantly reduces processing time and costs for repetitive tasks or prompts with consistent elements.
  * **Vercel v0 Model:** Added support for new Vercel v0 models and cookbook examples.
  * **Qdrant Hybrid Search support**
  * **Markdown Knowledge Base**: Added native support for Markdown-based knowledge bases.
  * **AI/ML API platform integration:** Introduced integration with [`AI/ML API`](https://aimlapi.com/models/?utm_source=agno\&utm_medium=github\&utm_campaign=integration), a platform providing AI/ML models. AI/ML API provides 300+ AI models including Deepseek, Gemini, ChatGPT. The models run at enterprise-grade rate limits and uptimes.
  * **Update Pydantic and dataclass in function handling:** Added support for `Pydantic` and `dataclass` objects as input to a function. See [here](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/tool_concepts/custom_tools/complex_input_types.py) for an example.

  ## Improvements:

  * **Timeout handling for API calls in ExaTools class:**
    * Timeout functionality to Exa API calls to prevent indefinite hanging of search operations. The implementation uses Python's `concurrent.futures` module to enforce timeouts on all Exa API operations (search, get contents, find similar, and answer generation).
    * This change addresses the issue where Exa search functions would hang indefinitely, causing potential service disruptions and resource leaks.
  * **Fetch messages from last N sessions:**
    * A tool for the agent, something like `get_previous_session_messages(number_of_sessions: int)` that returns a list of messages that the agent can analyse
    * Switch on with `search_previous_sessions_history`
  * **Redis Expiration**: Added `expire` key to set TTL on Redis keys.
  * **Add Anthropic Cache Write to Agent Session Metrics:** Added `cache_creation_input_tokens` to agent session metrics, to allow for tracking Anthropic cache write statistics

  ## Bug Fixes:

  * **Huggingface Embedder Updates:**
    * Huggingface has changed some things on their API and they've deprecated `.post` on their `InferenceClient()`- [https://discuss.huggingface.co/t/getting-error-attributeerror-inferenceclient-object-has-no-attribute-post/156682](https://discuss.huggingface.co/t/getting-error-attributeerror-inferenceclient-object-has-no-attribute-post/156682)
    * We can also no longer use `id: str = "jinaai/jina-embeddings-v2-base-code"` as default, because these models are no longer provided by the `HF Inference API`. Changed the default to `id: str = "intfloat/multilingual-e5-large"`
  * **Add `role_map` for `OpenAIChat`:** This allows certain models that don’t adhere to OpenAI’s role mapping to be used vir `OpenAILike`.
  * **Use Content Hash as ID in Upsert in Pgvector:** Use reproducible `content_hash` in upsert as ID.
  * **Insert in Vector DB passes only last chunk meta\_data:** Insert in vector db passes only last chunk meta\_data. issue link- [https://discord.com/channels/965734768803192842/1219054452221153463/1376631140047130649](https://discord.com/channels/965734768803192842/1219054452221153463/1376631140047130649)
  * **Remove Argument Sanitization:** Replaced with a safer way to do this that won't break arguments that shouldn't be sanitized
  * **Handle async tools when running async agents on playground:** Fixed a regression where using Agents with async tools (e.g. MCP tools) was breaking in the Playground.
</Update>

<Update label="2025-05-23" description="v1.5.4">
  ## New Features:

  * **User Control Flows**: This is the beta release of Agno’s Human-in-the-loop flows and tools.
    * We now allow agent runs to be `paused` awaiting completion of certain user requirements before the agent can continue.
    * This also adds the `agent.continue_run` and `agent.acontinue_run` functions.
    * The control flows that are available:
      * User confirmation flow → Decorate a function with `@tool(requires_confirmation=True)` and the agent will expect user confirmation before executing the tool.
      * User input required → Decorate a function with `@tool(requires_user_input=True)` to have the agent stop and ask for user input before continuing.
      * External tool execution → Decorate a function with `@tool(external_execution=True)` to indicate that you will execute this function outside of the agent context.
      * Dynamic user input → Add `UserControlFlowTools()` to an agent to give the agent the ability to dynamically stop the flow and ask for user input where required.
    * See a host of examples [here](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/user_control_flows).
  * **Mem0 Toolkit**: Added a toolkit for managing memories in Mem0.
  * **Firecrawl Search**: Added support for Firecrawl web search in `FirecrawlTools`.

  ## Bug Fixes:

  * **Firecrawl Tools and Reader**: Fixed parameter parsing for the Firecrawl reader and tools.
  * **Include/Exclude on all Tools**: Ensure all toolkits support `include_tools` and `exclude_tools`.
</Update>

<Update label="2025-05-21" description="v1.5.3">
  ## Improvements:

  * **Improved Accuracy Evals:** Updated the way accuracy evals works for more accurate agent-based evaluation.

  ## Bug Fixes:

  * **MCP Client Timeout:** Client timeouts now work correctly and use the timeout set on parameters.
</Update>

<Update label="2025-05-20" description="v1.5.2">
  ## New Features:

  * **Agno Apps (Beta)**: Introducing Agno Apps, convenience functions to assist with building production-ready applications. The first supported apps are:
    * `FastAPIApp` → A really simple FastAPI server that provides access to your `agent` or `team`.
    * `WhatsappAPIApp` → An app that implements the Whatsapp protocol allowing you to have an Agno agent running on Whatsapp. Supports image / audio / video input and can generate images as responses. Supports reasoning.
  * **Couchbase Vector DB Support**: Added support for Couchbase as a vector DB for knowledge bases.
  * **Knowledge Filters Update for Teams:** Filters (manual + agentic) can now be used with Teams.
  * **Azure Cosmos DB for MongoDB (vCore) vector db support:**  In the MongoDB vector db class add support for cosmosdb mongo vcore support by enabling `cosmos_compatibility=True`
  * **Google Big Query Tools**: Added Toolkit for Google BigQuery support.
  * **Async Support for s3 Readers:** Add async support for `pdf` and `text` s3 readers.
  * **`stop_after_tool_call` and `show_result` for Toolkits:** Now the base Toolkit class has `stop_after_tool_call_tools` and `show_result_tools` similar to the `@tool` decorator.
</Update>

<Update label="2025-05-16" description="v1.5.1">
  ## New Features:

  * **Nebius Model Provider**: Added [Nebius](https://studio.nebius.com/) as a model provider.
  * **Extended Filters Support on Vector DBs**: Added filtering support for other vector DBs.
    * pgvector
    * Milvus
    * Weaviate
    * Chroma

  ## Improvements:

  * **Redis SSL**: Added the `ssl` parameter to `Redis` storage.
</Update>

<Update label="2025-05-13" description="v1.5.0">
  ## New Features:

  * **Azure OpenAI Tools**: Added image generation via Dall-E via Azure AI Foundry.
  * **OpenTelemetry Instrumentation:** We have contributed to the [OpenInference](https://github.com/Arize-ai/openinference) project and added an auto-instrumentor for Agno agents. This adds tracing instrumentation for Agno Agents for any OpenTelemetry-compatible observability provider. These include Arize, Langfuse and Langsmith. Examples added to illustrate how to use each one ([here](https://github.com/agno-agi/agno/tree/main/cookbook/observability)).
  * **Evals Updates**: Added logic to run accuracy evaluations with pre-generated answers and minor improvements for all evals classes.
  * **Hybrid Search and Reranker for Milvus Vector DB:** Added support for `hybrid_search` on Milvus.
  * **MCP with Streamable-HTTP:** Now supporting the streamable-HTTP transport for MCP servers.

  ## Improvements:

  * **Knowledge Filters Cookbook:** Instead of storing the sample data locally, we now pull it from s3 at runtime to keep the forking of the repo as light as possible.

  ## Bug Fixes:

  * **Team Model State:** Fixed issues related to state being shared between models on teams.
  * **Concurrent Agent Runs**: Fixed certain race-conditions related to running agents concurrently.

  ## Breaking changes:

  * **Evals Refactoring:**
    * Our performance evaluation class has been renamed from `PerfEval` to `PerformanceEval`
    * Our accuracy evaluation class has new required fields: `agent`, `prompt` and `expected_answer`
  * **Concurrent Agent Runs:** We removed duplicate information from some events during streaming (`stream=True`). Individual events will have more relevant data now.
</Update>

<Update label="2025-05-10" description="v1.4.6">
  ## New Features:

  * **Cerebras Model Provider**: Added Cerebras as a model provider.
  * **Claude Web Search**: Added support for [Claude’s new web search tool](https://www.anthropic.com/news/web-search).
  * **Knowledge Base Metadata Filtering (Beta)**: Added support for filtering documents by metadata
    * **Two Ways to Apply Filters**:
      * **Explicit Filtering**: Pass filters directly to Agent or during run/query

        ```python
        # Option 1: Filters on Agent initialization
        agent = Agent(
        					knowledge=knowledge_base, 
        					knowledge_filters={"filter_1": "abc"}
        				)
             
        # Option 2: Filters on run execution
        agent.run("Tell me about...", knowledge_filters={"filter_1": "abc"})
        ```

        See docs [here](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/filters/pdf/filtering.py)

      * **Agentic Filtering**: Agent automatically detects and applies filters from user queries

        ```python
        # Enable automatic filter detection
        agent = Agent(
        					knowledge=knowledge_base, 
        					enable_agentic_knowledge_filters=True
        				)
             
        # Agent extracts filters from query
        agent.run("Tell me about John Doe's experience...")
        ```

        See docs [here](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/filters/pdf/agentic_filtering.py)
    * Two approaches for adding metadata to documents:
      1. **During Knowledge Base Initialization**:

         ```python
         knowledge_base = PDFKnowledgeBase(path=[
              {
         		     "path": "file_1.pdf", 
         		     "metadata": {
         				     "user_id": "abc"
         				  }
         		 },
         		 {
         		     "path": "file_2.pdf", 
         		     "metadata": {
         				     "user_id": "xyz"
         				  }
         		 }
         ])
         ```

      2. **During Individual Document Loading:**

         ```python
         knowledge_base.load_document(
              path="file.pdf",
              metadata={"user_id": "abc"}
         )
         ```
    * **Compatibility**
      * **Knowledge Base Types**: `PDF`, `Text`, `DOCX`, `JSON`, and `PDF_URL`
      * **Vector Databases**: `Qdrant`, `LanceDB`, and `MongoDB`

  ## Improvements:

  * **User and Session ID in Tools**: Added `current_user_id` and `current_session_id` as default variables in `session_data` for `Agent` and `Team`.

  ## Bug Fixes:

  * **Knowledge Base ID Clashes**: Knowledge files with overlapping names (e.g., `abc.-.xyz.pdf` and `abc.-.def.pdf`) were being incorrectly identified due to the readers using formatted names as unique id which were getting uniqueness conflict. Introduced a unique ID for each document in all the readers using `uuidv4()` to ensure strict identification and prevent conflicts.
</Update>

<Update label="2025-05-06" description="v1.4.5">
  ## New Features:

  * **Embedder Support via AWS Bedrock**: `AwsBedrockEmbedder` has been added with a default embedding model of `cohere.embed-multilingual-v3`.
  * **Gemini Video Generation Tool**: Added video generation capabilities to `GeminiTools`.

  ## Improvements:

  * **Apify Revamp**: Complete revamp of `ApifyTools` to make it completely compatible with Apify actors.

  ## Bug Fixes:

  * **Tools with Optional Parameters on Llama API**: Fixed edge cases with functions.
</Update>

<Update label="2025-05-03" description="v1.4.4">
  ## New Features:

  * **OpenAI File Support:** Added support for `File` attached to prompts for agents with `OpenAIChat` models.

  ## Improvements:

  * **Llama API:** Various improvements for Llama and LlamaOpenAI model classes including structured output and image input support
  * **Async Custom Retriever**: The `retriever` parameter can now be an `async` function to be used with `agent.arun` and `agent.aprint_response`.
  * **Gemini Video URL Input**: Added support for `Video(url=...)` for Gemini.

  ## Bug Fixes:

  * **OpenAI Responses o3 / o4 Tools**: Fixed broken tool use for advanced reasoning models on `OpenAIResponses`.
  * **MCP on CLI Support**: Fixed support for `MCPTools` usage while calling `agent.acli_app`.
</Update>

<Update label="2025-04-30" description="v1.4.3">
  ## **New Features:**

  * **Llama API:** Added native SDK and OpenAI-like model classes.

  ## **Improvements:**

  * **Claude**: Added support for AWS Session token for Claude.
  * **DynamoDB**: Added support for AWS profile-based authentication.

  ## **Bug Fixes:**

  * **Session Metrics**: Fix for session metrics showing up as 0.
  * **HF Embedder fix**: Fixed Hugging Face Embedder.
</Update>

<Update label="2025-04-25" description="v1.4.2">
  ## New Features:

  * **MCP SSE Support**: Added support for connecting to SSE MCP Servers.
  * **Tool Hooks**: You can now have a hook that is wrapped around all tool calls. This works for `Toolkits` and custom tools. See [this example](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/tool_concepts/toolkits/tool_hook.py).
  * **Team Session State:** You can now manage a single state dictionary across a team leader and team members inside tools given to the team leader/members. See [this example](https://github.com/agno-agi/agno/blob/main/cookbook/teams/team_with_shared_state.py).
  * **Cartesia Tool**: Added support for Cartesia for text-to-speech capabilities.
  * **Gemini Image Tools:** Added a tool that uses Gemini models to generate images.
  * **Groq Audio Tools**: Added a tool that uses Groq models to translate, transcribe and generate audio.

  ## Improvements:

  * **PubmedTools Expanded Results**: Added expanded result sets for `PubmedTools` .
  * **Variety in Tool Results**: Custom tools can now have any return type and it would be handled before being provided to the model.

  ## Bug Fixes:

  * **Teams Shared Model Bug**: Fixed issues where a single model is used across team members. This should reduce tool call failures in team execution.
</Update>

<Update label="2025-04-23" description="v1.4.0">
  ## New Features:

  * **Memory Generally Available**: We have made improvements and adjustments to how Agentic user memory management works. This is now out of beta and generally available. See these [examples](https://github.com/agno-agi/agno/tree/main/cookbook/agent_concepts/memory) and these [docs](https://docs.agno.com/agents/memory) for more info.
  * **OpenAI Tools**: Added `OpenAITools` to enable text-to-speech and image generation through OpenAI’s APIs.
  * **Zep Tools**: Added `ZepTools` and `AsyncZepTools` to manage memories for your Agent using `zep-cloud`

  ## Improvements:

  * **Azure AI Foundry Reasoning**: Added support for reasoning models via Azure AI Foundry. E.g. Deepseek-R1.
  * **Include/Exclude Tools**: Added `include_tools` and `exclude_tools` for all toolkits. This allows for selective enabling / disabling of tools inside toolkits, which is especially useful for larger toolkits.

  ## Bug Fixes:

  * **Gemini with Memory**: Fixed issue with `deepcopy` when Gemini is used with `Memory`.

  ## Breaking Changes:

  * **Memory:** Agents will now by default use an improved `Memory` instead of the now deprecated `AgentMemory`. - `agent.memory.messages` → `run.messages for run in agent.memory.runs` (or `agent.get_messages_for_session()`) - `create_user_memories` → `enable_user_memories` and is now set on the Agent/Team directly. - `create_session_summary` → `enable_session_summaries` and is now set on the Agent/Team directly.
</Update>

<Update label="2025-04-21" description="v1.3.5">
  ## Improvements:

  * **Further Async Vector DB Support**: Support added for:
    * [Clickhouse](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/vector_dbs/clickhouse_db/async_clickhouse.py)
    * [ChromaDB](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/vector_dbs/chroma_db/async_chroma_db.py)
    * [Cassandra](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/vector_dbs/cassandra_db/async_cassandra_db.py)
    * [PineconeDB](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/vector_dbs/pinecone_db/async_pinecone_db.py)
    * [Pgvector](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/vector_dbs/pgvector_db/async_pg_vector.py)
  * **Reasoning on Agno Platform**:
    * Added extensive support for reasoning on the Agno Platform. Go see your favourite reasoning agents in action!
    * Changes from SDK
      * send proper events in different types of reasoning and populate the `reasoning_content` on `RunResponse` for `stream/non-stream`, `async/non-async`
      * unified json structure for all types of reasoning in `Reasoning events`
  * **Google Caching Support**: Added support for caching files and sending the cached content to Gemini.

  ## Bug Fixes

  * **Firecrawl Scrape**: Fixed issues with non-serializable types for during Firecrawl execution. [https://github.com/agno-agi/agno/issues/2883](https://github.com/agno-agi/agno/issues/2883)
</Update>

<Update label="2025-04-18" description="v1.3.4">
  ## New Features:

  * **Web Browser Tool:** Introduced a `webbrowser` tool for agents to interact with the web.
  * **Proxy Support:** Added `proxy` parameter support to both URL and PDF tools for network customization.

  ## Improvements:

  * **Session State:** Added examples for managing session state in agents.
  * **AzureOpenAIEmbedder:** Now considers `client_params` passed in the `client_params` argument for more flexible configuration.
  * **LiteLLM:** Now uses built-in environment validation to simplify setup.
  * **Team Class:** Added a `mode` attribute to team data serialization for enhanced team configuration.
  * **Insert/Upsert/Log Optimization:** insert/upsert/log\_info operations now trigger only when documents are present in the reader.
  * **Database Preference:** Session state now prefers database-backed storage if available.
  * **Memory Management:** Internal memory system updated for better session handling and resource efficiency.
  * **Module Exports:** Init files that only import now explicitly export symbols using `__all__`.

  ## Bug Fixes:

  * **DynamoDB Storage:** Fixed an issue with storage handling in DynamoDB-based setups.
  * **DeepSeek:** Fixed a bug with API key validation logic.
</Update>

<Update label="2025-04-17" description="v1.3.3">
  ## Improvements:

  * **Gemini File Upload**: Enabled direct use of uploaded files with Gemini.
  * **Metrics Update**: Added audio, reasoning and cached token counts to metrics where available on models.
  * **Reasoning Updates**: We now natively support Ollama and AzureOpenAI reasoning models.

  ## Bug Fixes:

  * **PPrint Util Async**: Added `apprint_run_response` to support async.
  * **Mistral Reasoning:** Fixed issues with using a Mistral model for chain-of-thought reasoning.
</Update>

<Update label="2025-04-16" description="v1.3.2">
  ## New Features:

  * **Redis Memory DB**: Added Redis as a storage provider for `Memory`. See [here](https://docs.agno.com/examples/concepts/memory/mem-redis-memory).

  ## Improvements:

  * **Memory Updates**: Various performance improvements made and convenience functions added:
    * `agent.get_session_summary()` → Use to get the previous session summary from the agent.
    * `agent.get_user_memories()` → Use to get the current user’s memories.
    * You can also add additional instructions to the `MemoryManager` or `SessionSummarizer`.
  * **Confluence Bypass SSL Verification**: If required, you can now skip SSL verification for Confluence connections.
  * **More Flexibility On Team Prompts**: Added `add_member_tools_to_system_message` to remove the member tool names from the system message given to the team leader, which allows flexibility to make teams transfer functions work in more cases.

  ## Bug Fixes:

  * **LiteLLM Streaming Tool Calls**: Fixed issues with tool call streaming in LiteLLM.
  * **E2B Casing Issue**: Fixed issues with parsed Python code that would make some values lowercase.
  * **Team Member IDs**: Fixed edge-cases with team member IDs causing teams to break.
</Update>

<Update label="2025-04-12" description="v1.3.0">
  ## New Features:

  * **Memory Revamp (Beta)**: This is a beta release of a complete revamp of Agno Memory. This includes a new `Memory` class that supports adding, updating and deleting user memories, as well as doing semantic search with a model. This also adds additional abilities to the agent to manage memories on your behalf. See the docs [here](https://docs.agno.com/memory/introduction).
  * **User ID and Session ID on Run**: You can now pass `user_id` and `session_id` on `agent.run()`. This will ensure the agent is set up for the session belonging to the `session_id` and that only the memories of the current user is accessible to the agent. This allows you to build multi-user and multi-session applications with a single agent configuration.
  * **Redis Storage**: Support added for Redis as a session storage provider.
</Update>

<Update label="2025-04-11" description="v1.2.16">
  ## Improvements:

  * **Teams Improvements**: Multiple improvements to teams to make task forwarding to member agents more reliable and to make the team leader more conversational. Also added various examples of reasoning with teams.
  * **Knowledge on Teams**: Added `knowledge` to `Team` to better align with the functionality on `Agent`. This comes with `retriever` to set a custom retriever and `search_knowledge` to enable Agentic RAG.

  ## Bug Fixes:

  * **Gemini Grounding Chunks**: Fixed error when Gemini Grounding was used in streaming.
  * **OpenAI Defaults in Structured Outputs**: OpenAI does not allow defaults in structured outputs. To make our structured outputs as compatible as possible without adverse effects, we made updates to `OpenAIResponses` and `OpenAIChat`.
</Update>

<Update label="2025-04-08" description="v1.2.14">
  ## Improvements:

  * **Improved Github Tools**: Added many more capabilities to `GithubTools`.
  * **Windows Scripts Support**: Converted all the utility scripts to be Windows compatible.
  * **MongoDB VectorDB Async Support**: MongoDB can now be used in async knowledge bases.

  ## Bug Fixes:

  * **Gemini Tool Formatting**: Fixed various cases where functions would not be parsed correctly when used with Gemini.
  * **ChromaDB Version Compatibility:** Fix to ensure that ChromaDB and Agno are compatible with newer versions of ChromaDB.
  * **Team-Member Interactions**: Fixed issue where if members respond with empty content the team would halt. This is now be resolved.
  * **Claude Empty Response:** Fixed a case when the response did not include any content with tool calls resulting in an error from the Anthropic API
</Update>

<Update label="2025-04-07" description="v1.2.12">
  ## New Features:

  * **Timezone Identifier:** Added a new `timezone_identifier` parameter in the Agent class to include the timezone alongside the current date in the instructions.
  * **Google Cloud JSON Storage**: Added support for JSON-based session storage on Google Cloud.
  * **Reasoning Tools**: Added `ReasoningTools` for an advanced reasoning scratchpad for agents.

  ## Improvements:

  * **Async Vector DB and Knowledge Base Improvements**: More knowledge bases have been updated for `async-await` support: - `URLKnowledgeBase` → Find some examples [here](https://github.com/agno-agi/agno/blob/9d1b14af9709dde1e3bf36c241c80fb295c3b6d3/cookbook/agent_concepts/knowledge/url_kb_async.py). - `FireCrawlKnowledgeBase` → Find some examples [here](https://github.com/agno-agi/agno/blob/596898d5ba27d2fe228ea4f79edbe9068d34a1f8/cookbook/agent_concepts/knowledge/firecrawl_kb_async.py). - `DocxKnowledgeBase` → Find some examples [here](https://github.com/agno-agi/agno/blob/f6db19f4684f6ab74044a4466946e281586ca1cf/cookbook/agent_concepts/knowledge/docx_kb_async.py).
</Update>

<Update label="2025-04-07" description="v1.2.11">
  ## Bug Fixes:

  * **Fix for structured outputs**: Fixed cases of structured outputs for reasoning.
</Update>

<Update label="2025-04-07" description="v1.2.10">
  ## 1.2.10

  ## New Features:

  * **Knowledge Tools**: Added `KnowledgeTools` for thinking, searching and analysing documents in a knowledge base.
</Update>

<Update label="2025-04-05" description="v1.2.9">
  ## 1.2.9

  ## Improvements:

  * **Simpler MCP Interface**: Added `MultiMCPTools` to support multiple server connections and simplified the interface to allow `command` to be passed. See [these examples](https://github.com/agno-agi/agno/blob/382667097c31fbb9f08783431dcac5eccd64b84a/cookbook/tools/mcp) of how to use it.
</Update>

<Update label="2025-04-04" description="v1.2.8">
  ## 1.2.8

  # Changelog

  ## New Features:

  * **Toolkit Instructions**: Extended `Toolkit` with `instructions` and `add_instructions` to enable you to specify additional instructions related to how a tool should be used. These instructions are then added to the model’s “system message” if `add_instructions=True` .

  ## Bug Fixes:

  * **Teams transfer functions**: Some tool definitions of teams failed for certain models. This has been fixed.
</Update>

<Update label="2025-04-02" description="v1.2.7">
  ## 1.2.7

  ## New Features:

  * **Gemini Image Generation**: Added support for generating images straight from Gemini using the `gemini-2.0-flash-exp-image-generation` model.

  ## Improvements:

  * **Vertex AI**: Improved use of Vertex AI with Gemini Model class to closely follow the official Google specification
  * **Function Result Caching Improvement:** We now have result caching on all Agno Toolkits and any custom functions using the `@tool` decorator. See the docs [here](https://docs.agno.com/tools/functions).
  * **Async Vector DB and Knowledge Base Improvements**: Various knowledge bases, readers and vector DBs now have `async-await` support, so it will be used in `agent.arun` and `agent.aprint_response`. This also means that `knowledge_base.aload()` is possible which should greatly increase loading speed in some cases. The following have been converted:
    * Vector DBs:
      * `LanceDb` → [Here](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/vector_dbs/lance_db/async_lance_db.py) is a cookbook to illustrate how to use it.
      * `Milvus` → [Here](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/vector_dbs/milvus_db/async_milvus_db.py) is a cookbook to illustrate how to use it.
      * `Weaviate` → [Here](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/vector_dbs/weaviate_db/async_weaviate_db.py) is a cookbook to illustrate how to use it.
    * Knowledge Bases:
      * `JSONKnowledgeBase` → [Here](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/json_kb_async.py) is a cookbook to illustrate how to use it.
      * `PDFKnowledgeBase` → [Here](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/pdf_kb_async.py) is a cookbook to illustrate how to use it.
      * `PDFUrlKnowledgeBase` → [Here](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/pdf_url_kb_async.py) is a cookbook to illustrate how to use it.
      * `CSVKnowledgeBase` → [Here](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/csv_kb_async.py) is a cookbook to illustrate how to use it.
      * `CSVUrlKnowledgeBase` → [Here](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/csv_url_kb_async.py) is a cookbook to illustrate how to use it.
      * `ArxivKnowledgeBase` → [Here](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/arxiv_kb_async.py) is a cookbook to illustrate how to use it.
      * `WebsiteKnowledgeBase` → [Here](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/website_kb_async.py) is a cookbook to illustrate how to use it.
      * `YoutubeKnowledgeBase` → [Here](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/youtube_kb_async.py) is a cookbook to illustrate how to use it.
      * `TextKnowledgeBase` → [Here](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/text_kb_async.py) is a cookbook to illustrate how to use it.

  ## Bug Fixes:

  * **Recursive Chunking Infinite Loop**: Fixes an issue with RecursiveChunking getting stuck in an infinite loop for large documents.
</Update>

<Update label="2025-03-28" description="v1.2.6">
  ## 1.2.6

  ## Bug Fixes:

  * **Gemini Function call result fix**: Fixed a bug with function call results failing formatting and added proper role mapping .
  * **Reasoning fix**: Fixed an issue with default reasoning and improved logging for reasoning models .
</Update>

<Update label="2025-03-27" description="v1.2.5">
  ## 1.2.5

  ## New Features:

  * **E2B Tools:** Added E2B Tools to run code in E2B Sandbox

  ## Improvements:

  * **Teams Tools**: Add `tools` and `tool_call_limit` to `Team`. This means the team leader itself can also have tools provided by the user, so it can act as an agent.
  * **Teams Instructions:** Improved instructions around attached images, audio, videos, and files. This should increase success when attaching artifacts to prompts meant for member agents.
  * **MCP Include/Exclude Tools**: Expanded `MCPTools` to allow you to specify tools to specifically include or exclude from all the available tools on an MCP server. This is very useful for limiting which tools the model has access to.
  * **Tool Decorator Async Support**: The `@tool()` decorator now supports async functions, including async pre and post-hooks.

  ## Bug Fixes:

  * **Default Chain-of-Thought Reasoning:** Fixed issue where reasoning would not default to manual CoT if the provided reasoning model was not capable of reasoning.
  * **Teams non-markdown responses**: Fixed issue with non-markdown responses in teams.
  * **Ollama tool choice:** Removed `tool_choice` from Ollama usage as it is not supported.
  * **Worklow session retrieval from storage**: Fixed `entity_id` mappings.
</Update>

<Update label="2025-03-25" description="v1.2.4">
  ## 1.2.4

  ## Improvements:

  * **Tool Choice on Teams**: Made `tool_choice` configurable.

  ## Bug Fixes:

  * **Sessions not created**: Made issue where sessions would not be created in existing tables without a migration be more visible. Please read the docs on [storage schema migrations](https://docs.agno.com/agents/storage).
  * **Todoist fixes**: Fixed `update_task` on `TodoistTools`.
</Update>

<Update label="2025-03-24" description="v1.2.3">
  ## 1.2.3

  ## Improvements:

  * **Teams Error Handling:** Improved the flow in cases where the model gets it wrong when forwarding tasks to members.
</Update>

<Update label="2025-03-24" description="v1.2.2">
  ## 1.2.2

  ## Bug Fixes:

  * **Teams Memory:** Fixed issues related to memory not persisting correctly across multiple sessions.
</Update>

<Update label="2025-03-24" description="v1.2.1">
  ## 1.2.1

  ## Bug Fixes:

  * **Teams Markdown**: Fixed issue with markdown in teams responses.
</Update>

<Update label="2025-03-24" description="v1.2.0">
  ## 1.2.0

  ## New Features:

  * **Financial Datasets Tools**: Added tools for [https://www.financialdatasets.ai/](https://www.financialdatasets.ai/).
  * **Docker Tools**: Added tools to manage local docker environments.

  ## Improvements:

  * **Teams Improvements:** Reasoning enabled for the team.
  * **MCP Simplification:** Simplified creation of `MCPTools` for connections to external MCP servers. See the updated [docs](https://docs.agno.com/tools/mcp#example%3A-filesystem-agent).

  ## Bug Fixes:

  * **Azure AI Factory:** Fix for a broken import in Azure AI Factory.
</Update>

<Update label="2025-03-23" description="v1.1.17">
  ## 1.1.17

  ## Improvements:

  * **Better Debug Logs**: Enhanced debug logs for better readability and clarity.
</Update>

<Update label="2025-03-22" description="v1.1.16">
  ## 1.1.16

  ## New Features:

  * **Async Qdrant VectorDB:** Implemented async support for Qdrant VectorDB, improving performance and efficiency.
  * **Claude Think Tool:** Introduced the Claude **Think tool**, following the specified implementation [guide.](https://www.anthropic.com/engineering/claude-think-tool)
</Update>

<Update label="2025-03-21" description="v1.1.15">
  ## 1.1.15

  ## Improvements:

  * **Tool Result Caching:** Added caching of selected searchers and scrapers. This is only intended for testing and should greatly improve iteration speed, prevent rate limits and reduce costs (where applicable) when testing agents. Applies to:
    * DuckDuckGoTools
    * ExaTools
    * FirecrawlTools
    * GoogleSearchtools
    * HackernewsTools
    * NewspaperTools
    * Newspaper4kTools
    * Websitetools
    * YFinanceTools
  * **Show tool calls**: Improved how tool calls are displayed when `print_response` and `aprint_response` is used. They are now displayed in a separate panel different from response panel. It can also be used in conjunction in `response_model`.
</Update>

<Update label="2025-03-20" description="v1.1.14">
  ## 1.1.14 - Teams Revamp

  ## New Features:

  * **Teams Revamp**: Announcing a new iteration of Agent teams with the following features:
    * Create a `Team` in one of 3 modes: “Collaborate”, “Coordinate” or “Route”.
    * Various improvements have been made that was broken with the previous teams implementation. Including returning structured output from member agents (for “route” mode), passing images, audio and video to member agents, etc.
    * It has added features like “agentic shared context” between team members and sharing of individual team member responses with other team members.
    * This also comes with a revamp of Agent and Team debug logs. Use `debug_mode=True` and `team.print_response(...)` to see it in action.
    * Find the docs [here](https://docs.agno.com/teams/introduction). Please look at the example implementations [here](https://github.com/agno-agi/agno/blob/c8e47d1643065a0a6ee795c6b063f8576a7a2ef6/cookbook/examples/teams).
    * This is the first release. Please give us feedback. Updates and improvements will follow.
    * Support for `Agent(team=[])` is still there, but deprecated (see below).
  * **LiteLLM:** Added [LiteLLM](https://www.litellm.ai/) support, both as a native implementation and via the `OpenAILike` interface.

  ## Improvements:

  * **Change structured\_output to response\_format:** Added `use_json_mode: bool = False` as a parameter of `Agent` and `Team`, which in conjunction with `response_model=YourModel`, is used to indicate whether the agent/team model should be forced to respond in json instead of (now default) structured output. Previous behaviour defaulted to “json-mode”, but since most models now support native structured output, we are now defaulting to native structured output. It is now also much simpler to work with response models, since now only `response_model` needs to be set. It is not necessary anymore to set `structured_output=True` to specifically get structured output from the model.
  * **Website Tools + Combined Knowledgebase:** Added functionality for `WebsiteTools` to also update combined knowledgebases.

  ## Bug Fixes:

  * **AgentMemory**: Fixed `get_message_pairs()` fetching incorrect messages.
  * **UnionType in Functions**: Fixed issue with function parsing where pipe-style unions were used in function parameters.
  * **Gemini Array Function Parsing**: Fixed issue preventing gemini function parsing to work in some MCP cases.

  ## Deprecations:

  * **Structured Output:** `Agent.structured_output` has been replaced by `Agent.use_json_mode`. This will be removed in a future major version release.
  * **Agent Team:** `Agent.team` is deprecated with the release of our new Teams implementation [here](https://docs.agno.com/teams/introduction). This will be removed in a future major version release.
</Update>

<Update label="2025-03-14" description="v1.1.13">
  ## 1.1.13

  ## Improvements:

  * **OpenAIResponses File Search**: Added support for the built-in [“File Search”](https://platform.openai.com/docs/guides/tools-file-search) function from OpenAI. This automatically uploads `File` objects attached to the agent prompt.
  * **OpenAIReponses web citations**: Added support to extract URL citations after usage of the built-in “Web Search” tool from OpenAI.
  * **Anthropic document citations**: Added support to extract document citations from Claude responses when `File` objects are attached to agent prompts.
  * **Cohere Command A**: Support and examples added for Coheres new flagship model

  ## Bug Fixes:

  * **Ollama tools**: Fixed issues with tools where parameters are not typed.
  * **Anthropic Structured Output**: Fixed issue affecting Anthropic and Anthropic via Azure where structured output wouldn’t work in some cases. This should make the experience of using structured output for models that don’t natively support it better overall. Also now works with enums as types in the Pydantic model.
  * **Google Maps Places**: Support from Google for Places API has been changed and this brings it up to date so we can continue to support “search places”.
</Update>

<Update label="2025-03-13" description="v1.1.12">
  ## 1.1.12

  ## New Features:

  * **Citations**: Improved support for capturing, displaying, and storing citations from models, with integration for Gemini and Perplexity.

  ## Improvements:

  * **CalComTools**: Improvement to tool Initialization.

  ## Bug Fixes:

  * **MemoryManager**: Limit parameter was added fixing a KeyError in MongoMemoryDb.
</Update>

<Update label="2025-03-13" description="v1.1.11">
  ## 1.1.11

  ## New Features:

  * **OpenAI Responses**: Added a new model implementation that supports OpenAI’s Responses API. This includes support for their [“websearch”](https://platform.openai.com/docs/guides/tools-web-search#page-top) built-in tool.
  * **Openweather API Tool:** Added tool to get real-time weather information.

  ## Improvements:

  * **Storage Refactor:** Merged agent and workflow storage classes to align storage better for agents, teams and workflows. This change is backwards compatible and should not result in any disruptions.
</Update>

<Update label="2025-03-12" description="v1.1.10">
  ## 1.1.10

  ## New Features:

  * **File Prompts**: Introduced a new `File` type that can be added to prompts and will be sent to the model providers. Only Gemini and Anthropic Claude supported for now.
  * **LMStudio:** Added support for [LMStudio](https://lmstudio.ai/) as a model provider. See the [docs](https://docs.agno.com/models/lmstudio).
  * **AgentQL Tools**: Added tools to support [AgentQL](https://www.agentql.com/) for connecting agents to websites for scraping, etc. See the [docs](https://docs.agno.com/tools/toolkits/agentql).
  * **Browserbase Tool:** Added [Browserbase](https://www.browserbase.com/) tool.

  ## Improvements:

  * **Cohere Vision**: Added support for image understanding with Cohere models. See [this cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/models/cohere/image_agent.py) to try it out.
  * **Embedder defaults logging**: Improved logging when using the default OpenAI embedder.

  ## Bug Fixes:

  * **Ollama Embedder**: Fix for getting embeddings from Ollama across different versions.
</Update>

<Update label="2025-03-06" description="v1.1.9">
  ## 1.1.9

  ## New Features:

  * **IBM Watson X:** Added support for IBM Watson X as a model provider. Find the docs [here](https://docs.agno.com/models/ibm-watsonx).
  * **DeepInfra**: Added support for [DeepInfra](https://deepinfra.com). Find the docs [here](https://docs.agno.com/models/deepinfra).
  * **Support for MCP**: Introducing `MCPTools` along with examples for using MCP with Agno agents.

  ## Bug Fixes:

  * **Mistral with reasoning**: Fixed cases where Mistral would fail when reasoning models from other providers generated reasoning content.
</Update>

<Update label="2025-03-03" description="v1.1.8">
  ## 1.1.8

  ## New Features:

  * **Video File Upload on Playground**: You can now upload video files and have a model interpret the video. This feature is supported only by select `Gemini` models with video processing capabilities.

  ## Bug Fixes:

  * **Huggingface**: Fixed multiple issues with the `Huggingface` model integration. Tool calling is now fully supported in non-streaming cases.
  * **Gemini**: Resolved an issue with manually setting the assistant role and tool call result metrics.
  * **OllamaEmbedder**: Fixed issue where no embeddings were returned.
</Update>

<Update label="2025-02-26" description="v1.1.7">
  ## 1.1.7

  ## New Features:

  * **Audio File Upload on Playground**: You can now upload audio files and have a model interpret the audio, do sentiment analysis, provide an audio transcription, etc.

  ## Bug Fixes:

  * **Claude Thinking Streaming**: Fix Claude thinking when streaming is active, as well as for async runs.
</Update>

<Update label="2025-02-24" description="v1.1.6">
  ## 1.1.6

  ## New Features:

  -**Claude 3.7 Support:** Added support for the latest Claude 3.7 Sonnet model

  ## Bug Fixes:

  -**Claude Tool Use**: Fixed an issue where tools and content could not be used in the same block when interacting with Claude models.
</Update>

<Update label="2025-02-24" description="v1.1.5">
  ## 1.1.5

  ## New Features:

  * **Audio Responses:** Agents can now deliver audio responses (both with streaming and non-streaming).

    * The audio is in the `agent.run_response.response_audio`.

    * This only works with `OpenAIChat` with the `gpt-4o-audio-preview` model. See [their docs](https://platform.openai.com/docs/guides/audio) for more on how it works. For example

      ```python
      from agno.agent import Agent
      from agno.models.openai import OpenAIChat
      from agno.utils.audio import write_audio_to_file

      agent = Agent(
          model=OpenAIChat(
              id="gpt-4o-audio-preview",
              modalities=["text", "audio"],  # Both text and audio responses are provided.
              audio={"voice": "alloy", "format": "wav"},
          ),
      )
      agent.print_response(
          "Tell me a 5 second story"
      )
      if agent.run_response.response_audio is not None:
          write_audio_to_file(
              audio=agent.run_response.response_audio.base64_audio, filename=str(filename)
          )
      ```

    * See the [audio\_conversation\_agent cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/playground/audio_conversation_agent.py) to test it out on the Agent Playground.

  * **Image understanding support for [Together.ai](http://Together.ai) and XAi**: You can now give images to agents using models from XAi and Together.ai.

  ## Improvements:

  * **Automated Tests:** Added integration tests for all models. Most of these will be run on each pull request, with a suite of integration tests run before a new release is published.
  * **Grounding and Search with Gemini:** [Grounding and Search](https://ai.google.dev/gemini-api/docs/grounding?lang=python) can be used to improve the accuracy and recency of responses from the Gemini models.

  ## Bug Fixes:

  * **Structured output updates**: Fixed various cases where native structured output was not used on models.
  * **Ollama tool parsing**: Fixed cases for Ollama with tools with optional parameters.
  * **Gemini Memory Summariser**: Fixed cases where Gemini models were used as the memory summariser.
  * **Gemini auto tool calling**: Enabled automatic tool calling when tools are provided, aligning behavior with other models.
  * **FixedSizeChunking issue with overlap:** Fixed issue where chunking would fail if overlap was set.
  * **Claude tools with multiple types**: Fixed an issue where Claude tools would break when handling a union of types in parameters.
  * **JSON response parsing**: Fixed cases where JSON model responses returned quoted strings within dictionary values.
</Update>

<Update label="2025-02-17" description="v1.1.4">
  ## 1.1.4

  ## Improvements:

  * **Gmail Tools**: Added `get_emails_by_thread` and `send_email_reply` methods to `GmailTools`.

  ## Bug Fixes:

  * **Gemini List Parameters**: Fixed an issue with functions using list-type parameters in Gemini.
  * **Gemini Safety Parameters**: Fixed an issue with passing safety parameters in Gemini.
  * **ChromaDB Multiple Docs:** Fixed an issue with loading multiple documents into ChromaDB.
  * **Agentic Chunking:** Fixed an issue where OpenAI was required for chunking even when a model was provided.
</Update>

<Update label="2025-02-16" description="v1.1.3">
  ## 1.1.3

  ## Bug Fixes:

  * **Gemini Tool-Call History**: Fixed an issue where Gemini rejected tool-calls from historic messages.
</Update>

<Update label="2025-02-15" description="v1.1.2">
  ## 1.1.2

  ## Improvements:

  * **Reasoning with o3 Models**: Reasoning support added for OpenAI’s o3 models.
  * **Gemini embedder update:** Updated the `GeminiEmbedder` to use the new [Google’s genai SDK](https://github.com/googleapis/python-genai). This update introduces a slight change in the interface:

    ```python
    # Before
    embeddings = GeminiEmbedder("models/text-embedding-004").get_embedding(
        "The quick brown fox jumps over the lazy dog."
    )

    # After
    embeddings = GeminiEmbedder("text-embedding-004").get_embedding(
        "The quick brown fox jumps over the lazy dog."
    )
    ```

  ## Bug Fixes:

  * **Singlestore Fix:** Fixed an issue where querying SingleStore caused the embeddings column to return in binary format.
  * **MongoDB Vectorstore Fix:** Fixed multiple issues in MongoDB, including duplicate creation and deletion of collections during initialization. All known issues have been resolved.
  * **LanceDB Fix:** Fixed various errors in LanceDB and added on\_bad\_vectors as a parameter.
</Update>

<Update label="2025-02-14" description="v1.1.1">
  ## 1.1.1

  ## Improvements:

  * **File / Image Uploads on Agent UI:** Agent UI now supports file and image uploads with prompts.
    * Supported file formats: `.pdf` , `.csv` , `.txt` , `.docx` , `.json`
    * Supported image formats: `.png` , `.jpeg` , `.jpg` , `.webp`
  * **Firecrawl Custom API URL**: Allowed users to set a custom API URL for Firecrawl.
  * **Updated `ModelsLabTools` Toolkit Constructor**: The constructor in `/libs/agno/tools/models_labs.py` has been updated to accommodate audio generation API calls. This is a breaking change, as the parameters for the `ModelsLabTools` class have changed. The `url` and `fetch_url` parameters have been removed, and API URLs are now decided based on the `file_type` provided by the user.

    ```python
    MODELS_LAB_URLS = {
        "MP4": "https://modelslab.com/api/v6/video/text2video",
        "MP3": "https://modelslab.com/api/v6/voice/music_gen",
        "GIF": "https://modelslab.com/api/v6/video/text2video",
    }

    MODELS_LAB_FETCH_URLS = {
        "MP4": "https://modelslab.com/api/v6/video/fetch",
        "MP3": "https://modelslab.com/api/v6/voice/fetch",
        "GIF": "https://modelslab.com/api/v6/video/fetch",
    }
    ```

    The `FileType` enum now includes `MP3` type:

    ```jsx
    class FileType(str, Enum):
        MP4 = "mp4"
        GIF = "gif"
        MP3 = "mp3"
    ```

  ## Bug Fixes:

  * **Gemini functions with no parameters:** Addressed an issue where Gemini would reject function declarations with empty properties.
  * **Fix exponential memory growth**: Fixed certain cases where the agent memory would grow exponentially.
  * **Chroma DB:** Fixed various issues related to metadata on insertion and search.
  * **Gemini Structured Output**: Fixed a bug where Gemini would not generate structured output correctly.
  * **MistralEmbedder:** Fixed issue with instantiation of `MistralEmbedder`.
  * **Reasoning**: Fixed an issue with setting reasoning models.
  * **Audio Response:** Fixed an issue with streaming audio artefacts to the playground.
</Update>

<Update label="2025-02-12" description="v1.1.0">
  ## 1.1.0 - Models Refactor and Cloud Support

  ## Model Improvements:

  * **Models Refactor**: A complete overhaul of our models implementation to improve on performance and to have better feature parity across models.
    * This improves metrics and visibility on the Agent UI as well.
    * All models now support async-await, with the exception of `AwsBedrock`.
  * **Azure AI Foundry**: We now support all models on Azure AI Foundry. Learn more [here](https://learn.microsoft.com/azure/ai-services/models)..
  * **AWS Bedrock Support**: Our redone AWS Bedrock implementation now supports all Bedrock models. It is important to note [which models support which features](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference-supported-models-features.html).
  * **Gemini via Google SDK**: With the 1.0.0 release of [Google's genai SDK](https://github.com/googleapis/python-genai) we could improve our previous implementation of `Gemini`. This will allow for easier integration of Gemini features in future.
  * **Model Failure Retries:** We added better error handling of third-party errors (e.g. Rate-Limit errors) and the agent will now optionally retry with exponential backoff if `exponential_backoff` is set to `True`.

  ## Other Improvements

  * **Exa Answers Support**: Added support for the [Exa answers](https://docs.exa.ai/reference/answer) capability.
  * **GoogleSearchTools**: Updated the name of `GoogleSearch` to `GoogleSearchTools` for consistency.

  ## Deprecation

  * Our `Gemini` implementation directly on the Vertex API has been replaced by the Google SDK implementation of `Gemini`.
  * Our `Gemini` implementation via the OpenAI client has been replaced by the Google SDK implementation of `Gemini`.
  * Our `OllamaHermes` has been removed as the implementation of `Ollama` was improved.

  ## Bug Fixes

  * **Team Members Names**: Fixed a bug where teams where team members have non-aphanumeric characters in their names would cause exceptions.
</Update>

<Update label="2025-02-07" description="v1.0.8">
  ## 1.0.8

  ## New Features:

  * **Perplexity Model**: We now support [Perplexity](https://www.perplexity.ai/) as a model provider.
  * **Todoist Toolkit:** Added a toolkit for managing tasks on Todoist.
  * **JSON Reader**: Added a JSON file reader for use in knowledge bases.

  ## Improvements:

  * **LanceDb**: Implemented `name_exists` function for LanceDb.

  ## Bug Fixes:

  * **Storage growth bug:** Fixed a bug with duplication of `run_messages.messages` for every run in storage.
</Update>

<Update label="2025-02-05" description="v1.0.7">
  ## 1.0.7

  ## New Features:

  * **Google Sheets Toolkit**: Added a basic toolkit for reading, creating and updating Google sheets.
  * **Weviate Vector Store**: Added support for Weviate as a vector store.

  ## Improvements:

  * **Mistral Async**: Mistral now supports async execution via `agent.arun()` and `agent.aprint_response()`.
  * **Cohere Async**: Cohere now supports async execution via `agent.arun()` and `agent.aprint_response()`.

  ## Bug Fixes:

  * **Retriever as knowledge source**: Added small fix and examples for using the custom `retriever` parameter with an agent.
</Update>

<Update label="2025-02-05" description="v1.0.6">
  ## 1.0.6

  ## New Features:

  * **Google Maps Toolkit**: Added a rich toolkit for Google Maps that includes business discovery, directions, navigation, geocode locations, nearby places, etc.
  * **URL reader and knowledge base**: Added reader and knowledge base that can process any URL and store the text contents in the document store.

  ## Bug Fixes:

  * **Zoom tools fix:** Zoom tools updated to include the auth step and other misc fixes.
  * **Github search\_repositories pagination**: Pagination did not work correctly and this was fixed.
</Update>

<Update label="2025-02-03" description="v1.0.5">
  ## 1.0.5

  ## New Features:

  * **Gmail Tools:** Add tools for Gmail, including mail search, sending mails, etc.

  ## Improvements:

  * **Exa Toolkit Upgrade:** Added `find_similar` to `ExaTools`
  * **Claude Async:** Claude models can now be used with `await agent.aprint_response()` and `await agent.arun()`.
  * **Mistral Vision:** Mistral vision models are now supported. Various examples were added to illustrate [example](https://github.com/agno-agi/agno/blob/main/cookbook/models/mistral/image_file_input_agent.py).
</Update>

<Update label="2025-02-02" description="v1.0.4">
  ## 1.0.4

  ## Bug Fixes:

  * **Claude Tool Invocation:** Fixed issue where Claude was not working with tools that have no parameters.
</Update>

<Update label="2025-01-31" description="v1.0.3">
  ## 1.0.3

  ## Improvements:

  * **OpenAI Reasoning Parameter:** Added a reasoning parameter to OpenAI models.
</Update>

<Update label="2025-01-31" description="v1.0.2">
  ## 1.0.2

  ## Improvements:

  * **Model Client Caching:** Made all models cache the client instantiation, improving Agno agent instantiation time
  * **XTools:** Renamed `TwitterTools` to `XTools` and updated capabilities to be compatible with Twitter API v2.

  ## Bug Fixes:

  * **Agent Dataclass Compatibility:** Removed `slots=True` from the agent dataclass decorator, which was not compatible with Python \< 3.10.
  * **AzureOpenAIEmbedder:** Made `AzureOpenAIEmbedder` a dataclass to match other embedders.
</Update>

<Update label="2025-01-31" description="v1.0.1">
  ## 1.0.1

  ## Improvement:

  * **Mistral Model Caching:** Enabled caching for Mistral models.
</Update>

<Update label="2025-01-30" description="v1.0.0">
  ## 1.0.0 - Agno

  This is the major refactor from `phidata` to `agno`, released with the official launch of Agno AI.

  See the [migration guide](../how-to/phidata-to-agno) for additional guidance.

  ## Interface Changes:

  * `phi.model.x` → `agno.models.x`

  * `phi.knowledge_base.x` → `agno.knowledge.x` (applies to all knowledge bases)

  * `phi.document.reader.xxx` → `agno.document.reader.xxx_reader` (applies to all document readers)

  * All Agno toolkits are now suffixed with `Tools`. E.g. `DuckDuckGo` → `DuckDuckGoTools`

  * Multi-modal interface updates:

    * `agent.run(images=[])` and `agent.print_response(images=[])` is now of type `Image`

      ```python
      class Image(BaseModel):
          url: Optional[str] = None  # Remote location for image
          filepath: Optional[Union[Path, str]] = None  # Absolute local location for image
          content: Optional[Any] = None  # Actual image bytes content
          detail: Optional[str] = None # low, medium, high or auto (per OpenAI spec https://platform.openai.com/docs/guides/vision?lang=node#low-or-high-fidelity-image-understanding)
          id: Optional[str] = None
      ```

    * `agent.run(audio=[])` and `agent.print_response(audio=[])` is now of type `Audio`

      ```python
      class Audio(BaseModel):
          filepath: Optional[Union[Path, str]] = None  # Absolute local location for audio
          content: Optional[Any] = None  # Actual audio bytes content
          format: Optional[str] = None
      ```

    * `agent.run(video=[])` and `agent.print_response(video=[])` is now of type `Video`

      ```python
      class Video(BaseModel):
          filepath: Optional[Union[Path, str]] = None  # Absolute local location for video
          content: Optional[Any] = None  # Actual video bytes content
      ```

    * `RunResponse.images` is now a list of type `ImageArtifact`

      ```python
      class ImageArtifact(Media):
          id: str
          url: str  # Remote location for file
          alt_text: Optional[str] = None
      ```

    * `RunResponse.audio` is now a list of type `AudioArtifact`

      ```python
      class AudioArtifact(Media):
          id: str
          url: Optional[str] = None  # Remote location for file
          base64_audio: Optional[str] = None  # Base64-encoded audio data
          length: Optional[str] = None
          mime_type: Optional[str] = None
      ```

    * `RunResponse.videos` is now a list of type `VideoArtifact`

      ```python
      class VideoArtifact(Media):
          id: str
          url: str  # Remote location for file
          eta: Optional[str] = None
          length: Optional[str] = None
      ```

    * `RunResponse.response_audio` is now of type `AudioOutput`

      ```python
      class AudioOutput(BaseModel):
          id: str
          content: str  # Base64 encoded
          expires_at: int
          transcript: str
      ```

  * Models:
    * `Hermes` → `OllamaHermes`
    * `AzureOpenAIChat` → `AzureOpenAI`
    * `CohereChat` → `Cohere`
    * `DeepSeekChat` → `DeepSeek`
    * `GeminiOpenAIChat` → `GeminiOpenAI`
    * `HuggingFaceChat` → `HuggingFace`

  * Embedders now all take `id` instead of `model` as a parameter. For example

    ```python
    db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

    knowledge_base = PDFUrlKnowledgeBase(
        urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
        vector_db=PgVector(
            table_name="recipes",
            db_url=db_url,
            embedder=OllamaEmbedder(id="llama3.2", dimensions=3072),
        ),
    )
    knowledge_base.load(recreate=True)
    ```

  * Agent Storage class
    * `PgAgentStorage` → `PostgresDbAgentStorage`
    * `SqlAgentStorage` → `SqliteDbAgentStorage`
    * `MongoAgentStorage` → `MongoDbAgentStorage`
    * `S2AgentStorage` → `SingleStoreDbAgentStorage`

  * Workflow Storage class
    * `SqlWorkflowStorage` → `SqliteDbWorkflowStorage`
    * `PgWorkflowStorage` → `PostgresDbWorkflowStorage`
    * `MongoWorkflowStorage` → `MongoDbWorkflowStorage`

  * Knowledge Base
    * `phi.knowledge.pdf.PDFUrlKnowledgeBase` → `agno.knowledge.pdf_url.PDFUrlKnowledgeBase`
    * `phi.knowledge.csv.CSVUrlKnowledgeBase` → `agno.knowledge.csv_url.CSVUrlKnowledgeBase`

  * Readers
    * `phi.document.reader.arxiv` → `agno.document.reader.arxiv_reader`
    * `phi.document.reader.docx` → `agno.document.reader.docx_reader`
    * `phi.document.reader.json` → `agno.document.reader.json_reader`
    * `phi.document.reader.pdf` → `agno.document.reader.pdf_reader`
    * `phi.document.reader.s3.pdf` → `agno.document.reader.s3.pdf_reader`
    * `phi.document.reader.s3.text` → `agno.document.reader.s3.text_reader`
    * `phi.document.reader.text` → `agno.document.reader.text_reader`
    * `phi.document.reader.website` → `agno.document.reader.website_reader`

  ## Improvements:

  * **Dataclasses:** Changed various instances of Pydantic models to dataclasses to improve the speed.
  * Moved `Embedder` class from pydantic to data class

  ## Removals

  * Removed all references to `Assistant`
  * Removed all references to `llm`
  * Removed the `PhiTools` tool
  * On the `Agent` class, `guidelines`, `prevent_hallucinations`, `prevent_prompt_leakage`, `limit_tool_access`, and `task` has been removed. They can be incorporated into the `instructions` parameter as you see fit.

  ## Bug Fixes:

  * **Semantic Chunking:** Fixed semantic chunking by replacing `similarity_threshold` param with `threshold` param.

  ## New Features:

  * **Evals for Agents:** Introducing Evals to measure the performance, accuracy, and reliability of your Agents.
</Update>


