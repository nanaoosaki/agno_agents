---
title: Create the agent
category: misc
source_lines: 8784-8833
line_count: 49
---

# Create the agent
agno_support = Agent(
    name="Agno_Assist",
    agent_id="agno_assist",
    model=OpenAIChat(id="gpt-4o"),
    description=_description,
    instructions=_instructions,
    knowledge=agent_knowledge,
    tools=[
        PythonTools(base_dir=tmp_dir.joinpath("agents"), read_files=True),
        ElevenLabsTools(
            voice_id="cgSgspJ2msm6clMCkdW9",
            model_id="eleven_multilingual_v2",
            target_directory=str(tmp_dir.joinpath("audio").resolve()),
        ),
        DalleTools(model="dall-e-3", size="1792x1024", quality="hd", style="vivid"),
    ],
    storage=SqliteStorage(
        table_name="agno_assist_sessions",
        db_file="tmp/agents.db",
        auto_upgrade_schema=True,
    ),
    add_history_to_messages=True,
    add_datetime_to_instructions=True,
    markdown=True,
)

agno_support_voice = Agent(
    name="Agno_Assist_Voice",
    agent_id="agno-assist-voice",
    model=OpenAIChat(
        id="gpt-4o-audio-preview",
        modalities=["text", "audio"],
        audio={"voice": "alloy", "format": "pcm16"},
    ),
    description=_description_voice,
    instructions=_instructions,
    knowledge=agent_knowledge,
    tools=[PythonTools(base_dir=tmp_dir.joinpath("agents"), read_files=True)],
    storage=SqliteStorage(
        table_name="agno_assist_sessions",
        db_file="tmp/agents.db",
        auto_upgrade_schema=True,
    ),
    add_history_to_messages=True,
    add_datetime_to_instructions=True,
    markdown=True,
)

