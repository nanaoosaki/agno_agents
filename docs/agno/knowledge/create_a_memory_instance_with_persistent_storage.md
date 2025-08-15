---
title: Create a memory instance with persistent storage
category: knowledge
source_lines: 69702-69804
line_count: 102
---

# Create a memory instance with persistent storage
memory_db = SqliteMemoryDb(table_name="memory", db_file="memory.db")
memory = Memory(db=memory_db)

team_with_memory = Team(
    name="Team with Memory",
    members=[agent1, agent2],
    memory=memory,
    enable_user_memories=True,
)

team_with_memory.print_response("Hi! My name is John Doe.")
team_with_memory.print_response("What is my name?")
```

## Session Summaries

To enable session summaries, set `enable_session_summaries=True` on the `Team`.

```python
from agno.team import Team
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory

team_with_session_summaries = Team(
    name="Team with Memory",
    members=[agent1, agent2],
    enable_session_summaries=True,
)

team_with_session_summaries.print_response("Hi! My name is John Doe and I live in New York City.")

session_summary = team_with_session_summaries.get_session_summary()
print("Session Summary: ", session_summary.summary)
```

## Examples

### Multi-Language Team

Let's walk through a simple example where we use different models to answer questions in different languages. The team consists of three specialized agents and the team leader routes the user's question to the appropriate language agent.

```python multilanguage_team.py
from agno.agent import Agent
from agno.models.deepseek import DeepSeek
from agno.models.mistral.mistral import MistralChat
from agno.models.openai import OpenAIChat
from agno.team.team import Team

english_agent = Agent(
    name="English Agent",
    role="You only answer in English",
    model=OpenAIChat(id="gpt-4o"),
)
chinese_agent = Agent(
    name="Chinese Agent",
    role="You only answer in Chinese",
    model=DeepSeek(id="deepseek-chat"),
)
french_agent = Agent(
    name="French Agent",
    role="You can only answer in French",
    model=MistralChat(id="mistral-large-latest"),
)

multi_language_team = Team(
    name="Multi Language Team",
    mode="route",
    model=OpenAIChat("gpt-4o"),
    members=[english_agent, chinese_agent, french_agent],
    show_tool_calls=True,
    markdown=True,
    description="You are a language router that directs questions to the appropriate language agent.",
    instructions=[
        "Identify the language of the user's question and direct it to the appropriate language agent.",
        "If the user asks in a language whose agent is not a team member, respond in English with:",
        "'I can only answer in the following languages: English, Chinese, French. Please ask your question in one of these languages.'",
        "Always check the language of the user's input before routing to an agent.",
        "For unsupported languages like Italian, respond in English with the above message.",
    ],
    show_members_responses=True,
)


if __name__ == "__main__":
    # Ask "How are you?" in all supported languages
    multi_language_team.print_response("Comment allez-vous?", stream=True)  # French
    multi_language_team.print_response("How are you?", stream=True)  # English
    multi_language_team.print_response("你好吗？", stream=True)  # Chinese
    multi_language_team.print_response("Come stai?", stream=True)  # Italian
```

### Content Team

Let's walk through another example where we use two specialized agents to write a blog post. The team leader coordinates the agents to write a blog post.

```python content_team.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.team import Team
from agno.tools.duckduckgo import DuckDuckGoTools

