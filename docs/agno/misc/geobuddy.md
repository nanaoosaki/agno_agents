---
title: GeoBuddy
category: misc
source_lines: 50083-50163
line_count: 80
---

# GeoBuddy
Source: https://docs.agno.com/examples/streamlit/geobuddy



GeoBuddy is a geography agent that analyzes images to predict locations based on visible cues such as landmarks, architecture, and cultural symbols.

### Key Capabilities

* Location Identification: Predicts location details from uploaded images
* Detailed Reasoning: Explains predictions based on visual cues
* User-Friendly Ul: Built with Streamlit for an intuitive experience

<video autoPlay muted controls className="w-full aspect-video" src="https://mintlify.s3.us-west-1.amazonaws.com/agno/videos/geobuddy.mp4" />

### Simple Examples to Try

* Landscape: A city skyline, a mountain panorama, or a famous landmark
* Architecture: Distinct buildings, bridges, or unique cityscapes
* Cultural Clues: Text on signboards, language hints, flags, or unique clothing

### Advanced Usage

Try providing images with subtle details, like store signs in different languages or iconic but less globally famous landmarks. GeoBuddy will attempt to reason more deeply about architectural style, environment (e.g. desert vs. tropical), and cultural references.

### Code

The complete code is available in the [Agno repository](https://github.com/agno-agi/agno).

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
    source .venv/bin/activate
    ```
  </Step>

  <Step title="Install Dependencies">
    ```bash
    pip install -r cookbook/examples/streamlit_apps/geobuddy/requirements.txt
    ```
  </Step>

  <Step title="Set up API Key">
    GeoBuddy uses the Google PaLM API for advanced image reasoning:

    ```bash
    export GOOGLE_API_KEY=***
    ```
  </Step>

  <Step title="Launch the App">
    ```bash
    streamlit run cookbook/examples/streamlit_apps/geobuddy/app.py
    ```
  </Step>

  <Step title="Open the App">
    Then, open [http://localhost:8501](http://localhost:8501) in your browser to start using GeoBuddy.
  </Step>
</Steps>

### Pro Tips

* High-Resolution Images: Clearer images with visible signboards or landmarks improve accuracy.
* Variety of Angles: Different angles (e.g. street-level vs. aerial views) can showcase unique clues.
* Contextual Clues: Sometimes minor details like license plates, local architectural elements or even vegetation can significantly influence the location guess.

Need help? Join our [Discourse community](https://community.agno.com) for support!


