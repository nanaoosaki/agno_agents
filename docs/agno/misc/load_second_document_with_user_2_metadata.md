---
title: Load second document with user_2 metadata
category: misc
source_lines: 16415-16421
line_count: 6
---

# Load second document with user_2 metadata
knowledge_base.load_document(
    path=downloaded_cv_paths[1],
    metadata={"user_id": "taylor_brooks", "document_type": "cv", "year": 2025},
)

