#!/usr/bin/env python3
import re
from pathlib import Path
import collections

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
md_files = list(DOCS.rglob("*.md"))

# Duplicate H1 titles
titles = collections.defaultdict(list)
h1_re = re.compile(r"^#\s+(.+)$", re.M)
for p in md_files:
    txt = p.read_text(encoding="utf-8", errors="replace")
    m = h1_re.search(txt)
    if m:
        titles[m.group(1).strip()].append(p)

dupes = {k:v for k,v in titles.items() if len(v) > 1}
if dupes:
    print("Duplicate H1 titles found:")
    for t, paths in dupes.items():
        print(f"- {t}")
        for pp in paths:
            print(f"  - {pp.relative_to(ROOT)}")
    print()

# Full-width punctuation (informational)
fw_re = re.compile(r"[，。；：、】【】（）《》“”‘’]")
fw_hits = [p for p in md_files if fw_re.search(p.read_text(encoding="utf-8", errors="replace"))]
if fw_hits:
    print("Files containing full-width punctuation:")
    for p in fw_hits[:200]:
        print(f"- {p.relative_to(ROOT)}")
    if len(fw_hits) > 200:
        print(f"... and {len(fw_hits)-200} more")
    print()

print("Validation completed.")
