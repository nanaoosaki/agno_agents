---
title: Load second document with user_3 metadata
category: misc
source_lines: 16421-16427
line_count: 6
---

# Load second document with user_3 metadata
knowledge_base.load_document(
    path=downloaded_cv_paths[2],
    metadata={"user_id": "morgan_lee", "document_type": "cv", "year": 2025},
)

