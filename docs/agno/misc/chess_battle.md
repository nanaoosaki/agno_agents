---
title: Chess Battle
category: misc
source_lines: 49830-49911
line_count: 81
---

# Chess Battle
Source: https://docs.agno.com/examples/streamlit/chess-team



Chess Battle is a chess application where multiple AI agents collaborate to play chess against each other, demonstrating the power of multi-agent systems in complex game environments.

### Key Capabilities

* Multi-Agent System: Features White and Black Piece Agents for move selection
* Move Validation: Dedicated Legal Move Agent ensures game rule compliance
* Game Coordination: Master Agent oversees the game flow and end conditions
* Interactive UI: Built with Streamlit for real-time game visualization

<video autoPlay muted controls className="w-full aspect-video" src="https://mintlify.s3.us-west-1.amazonaws.com/agno/videos/chess-team.mp4" />

### System Components

* White Piece Agent: Strategizes and selects moves for white pieces
* Black Piece Agent: Controls and determines moves for black pieces
* Legal Move Agent: Validates all proposed moves against chess rules
* Master Agent: Coordinates the game flow and monitors game status

### Advanced Features

The system demonstrates complex agent interactions where each AI component has a specific role. The agents communicate and coordinate to create a complete chess-playing experience, showcasing how multiple specialized AIs can work together effectively.

### Code

The complete code is available in the [Agno repository](https://github.com/agno-agi/agno/tree/main/cookbook/examples/streamlit_apps/chess_team).

### Usage

<Steps>
  <Step title="Clone the repository">
    ```bash
    git clone https://github.com/agno-agi/agno.git
    cd agno
    ```
  </Step>

  <Step title="Create a Virtual Environment">
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
    ```
  </Step>

  <Step title="Install Dependencies">
    ```bash
    pip install -r cookbook/examples/streamlit_apps/chess_team/requirements.txt
    ```
  </Step>

  <Step title="Set up API Key">
    The Chess Team Agent uses the Anthropic API for agent reasoning:

    ```bash
    export ANTHROPIC_API_KEY=your_api_key_here
    ```
  </Step>

  <Step title="Launch the App">
    ```bash
    streamlit run cookbook/examples/streamlit_apps/chess_team/app.py
    ```
  </Step>

  <Step title="Open the App">
    Then, open [http://localhost:8501](http://localhost:8501) in your browser to start watching the AI agents play chess.
  </Step>
</Steps>

### Pro Tips

* Watch Complete Games: Observe full matches to understand agent decision-making
* Monitor Agent Interactions: Pay attention to how agents communicate and coordinate

Need help? Join our [Discourse community](https://agno.link/community) for support!


