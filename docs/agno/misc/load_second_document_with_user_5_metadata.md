---
title: Load second document with user_5 metadata
category: misc
source_lines: 16433-16439
line_count: 6
---

# Load second document with user_5 metadata
knowledge_base.load_document(
    path=downloaded_cv_paths[4],
    metadata={"user_id": "alex_rivera", "document_type": "cv", "year": 2025},
)

