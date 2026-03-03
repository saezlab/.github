# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository manages the GitHub organization landing page for [saezlab](https://github.com/saezlab). The `profile/README.md` is **auto-generated** — never edit it directly. Content is maintained in source files under `profile/src/` and compiled via a Python script.

There is a dual-repo setup: changes are cross-merged between the public [`.github`](https://github.com/saezlab/.github) and private [`.github-private`](https://github.com/saezlab/.github-private) repos.

## Build Commands

```bash
# Install dependencies (requires Poetry)
poetry install

# Regenerate profile/README.md from source files
poetry run python profile/src/update_md.py

# Preview rendered markdown locally (opens a local server)
poetry run grip profile/README.md
```

## Architecture

**Source files** (edit these):
- `profile/src/README.main.md` — Header and intro text
- `profile/src/README.foot.md` — Footer (content after the resource table)
- `profile/src/resources.yaml` — Resource definitions: the `order` list controls which resources appear and in what order; the `resources` map holds each resource's description (`main`) and `links` (pairs of `[type, URL]`)

**Generation scripts:**
- `profile/src/update_md.py` — Reads the YAML + template files and produces `profile/README.md` as an HTML table (4-column layout with logos, titles, and icon links)
- `profile/src/from_md.py` — Reverse-engineers `resources.yaml` from a rendered README snapshot

**Assets:**
- `profile/logos/` — Resource logos (named lowercase, `.svg` or `.png`)
- `profile/icons/` — SVG icons for link types (16px height)

Images are referenced via absolute raw GitHub URLs (`https://raw.githubusercontent.com/saezlab/.github/main/profile/...`).

## Adding a New Resource

1. Add a logo to `profile/logos/` (lowercase name, `.svg` or `.png`)
2. In `profile/src/resources.yaml`: add the name to the `order` list and define it under `resources` with `main` (description) and `links` (list of `[type, URL]` pairs)
3. Run `poetry run python profile/src/update_md.py`
4. Preview with `poetry run grip profile/README.md`

Link types: `home`, `python`, `r`, `package:PYPI`, `package:BIOC`, `package:CYTO`, `docs-py`, `docs-r`, `article`, `main`, `cytoscape`.

## Cross-Merge Workflow

After pushing changes, sync between public and private repos:
```bash
git remote add public git@github.com:saezlab/.github.git  # one-time setup
git pull public main
git push origin main
```
