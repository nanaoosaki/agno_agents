---
title: Agentic Knowledge Filters
category: knowledge
source_lines: 59086-59192
line_count: 106
---

# Agentic Knowledge Filters

Agentic filtering lets the Agent automatically extract filter criteria from your query text, making the experience more natural and interactive.

## Step 1: Attach Metadata

There are two ways to attach metadata to your documents:

1. **Attach Metadata When Initializing the Knowledge Base**

   ```python
   knowledge_base = PDFKnowledgeBase(
       path=[
           {
               "path": "path/to/cv1.pdf",
               "metadata": {
                   "user_id": "jordan_mitchell",
                   "document_type": "cv",
                   "year": 2025,
               },
           },
           # ... more documents ...
       ],
       vector_db=vector_db,
   )
   knowledge_base.load(recreate=True)
   ```

2. **Attach Metadata When Loading Documents One by One**

   ```python
   # Initialize the PDFKnowledgeBase
   knowledge_base = PDFKnowledgeBase(
       vector_db=vector_db,
       num_documents=5,
   )

   # Load first document with user_1 metadata
   knowledge_base.load_document(
       path=path/to/cv1.pdf,
       metadata={"user_id": "jordan_mitchell", "document_type": "cv", "year": 2025},
       recreate=True,  # Set to True only for the first run, then set to False
   )

   # Load second document with user_2 metadata
   knowledge_base.load_document(
       path=path/to/cv2.pdf,
       metadata={"user_id": "taylor_brooks", "document_type": "cv", "year": 2025},
   )
   ```

***

## How It Works

When you enable agentic filtering (`enable_agentic_knowledge_filters=True`), the Agent analyzes your query and applies filters based on the metadata it detects.

**Example:**

```python
agent = Agent(
    knowledge=knowledge_base,
    search_knowledge=True,
    enable_agentic_knowledge_filters=True,
)
agent.print_response(
    "Tell me about Jordan Mitchell's experience and skills with jordan_mitchell as user id and document type cv",
    markdown=True,
)
```

In this example, the Agent will automatically use:

* `user_id = "jordan_mitchell"`
* `document_type = "cv"`

***

## 🌟 See Agentic Filters in Action!

Experience how agentic filters automatically extract relevant metadata from your query.

![Agentic Filters in Action](https://mintlify.s3.us-west-1.amazonaws.com/agno/images/agentic_filters.png)

*The Agent intelligently narrows down results based on your query.*

***

## When to Use Agentic Filtering

* When you want a more conversational, user-friendly experience.
* When users may not know the exact filter syntax.

## Try It Out!

* Enable `enable_agentic_knowledge_filters=True` on your Agent.
* Ask questions naturally, including filter info in your query.
* See how the Agent narrows down results automatically!

***

## Developer Resources

* [Agentic filtering](https://github.com/agno-agi/agno/blob/main/cookbook/agent_concepts/knowledge/filters/pdf/agentic_filtering.py)


