# Adventure Structure Guide — Design

**Date:** 2026-07-10
**Status:** Approved by Steffen

## Goal

Create a system-agnostic adventure structure guide plus template files in the `Adventures/` folder of the shadowVault. The guide defines the ground rules an AI (or human) must follow when generating adventures, so every adventure in the vault has the same predictable structure. The markdown files are the source of truth and will later be compiled into an interactive HTML version of each adventure.

## Requirements

- **System-agnostic:** the structure applies to any RPG system; the system is declared per adventure in metadata.
- **Language:** guide and adventure content in English.
- **Chapters = story acts:** adventures are broken into acts following the dramatic arc; no fixed act skeleton is prescribed — the number and nature of acts is up to each adventure. Acts contain scenes as subchapters.
- **Overview as entry point** containing premise & hook, GM background/truth, cast & factions list, practical metadata, and the linked chapter structure.
- **Stat blocks are referenced, never inlined:** encounters name enemies and wikilink to stat block files.
- **Hybrid support-file storage:** adventure-specific NPCs/monsters/assets live inside the adventure folder; generic reusable monsters live in a shared `Adventures/Monsters/` folder.
- **Wikilinks** for all cross-references (HTML link resolution deferred until the pipeline is built).
- **Deliverable packaging:** one guide document + a `_templates/` folder with skeleton files.

## Folder layout

```
Adventures/
├── Adventure Structure Guide.md      ← the guide itself
├── _templates/
│   ├── overview-template.md
│   ├── act-template.md
│   ├── npc-template.md
│   └── statblock-template.md
├── Monsters/                         ← shared reusable generic stat blocks
└── <Adventure Name>/                 ← one folder per adventure (human-readable title)
    ├── 00-overview.md                ← always the entry point
    ├── 01-<act-name>.md              ← one file per act, numeric prefix = reading order
    ├── 02-<act-name>.md
    ├── npcs/                         ← adventure-specific NPCs
    ├── statblocks/                   ← adventure-specific monsters/enemies
    └── assets/                       ← maps, handouts, images
```

Naming rules:

- Numeric prefixes (`00-`, `01-`, …) give deterministic ordering for Obsidian and the future HTML generator.
- kebab-case filenames inside adventure folders; the adventure folder itself uses the human-readable title.

## File specifications

### 00-overview.md

Frontmatter:

```yaml
---
title: <Adventure Title>
system: <RPG system>
levels: <level range>
party-size: <e.g. 3-5>
sessions: <expected count>
status: draft   # draft | ready | played
tags: [adventure]
---
```

Sections, in order:

1. **Premise & Hook** — 2–4 sentence pitch: what it's about, why the characters get involved, tone.
2. **Background (GM only)** — the truth behind events; the secret history explaining everything.
3. **Cast & Factions** — table of every NPC/monster/faction: name (wikilink), role, one-liner, where they appear.
4. **Structure** — linked chapter list: each act as `[[01-act-name|Act 1: Name]]` with subchapter bullets (its scenes) and a one-line description each. Navigation backbone for the future HTML.

### Act files (01-*.md and up)

- **Act Overview:** purpose of the act, state of the world when it starts, ways it can end.
- **Scenes**, each with a fixed skeleton:
  - **Purpose** — why the scene exists in the story
  - **Trigger** — what brings the party here
  - **Setup** — situation, location, who is present
  - **What Happens** — events, encounters, discoveries
  - **Outcomes** — possible results and which scene/act each leads to

Standardized callouts inside scenes:

- `> [!quote] Read Aloud` — player-facing boxed text
- `> [!tip] GM Guidance` — pacing advice, "if the players do X" branches, check suggestions
- `> [!warning]` — pitfalls (deadly fights, dead ends)

Encounters are compact blocks: enemies (wikilinks to stat blocks only), numbers, tactics, terrain, treasure.

### NPC files

One page per NPC: appearance, personality (a mannerism to roleplay), motivation, secrets, relationships, wikilink to a stat block if they can fight.

### Stat block files

One creature per file, `system:` frontmatter field; stat format follows the declared system. Generic reusable creatures go to shared `Monsters/`; adventure-specific ones to the adventure's `statblocks/`.

### Templates

The four `_templates/` files mirror these specs exactly, with placeholder text (`<like this>`) that the AI replaces during generation.

## Out of scope (for now)

- The HTML generation pipeline (link resolution strategy decided later; wikilinks used meanwhile).
- A worked example adventure — the first real generated adventure will serve as the example.
