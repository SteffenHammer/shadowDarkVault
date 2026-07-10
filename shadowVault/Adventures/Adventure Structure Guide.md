---
title: Adventure Structure Guide
tags: [guide]
---

# Adventure Structure Guide

Ground rules for every adventure in this vault, whether written by hand or generated with AI. Follow this guide exactly: the predictable structure is what makes adventures easy to navigate in Obsidian and machine-readable for the planned interactive HTML export.

## Core Principles

1. **System-agnostic.** The structure works for any RPG system. The system an adventure targets is declared in its overview frontmatter, never assumed.
2. **English.** All adventure content and metadata is written in English.
3. **Markdown is the source of truth.** These files will later be compiled into an interactive HTML version of the adventure. Keep the structure clean and consistent so tooling can rely on it.
4. **Chapters are story acts.** Adventures are broken down by dramatic arc, not by location. Locations and scenes live inside the act they belong to.
5. **No fixed act skeleton.** Use as many acts as the story needs. The guide defines what an act file must contain, not how many acts exist.
6. **Stat blocks are referenced, never inlined.** An encounter names its enemies and wikilinks their stat block files. Stats never appear inside act files.
7. **Wikilinks everywhere.** All cross-references between files use `[[wikilinks]]`. (The HTML pipeline will resolve them later.)

## Folder Layout

```
Adventures/
├── Adventure Structure Guide.md      ← this guide
├── _templates/                       ← skeleton files, copy when generating
│   ├── overview-template.md
│   ├── act-template.md
│   ├── npc-template.md
│   └── statblock-template.md
├── Monsters/                         ← SHARED: reusable generic stat blocks
└── <Adventure Name>/                 ← one folder per adventure
    ├── 00-overview.md                ← always the entry point
    ├── 01-<act-name>.md              ← one file per act
    ├── 02-<act-name>.md
    ├── npcs/                         ← adventure-specific NPCs
    ├── statblocks/                   ← adventure-specific monsters/enemies
    └── assets/                       ← maps, handouts, images
```

## Naming Conventions

- **Numeric prefixes** (`00-`, `01-`, …) keep files in reading order and give the HTML generator a deterministic chapter sequence. `00-overview.md` is always the entry point.
- **kebab-case** for every filename inside an adventure folder (e.g. `01-the-hook.md`, `old-marta.md`).
- The **adventure folder itself** uses the human-readable title (e.g. `The Sunken Crypt/`).

## The Overview File (`00-overview.md`)

Every adventure starts here. Frontmatter:

```yaml
---
title: The Sunken Crypt
system: Shadowdark
levels: 1-3
party-size: 3-5
sessions: 2-3
status: draft   # draft | ready | played
tags: [adventure]
---
```

Then exactly these four sections, in order:

1. **Premise & Hook** — a 2–4 sentence pitch: what the adventure is about, why the characters get involved, and the expected tone.
2. **Background (GM only)** — the truth behind events; the secret history that explains everything the players will uncover.
3. **Cast & Factions** — a table of every NPC, monster, and faction: name (wikilink), role, one-liner, where they appear.
4. **Structure** — the linked chapter list. Each act appears as `[[01-act-name|Act 1: Name]]` followed by subchapter bullets listing its scenes with a one-line description each. This section is the navigation backbone for the HTML export.

## Act Files (`01-*.md` and up)

Each act file opens with an **Act Overview**: the purpose of the act, the state of the world when it starts, and the ways it can end.

The rest of the file is **Scenes**. Every scene uses this fixed skeleton:

- **Purpose** — why this scene exists in the story
- **Trigger** — what brings the party here
- **Setup** — the situation, location, and who is present
- **What Happens** — the meat: events, encounters, discoveries
- **Outcomes** — possible results and which scene or act each one leads to

### Callouts

Use these standardized callouts inside scenes:

- `> [!quote] Read Aloud` — player-facing boxed text, read or paraphrase aloud
- `> [!tip] GM Guidance` — pacing advice, "if the players do X" branches, suggested checks
- `> [!warning]` — pitfalls: deadly fights, potential dead ends

### Encounters

Encounters are compact blocks inside a scene's **What Happens** section:

```markdown
**Encounter: Spiders in the Rafters**
- Enemies: 3 × [[giant-spider]], 1 × [[broodmother]]
- Tactics: spiders drop on the rear rank; broodmother stays on the ceiling
- Terrain: webs count as difficult ground; braziers can be toppled
- Treasure: 40 gp in a web-wrapped corpse, [[potion-of-healing]]
```

Enemies are always wikilinks to stat block files — never inline stats.

## NPC Files

One page per NPC in the adventure's `npcs/` folder, covering: appearance, personality (including one mannerism to roleplay at the table), motivation, secrets, relationships, and a wikilink to a stat block if the NPC can fight.

## Stat Block Files

One creature per file, with a `system:` frontmatter field. The stat format follows whatever system the adventure declares.

**Hybrid storage rule:**
- **Generic, reusable** creatures (wolves, guards, giant spiders) live in the shared `Adventures/Monsters/` folder.
- **Adventure-specific** creatures (the named villain, unique horrors) live in the adventure's own `statblocks/` folder, keeping the adventure self-contained for export.

Before creating a new stat block, check whether `Monsters/` already has it.

## Generating an Adventure — Checklist

1. Create the adventure folder (human-readable title) with `npcs/`, `statblocks/`, `assets/` subfolders.
2. Copy the relevant files from `_templates/` and replace every `<placeholder>`.
3. Write `00-overview.md` first — premise, background, cast, structure.
4. Write one act file per act, scenes using the fixed skeleton.
5. Create NPC files for every named character in the cast table.
6. Create stat blocks in `statblocks/`, or link existing ones from `Monsters/`.
7. Verify every wikilink resolves and every enemy in every encounter has a stat block file.
