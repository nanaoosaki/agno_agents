# 🤖 Agno Chat Interface

A local, multi-modal chat interface for Agno AI agents built with Gradio. Features text input, voice transcription, file attachments, and agent switching.

## ✨ Features

- **Multi-modal Input**: Text, microphone (Whisper transcription), and file attachments
- **Agent Selection**: Switch between different Agno agents via dropdown
- **Real-time Chat**: Interactive chat history with user/assistant conversation flow
- **File Support**: Upload and analyze images, PDFs, documents
- **Voice Input**: Record audio messages with automatic transcription
- **Modern UI**: Clean Gradio interface with custom styling

## 🚀 Quick Start

### 1. Setup Environment

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure API Keys

```bash
# Copy environment template
cp env_example.txt .env

# Edit .env file with your API keys
# At minimum, you need:
OPENAI_API_KEY=sk-your-key-here
```

### 3. Run the Application

```bash
python app.py
```

The interface will open automatically in your browser at `http://127.0.0.1:7860`

## 🔧 Available Agents

- **EchoAgent**: Simple test agent that echoes your input
- **ResearchAgent**: Web-enabled research assistant with DuckDuckGo search
- **GeneralAgent**: General purpose AI assistant for various tasks

## 📝 Usage

1. **Select Agent**: Choose your preferred AI agent from the dropdown
2. **Text Chat**: Type messages and press Enter or click Send
3. **Voice Input**: Click the microphone, record your message, then click "Transcribe & Send"
4. **File Attachments**: Upload files using the file input area
5. **Clear Chat**: Use the Clear Chat button to start a new conversation

## 🛠️ Configuration

### Environment Variables

Create a `.env` file with the following variables:

```env
# Required for all agents
OPENAI_API_KEY=sk-your-openai-api-key

# Optional - add as needed for specific agents
EXA_API_KEY=your-exa-key
ANTHROPIC_API_KEY=your-anthropic-key
GROQ_API_KEY=your-groq-key
```

### Adding Custom Agents

To add your own Agno agents, edit `agents.py`:

1. Create a new agent class following the existing pattern
2. Add it to the `AGENTS` registry
3. Restart the application

Example:
```python
class MyCustomAgent:
    name = "MyCustomAgent"
    description = "Description of what this agent does"
    
    def __init__(self):
        self.agent = Agent(
            name="My Custom Agent",
            model=OpenAIChat(id="gpt-4o-mini-2024-07-18"),
            instructions="Your custom instructions here",
            tools=[YourCustomTools()],
        )
    
    def run(self, prompt: str, files: Optional[List[str]] = None) -> ChatResult:
        # Your implementation here
        pass

# Add to registry
AGENTS["MyCustomAgent"] = MyCustomAgent()
```

## 🔍 Troubleshooting

### Common Issues

1. **"Agno imports failed"**: Install Agno with `pip install agno`
2. **"Audio transcription disabled"**: Set `OPENAI_API_KEY` in `.env`
3. **"Agent not available"**: Check API keys and Agno installation
4. **Import errors**: Ensure all dependencies are installed with `pip install -r requirements.txt`

### Debug Mode

To run with more verbose logging, modify `app.py`:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 📦 Dependencies

- `agno>=0.2.5` - The Agno AI framework
- `gradio>=4.44.0` - Web UI framework
- `openai>=1.35.14` - For Whisper transcription
- `python-dotenv>=1.0.1` - Environment variable loading

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project follows the same license as the parent Agno framework.

## 🔗 Links

- [Agno Documentation](https://docs.agno.com/)
- [Gradio Documentation](https://gradio.app/docs/)
- [OpenAI API Documentation](https://platform.openai.com/docs/)