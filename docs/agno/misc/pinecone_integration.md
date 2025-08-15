---
title: Pinecone Integration
category: misc
source_lines: 33105-33178
line_count: 73
---

# Pinecone Integration
Source: https://docs.agno.com/examples/concepts/vectordb/pinecone



## Code

```python cookbook/agent_concepts/vector_dbs/pinecone_db.py
from os import getenv

from agno.agent import Agent
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.pineconedb import PineconeDb

api_key = getenv("PINECONE_API_KEY")
index_name = "thai-recipe-index"

vector_db = PineconeDb(
    name=index_name,
    dimension=1536,
    metric="cosine",
    spec={"serverless": {"cloud": "aws", "region": "us-east-1"}},
    api_key=api_key,
)

knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=vector_db,
)

knowledge_base.load(recreate=False, upsert=True)

agent = Agent(
    knowledge=knowledge_base,
    show_tool_calls=True,
    search_knowledge=True,
    read_chat_history=True,
)

agent.print_response("How do I make pad thai?", markdown=True)
```

## Usage

<Steps>
  <Snippet file="create-venv-step.mdx" />

  <Step title="Set your API key">
    ```bash
    export PINECONE_API_KEY=xxx
    ```
  </Step>

  <Step title="Install libraries">
    ```bash
    pip install -U pinecone-client pypdf openai agno
    ```
  </Step>

  <Step title="Run Agent">
    <CodeGroup>
      ```bash Mac
      python cookbook/agent_concepts/vector_dbs/pinecone_db.py
      ```

      ```bash Windows
      python cookbook/agent_concepts/vector_dbs/pinecone_db.py
      ```
    </CodeGroup>
  </Step>
</Steps>


