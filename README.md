# Linda Agentic Engine

A comprehensive multi-agent AI system built with the Agno framework, featuring different levels of agent complexity and capabilities.

## 🤖 Agent Levels

### Level 1 Agent (`level_1_agent.py`)
- Basic agent with tools and instructions
- Simple financial queries using YFinance tools

### Level 2 Agent (`level_2_agent.py`) 
- Agents with knowledge base and storage
- Uses ChromaDB for vector storage (Windows-friendly)
- Loads external documentation for context

### Level 3 Agent (`level_3_agent.py`)
- Agents with memory and reasoning capabilities
- Persistent memory using SQLite
- Advanced reasoning tools

### Level 4 Agent (`level_4_agent.py`)
- Multi-agent teams with collaboration
- **Triple-hybrid model approach:**
  - **Web Search Agent**: Gemini 2.0 Flash (cost-effective research)
  - **Finance Agent**: GPT-4o (superior financial analysis)
  - **Team Coordinator**: Claude Sonnet 4 (advanced reasoning)
- Comprehensive financial analysis and portfolio recommendations

### Specialized Agents

#### Migraine Analysis Agent (`migraine_agent.py`)
- Specialized medical analysis assistant
- Uses Gemini 2.0 Flash for cost-effective processing
- Knowledge base from migraine medical documentation
- Patient memory storage and pattern analysis

## 🛠️ Setup

1. **Install Dependencies**
   ```bash
   pip install agno python-dotenv
   ```

2. **Environment Variables**
   Create a `.env` file with your API keys:
   ```
   OPENAI_API_KEY=your_openai_key_here
   GEMINI_API_KEY=your_gemini_key_here
   ANTHROPIC_API_KEY=your_anthropic_key_here
   ```

3. **Virtual Environment**
   ```bash
   python -m venv uv
   .\uv\Scripts\Activate  # Windows
   ```

## 🚀 Usage

### Run Individual Agents
```bash
python level_1_agent.py
python level_2_agent.py
python level_3_agent.py
python level_4_agent.py
python migraine_agent.py
```

### Level 4 Agent Features
- **Financial Analysis**: Comprehensive stock analysis (AAPL, GOOGL, MSFT)
- **News Research**: Real-time market sentiment analysis
- **Portfolio Recommendations**: AI-powered allocation strategies
- **Risk Assessment**: Multi-dimensional risk evaluation

## 🧠 AI Model Strategy

The system uses a **hybrid multi-model approach** to optimize for:
- **Performance**: Best-in-class models for specific tasks
- **Cost**: Efficient model selection based on complexity
- **Reliability**: Redundancy across different AI providers

### Model Selection:
- **GPT-4o**: Complex financial analysis and calculations
- **Claude Sonnet 4**: Advanced reasoning and synthesis
- **Gemini 2.0 Flash**: Fast, cost-effective general tasks

## 📊 Features

- ✅ Multi-agent collaboration
- ✅ Persistent memory and storage
- ✅ Vector databases for knowledge retrieval
- ✅ Real-time web search and news analysis
- ✅ Financial data integration (YFinance)
- ✅ Medical document analysis
- ✅ Reasoning and analysis tools
- ✅ Cross-platform compatibility

## 🔧 Technical Stack

- **Framework**: Agno (AI agent framework)
- **Vector DB**: ChromaDB (Windows-friendly)
- **Memory**: SQLite-based persistence
- **APIs**: OpenAI, Anthropic, Google AI
- **Tools**: YFinance, DuckDuckGo, ReasoningTools

## 📈 Performance

The Level 4 triple-hybrid team delivers institutional-quality analysis:
- **Speed**: ~30-130 seconds for comprehensive reports
- **Accuracy**: Multi-model validation and cross-checking
- **Cost**: Optimized model selection for efficiency

## 🛡️ Security

- Environment variable management for API keys
- Local data storage and processing
- No hardcoded credentials

## 📄 License

MIT License - Feel free to use and modify for your projects.

## 🤝 Contributing

Contributions welcome! Please feel free to submit pull requests or open issues for improvements.