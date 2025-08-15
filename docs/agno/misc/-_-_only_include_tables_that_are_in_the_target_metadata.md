---
title: -*- Only include tables that are in the target_metadata
category: misc
source_lines: 85750-85760
line_count: 10
---

# -*- Only include tables that are in the target_metadata
def include_name(name, type_, parent_names):
    if type_ == "table":
        return name in target_metadata.tables
    else:
        return True
...
```


