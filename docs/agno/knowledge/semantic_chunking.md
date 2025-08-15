---
title: Semantic Chunking
category: knowledge
source_lines: 67318-67330
line_count: 12
---

# Semantic Chunking
Source: https://docs.agno.com/reference/chunking/semantic



Semantic chunking is a method of splitting documents into smaller chunks by analyzing semantic similarity between text segments using embeddings.
It uses the chonkie library to identify natural breakpoints where the semantic meaning changes significantly, based on a configurable similarity threshold.
This helps preserve context and meaning better than fixed-size chunking by ensuring semantically related content stays together in the same chunk, while splitting occurs at meaningful topic transitions.

<Snippet file="chunking-semantic.mdx" />


