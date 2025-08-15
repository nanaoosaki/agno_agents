---
title: -*- Get the vectordb
category: misc
source_lines: 61689-61691
line_count: 2
---

# -*- Get the vectordb
db = Chroma(embedding_function=OpenAIEmbeddings(), persist_directory=str(chroma_db_dir))
