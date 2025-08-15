---
title: Memory V2
category: knowledge
source_lines: 58755-58838
line_count: 83
---

# Memory V2
Source: https://docs.agno.com/faq/memoryv2



Starting with Agno version 1.4.0, **Memory V2** is now the default memory for the Agno Agent. This replaces the previous `AgentMemory` and `TeamMemory` classes which is now deprecated but still available to use.

Memory V2 is a more powerful and flexible memory system that allows you to manage message history, session summaries, and long-term user memories.

## How to Continue Using AgentMemory (Memory V1)

If you want to continue using `AgentMemory` and avoid breaking changes, you can do so by updating your imports. By default, the Agent now uses the `Memory` class:

```python
from agno.memory.v2 import Memory
```

To use the legacy AgentMemory class instead, import it like this:

```python
from agno.memory import AgentMemory

agent = Agent(
    memory=AgentMemory()
)
```

## Key Memory V2 Changes

* **Accessing Messages:**

  * **Before:**
    ```python
    agent.memory.messages
    ```
  * **Now:**
    ```python
    [run.messages for run in agent.memory.runs]
    # or
    agent.get_messages_for_session()
    ```

* **User Memories:**

  * **Before:**

    ```python
    from agno.memory import AgentMemory

    memory = AgentMemory(create_user_memories=True)
    agent = Agent(memory=memory)
    ```

  * **Now:**

    ```python
    from agno.memory.v2 import Memory

    memory = Memory()
    agent = Agent(create_user_memories=True, memory=memory) or team = Team(create_user_memories=True, memory=memory)
    ```

* **Session Summaries:**

  * **Before:**

    ```python
    from agno.memory import AgentMemory

    memory = AgentMemory(create_session_summary=True)
    agent = Agent(memory=memory)
    ```

  * **Now:**

    ```python
    from agno.memory.v2 import Memory

    memory = Memory()
    agent = Agent(enable_session_summaries=True, memory=memory) or team = Team(enable_session_summaries=True, memory=memory)
    ```


