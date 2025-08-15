---
title: What are Teams?
category: misc
source_lines: 69545-69611
line_count: 66
---

# What are Teams?
Source: https://docs.agno.com/teams/introduction

Build autonomous multi-agent systems with Agno Teams.

A Team is a collection of Agents (or other sub-teams) that work together to accomplish tasks. Teams can either **"coordinate"**, **"collaborate"** or **"route"** to solve a task.

A `Team` has a list of `members` that can be instances of `Agent` or `Team`.

```python
from agno.team import Team
from agno.agent import Agent

team = Team(members=[
    Agent(name="Agent 1", role="You answer questions in English"),
    Agent(name="Agent 2", role="You answer questions in Chinese"),
    Team(name="Team 1", role="You answer questions in French"),
])
```

The team will transfer tasks to the members depending on the `mode` of the team.

<Note>
  It is recommended to specify the `name` and the `role` fields of the team member, for better identification by the team leader.
</Note>

## Modes

### Route Mode

In [**Route Mode**](/teams/route), the team leader routes the user's request to the most appropriate team member based on the content of the request. The member's response is returned directly to the user and the team leader doesn't interpret/transform the response.

<Note>
  In `async` execution, if more than once member is transferred to at once by the team leader, these members are executed concurrently.
</Note>

### Coordinate Mode

In [**Coordinate Mode**](/teams/coordinate), the team leader delegates tasks to team members and synthesizes their outputs into a cohesive response. The team leader can send to multiple members at once, or one after the other depending on the request and what the model decides is most appropriate.

<Note>
  In `async` execution, if more than once member is transferred to at once by the team leader, these members are executed concurrently.
</Note>

### Collaborate Mode

In [**Collaborate Mode**](/teams/collaborate), all team members are given the same task and the team leader synthesizes their outputs into a cohesive response.

<Note>
  In `async` execution, all the members are executed concurrently.
</Note>

## Team Memory and History

Teams can maintain memory of previous interactions, enabling contextual awareness:

```python
from agno.team import Team

team_with_memory = Team(
    name="Team with Memory",
    members=[agent1, agent2],
    add_history_to_messages=True,
    num_history_runs=5,
)

