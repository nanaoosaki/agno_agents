Love this. The quickest way to get a local, “good-enough” chat UI in pure Python—with mic input, text box, and file attachments—that you can wire to Agno is **Gradio**. It runs locally, needs no frontend work, and plays nicely with environment variables.

Below is a Cursor-ready plan with files you can paste in. I’ll assume you’ll call Agno agents from Python (single or multiple); we’ll add a tiny router so you can switch agents from a dropdown.

\[Inference] I’m using Gradio’s `Blocks` UI, OpenAI Whisper for speech-to-text, and a simple Agno agent stub. If your Agno version exposes different run/stream APIs, adjust the `call_agent()` function accordingly.

---

# 1) Project structure

```
agno-chat/
  ├─ app.py
  ├─ agents.py
  ├─ requirements.txt
  └─ .env.example
```

---

# 2) `requirements.txt`

```txt
python-dotenv==1.0.1
gradio==4.44.0
openai==1.35.14
agno==0.2.5           # [Unverified] Pin to the version you actually use
```

> If Agno’s package name/version differs in your setup, update this line. \[Unverified]

---

# 3) `.env.example`

```env
# Core LLM / STT
OPENAI_API_KEY=sk-...
# If you’ll use other APIs, add here and read with dotenv in agents.py or app.py:
# EXA_API_KEY=...
# NEBIUS_API_KEY=...
# ANYTHING_ELSE=...
```

Copy to `.env` and fill values.

---

# 4) `agents.py`

This is where you define and register your Agno agents. I’m showing:

* a trivial **EchoAgent** (works without external tools),
* a placeholder **ResearchAgent** (shows how you’d pass tools/keys).

```python
# agents.py
from dataclasses import dataclass
from typing import Dict, Any, Generator, Optional

# [Inference] Example Agno imports; adjust to your actual APIs
try:
    from agno.agent import Agent as AgnoAgent
    from agno.workflow import Workflow
except Exception:
    AgnoAgent = object
    Workflow = object

@dataclass
class ChatResult:
    text: str
    meta: Optional[Dict[str, Any]] = None

# --- Example 1: trivial echo agent (no external calls) ---
class EchoAgent:
    name = "EchoAgent"

    def run(self, prompt: str, files: Optional[list] = None) -> ChatResult:
        suffix = ""
        if files:
            suffix = f"  \n[received {len(files)} file(s)]"
        return ChatResult(text=f"Echo: {prompt}{suffix}")

# --- Example 2: placeholder Agno-powered agent ---
# Replace this with your actual Agno implementation
class ResearchAgent:
    name = "ResearchAgent"

    def __init__(self, tools: Optional[list] = None):
        self.tools = tools or []

    def run(self, prompt: str, files: Optional[list] = None) -> ChatResult:
        # [Inference] Replace with actual Agno agent execution and tool use.
        # For now, pretend we called a multi-stage workflow and got a string.
        lines = [f"Research summary for: {prompt}"]
        if files:
            lines.append(f"Files attached: {', '.join(files)}")
        lines.append("(Replace this with your real Agno workflow output)")
        return ChatResult(text="\n".join(lines))

# Registry of agents you can expose in the UI
AGENTS: Dict[str, Any] = {
    "EchoAgent": EchoAgent(),
    "ResearchAgent": ResearchAgent(),
}

def call_agent(agent_name: str, user_text: str, filepaths: Optional[list]) -> ChatResult:
    agent = AGENTS.get(agent_name)
    if not agent:
        return ChatResult(text=f"Unknown agent: {agent_name}")
    # If your real agent supports streaming, you can adapt this to return a generator.
    return agent.run(user_text, files=filepaths)
```

---

# 5) `app.py`

Gradio app with:

* chat area,
* text input,
* mic input (record → Whisper transcription → send),
* attachment input (images or any file),
* agent selector (dropdown),
* environment loading.

```python
# app.py
import os
from typing import List, Tuple, Optional
from dotenv import load_dotenv
import gradio as gr

# OpenAI for speech-to-text
from openai import OpenAI

from agents import call_agent, AGENTS

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    print("Warning: OPENAI_API_KEY not set. Audio transcription will fail.")

client = OpenAI(api_key=OPENAI_API_KEY)

def transcribe_audio(audio_path: str) -> str:
    """
    Transcribe microphone audio using OpenAI’s Whisper.
    """
    if not audio_path:
        return ""
    if not OPENAI_API_KEY:
        return "[Transcription failed: missing OPENAI_API_KEY]"
    # [Unverified] If you use the new STT model name, update 'whisper-1' accordingly.
    with open(audio_path, "rb") as f:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",  # [Unverified] use the model enabled for your account
            file=f
        )
    # .text is typical in current SDK; adjust if your SDK differs. [Unverified]
    return getattr(transcript, "text", str(transcript))

def normalize_files(files: Optional[List[gr.File]]) -> List[str]:
    """
    Convert Gradio file objects to filesystem paths.
    """
    if not files:
        return []
    paths = []
    for f in files:
        # f is either a dict-like or gradio object depending on version
        path = getattr(f, "name", None) or getattr(f, "path", None) or (f if isinstance(f, str) else None)
        if path:
            paths.append(path)
    return paths

def user_submit(
    message: str,
    history: List[Tuple[str, str]],
    agent_name: str,
    files: Optional[List[gr.File]],
):
    """
    Handle text submission.
    """
    history = history or []
    filepaths = normalize_files(files)
    history.append((message, ""))  # user message
    result = call_agent(agent_name, message, filepaths)
    history[-1] = (message, result.text)  # fill assistant response
    return history, gr.update(value=None), None  # clear text + files

def mic_submit(
    audio_path: str,
    history: List[Tuple[str, str]],
    agent_name: str,
    files: Optional[List[gr.File]],
):
    """
    Handle mic recording: transcribe, then route like a normal user message.
    """
    history = history or []
    text = transcribe_audio(audio_path)
    prompt = text or "[I recorded audio but no speech was detected.]"
    filepaths = normalize_files(files)
    history.append((prompt, ""))  # user message from mic
    result = call_agent(agent_name, prompt, filepaths)
    history[-1] = (prompt, result.text)
    return history, None  # no UI reset needed here

def clear_chat():
    return []

with gr.Blocks(title="Agno Chat (Local)") as demo:
    gr.Markdown("## Agno Chat — Local Dev UI")
    with gr.Row():
        agent_name = gr.Dropdown(
            choices=list(AGENTS.keys()),
            value=list(AGENTS.keys())[0],
            label="Agent"
        )
        clear_btn = gr.Button("Clear Chat")

    chat = gr.Chatbot(height=520, type="tuples", label="Conversation")

    with gr.Row():
        txt = gr.Textbox(placeholder="Type your message...", scale=4)
    with gr.Row():
        mic = gr.Audio(source="microphone", type="filepath", label="Mic input")
    with gr.Row():
        files = gr.Files(label="Attachments (images or files)", file_count="multiple")

    with gr.Row():
        send_btn = gr.Button("Send")
        mic_send_btn = gr.Button("Transcribe & Send")

    # Wire events
    send_btn.click(
        fn=user_submit,
        inputs=[txt, chat, agent_name, files],
        outputs=[chat, txt, files],
    )
    txt.submit(
        fn=user_submit,
        inputs=[txt, chat, agent_name, files],
        outputs=[chat, txt, files],
    )
    mic_send_btn.click(
        fn=mic_submit,
        inputs=[mic, chat, agent_name, files],
        outputs=[chat, mic],
    )
    clear_btn.click(fn=clear_chat, outputs=[chat])

if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", server_port=7860, inbrowser=True)
```

---

# 6) Run it locally (Cursor tasks)

1. Create the project and open in Cursor.
2. Create the four files exactly as above.
3. Copy `.env.example` to `.env` and fill your keys.
4. Create a venv and install deps:

   * macOS/Linux

     ```
     python3 -m venv .venv
     source .venv/bin/activate
     pip install -r requirements.txt
     ```
   * Windows (PowerShell)

     ```
     py -m venv .venv
     .venv\Scripts\Activate.ps1
     pip install -r requirements.txt
     ```
5. Run:

   ```
   python app.py
   ```
6. Your browser should open at `http://127.0.0.1:7860/`. Pick an agent and start chatting. Use the mic to record and send; add files via the uploader.

---

## Wiring in your real Agno agents

* Put your actual agent(s) into `agents.py`. For example, if you have a `Workflow` that streams events, you can adapt `call_agent()` to yield chunks and stream to Gradio by changing the handler to a generator. Minimal pattern:

```python
# in agents.py — streaming sketch [Unverified]
def call_agent_stream(agent_name: str, user_text: str, filepaths: Optional[list]):
    agent = AGENTS[agent_name]
    for event in agent.stream(user_text, files=filepaths):  # replace with your API
        yield event.delta_text  # or whatever field carries incremental tokens
```

Then, in `app.py`, replace the `user_submit` logic to append progressively. Gradio supports generator functions that yield partials to a single output; if you want token-stream UI, we can wire that next.

---

## Notes and options

* **STT model name**: I used `whisper-1`. If your account has a newer model (e.g., `gpt-4o-mini-transcribe`) use that. \[Unverified]
* **Attachments**: We pass file paths to your agent. If your tools want bytes, open and read in `call_agent`.
* **Auth and more APIs**: Add any API keys to `.env`; `dotenv` loads them at app start.
* **Styling**: You asked for simple; Gradio’s defaults are enough. We can later add avatars, system prompts, or a side panel for agent settings.

If you want me to switch this to Streamlit instead (it has a nice `st.chat_message` API), I can drop a parallel single-file version.
