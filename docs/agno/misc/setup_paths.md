---
title: Setup paths
category: misc
source_lines: 69653-69658
line_count: 5
---

# Setup paths
cwd = Path(__file__).parent
tmp_dir = cwd.joinpath("tmp")
tmp_dir.mkdir(parents=True, exist_ok=True)

