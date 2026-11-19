#!/usr/bin/env python3
"""Checks the skill and the manifests: frontmatter, links to reference files, and JSON files. Run: python3 scripts/validate.py"""
import json, pathlib, re, sys

root = pathlib.Path(__file__).resolve().parent.parent
errors = []

for f in [".claude-plugin/marketplace.json", ".claude-plugin/plugin.json", ".mcp.json", "gemini-extension.json"]:
    try:
        json.loads((root / f).read_text())
    except Exception as e:  # noqa: BLE001
        errors.append(f"{f}: {e}")

for skill in sorted((root / "skills").iterdir()):
    md = skill / "SKILL.md"
    if not md.exists():
        errors.append(f"{skill.name}: no SKILL.md"); continue
    text = md.read_text()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        errors.append(f"{skill.name}: no frontmatter"); continue
    fm = dict(re.findall(r"^(\w+):\s*(.+)$", m.group(1), re.M))
    if fm.get("name") != skill.name:
        errors.append(f"{skill.name}: frontmatter name {fm.get('name')!r} must match the folder")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", fm.get("name", "")) or len(fm.get("name", "")) > 64:
        errors.append(f"{skill.name}: name must be lowercase-with-hyphens, 64 characters or fewer")
    if not (20 <= len(fm.get("description", "")) <= 1024):
        errors.append(f"{skill.name}: description must be 20 to 1024 characters")
    for ref in sorted(set(re.findall(r"`(references/[\w.-]+\.md)`", text))):
        if not (skill / ref).exists():
            errors.append(f"{skill.name}: SKILL.md points to missing {ref}")
    for ref in (skill / "references").glob("*.md"):
        for other in re.findall(r"`references/([\w.-]+\.md)`", ref.read_text()):
            if not (skill / "references" / other).exists():
                errors.append(f"{skill.name}/{ref.name}: points to missing references/{other}")

print("\n".join(errors) if errors else "ok: skills and manifests are valid")
sys.exit(1 if errors else 0)
