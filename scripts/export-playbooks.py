#!/usr/bin/env python3
"""Copies the desk playbooks into the StockYan connector, which serves them with get_desk_playbook so that any AI app
using the connector gets the NEPSE Trading Desk method without installing the skill.
Usage: python3 scripts/export-playbooks.py <stockyan-backend>/src/mcp/playbooks"""
import pathlib, re, sys

skill = pathlib.Path(__file__).resolve().parent.parent / "skills" / "nepse-trading-desk"
out = pathlib.Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
for old in out.glob("*.md"): old.unlink()
body = re.sub(r"^---\n.*?\n---\n", "", (skill / "SKILL.md").read_text(), flags=re.S)
note = ("> Served by the StockYan connector. Where this text points to a file such as `references/desks/03-analyst-team.md`,\n"
        "> fetch it with `get_desk_playbook(\"03-analyst-team\")` (the file name without folder or `.md`).\n\n")
(out / "overview.md").write_text(note + body.lstrip())
for f in sorted((skill / "references").rglob("*.md")):
    (out / f.name).write_text(f.read_text())
print("\n".join(sorted(p.stem for p in out.glob("*.md"))))
