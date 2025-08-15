---
title: Load second document with user_4 metadata
category: misc
source_lines: 16427-16433
line_count: 6
---

# Load second document with user_4 metadata
knowledge_base.load_document(
    path=downloaded_cv_paths[3],
    metadata={"user_id": "casey_jordan", "document_type": "cv", "year": 2025},
)

