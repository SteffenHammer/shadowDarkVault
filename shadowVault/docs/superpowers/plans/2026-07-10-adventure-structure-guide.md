# Adventure Structure Guide Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create the Adventure Structure Guide and its four template files in `Adventures/` so AI-generated adventures follow one predictable, HTML-export-ready structure.

**Architecture:** Pure markdown deliverables inside an Obsidian vault. One prose guide document states the ground rules; a `_templates/` folder holds skeleton files with `<placeholder>` text that mirror the guide's specs exactly. A shared `Adventures/Monsters/` folder is seeded with a README explaining the hybrid stat-block rule.

**Tech Stack:** Obsidian-flavored markdown (frontmatter, wikilinks, callouts). No code, no test framework — verification is file existence plus a consistency read-through.

**Spec:** `docs/superpowers/specs/2026-07-10-adventure-structure-guide-design.md`

## Global Constraints

- All content in English.
- System-agnostic: RPG system is declared per adventure via `system:` frontmatter, never assumed.
- Wikilinks (`[[target]]`) for all cross-references between adventure files.
- Stat blocks are referenced, never inlined in act files.
- Numeric prefixes (`00-`, `01-`, …) on adventure files; kebab-case filenames inside adventure folders.
- Working directory: `D:\Private\obsidian\shadowDarkVault\shadowVault` (paths below relative to it).
- Do NOT commit `.obsidian/` — stage only the files each task names.

---

### Task 1: The guide document

**Files:**
- Create: `Adventures/Adventure Structure Guide.md`

**Interfaces:**
- Produces: the canonical rules that Tasks 2–4's templates must mirror (section names, frontmatter keys, callout types, scene skeleton labels: Purpose / Trigger / Setup / What Happens / Outcomes).

- [ ] **Step 1: Write the guide file**

Write `Adventures/Adventure Structure Guide.md` with exactly this content:

````markdown
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
````

- [ ] **Step 2: Verify the file exists and headings are intact**

Run: `ls "Adventures/Adventure Structure Guide.md"` and check the file renders in Obsidian without broken formatting (callout examples display as code, tree block intact).
Expected: file listed; all `##` sections present: Core Principles, Folder Layout, Naming Conventions, The Overview File, Act Files, NPC Files, Stat Block Files, Generating an Adventure — Checklist.

- [ ] **Step 3: Commit**

```bash
git add "Adventures/Adventure Structure Guide.md"
git commit -m "docs: add adventure structure guide"
```

---

### Task 2: Overview template

**Files:**
- Create: `Adventures/_templates/overview-template.md`

**Interfaces:**
- Consumes: overview spec from Task 1 (frontmatter keys `title, system, levels, party-size, sessions, status, tags`; sections Premise & Hook / Background / Cast & Factions / Structure).

- [ ] **Step 1: Write the template**

Write `Adventures/_templates/overview-template.md` with exactly this content:

````markdown
---
title: <Adventure Title>
system: <RPG system, e.g. Shadowdark>
levels: <level range, e.g. 1-3>
party-size: <e.g. 3-5>
sessions: <expected session count, e.g. 2-3>
status: draft
tags: [adventure]
---

# <Adventure Title>

## Premise & Hook

<2–4 sentence pitch: what the adventure is about, why the characters get involved, expected tone.>

## Background (GM only)

<The truth behind events — the secret history that explains everything the players will uncover.>

## Cast & Factions

| Name | Role | One-liner | Appears in |
| ---- | ---- | --------- | ---------- |
| [[<npc-file>\|<NPC Name>]] | <ally/villain/wildcard> | <one sentence> | <Act 1, Act 3> |
| [[<monster-file>\|<Monster Name>]] | <threat> | <one sentence> | <Act 2> |

## Structure

- [[01-<act-name>|Act 1: <Act Title>]] — <one-line description>
	- <Scene 1 name> — <one-line description>
	- <Scene 2 name> — <one-line description>
- [[02-<act-name>|Act 2: <Act Title>]] — <one-line description>
	- <Scene 1 name> — <one-line description>
````

- [ ] **Step 2: Verify**

Run: `ls Adventures/_templates/overview-template.md`
Expected: file listed; frontmatter keys match the guide exactly (`title, system, levels, party-size, sessions, status, tags`).

- [ ] **Step 3: Commit**

```bash
git add Adventures/_templates/overview-template.md
git commit -m "docs: add adventure overview template"
```

---

### Task 3: Act template

**Files:**
- Create: `Adventures/_templates/act-template.md`

**Interfaces:**
- Consumes: act spec from Task 1 (Act Overview; scene skeleton Purpose / Trigger / Setup / What Happens / Outcomes; callouts `[!quote] Read Aloud`, `[!tip] GM Guidance`, `[!warning]`; encounter block format).

- [ ] **Step 1: Write the template**

Write `Adventures/_templates/act-template.md` with exactly this content:

````markdown
---
title: <Act Title>
act: <act number>
tags: [act]
---

# Act <N>: <Act Title>

## Act Overview

- **Purpose:** <what this act accomplishes in the story>
- **State of the world:** <what is true when this act begins>
- **Ways it can end:** <the exits from this act and where each leads>

## Scene: <Scene Name>

- **Purpose:** <why this scene exists in the story>
- **Trigger:** <what brings the party here>
- **Setup:** <situation, location, who is present>

### What Happens

<Events, discoveries, and encounters. Use the callouts and encounter blocks below as needed.>

> [!quote] Read Aloud
> <Player-facing boxed text — read or paraphrase aloud.>

> [!tip] GM Guidance
> <Pacing advice, "if the players do X" branches, suggested checks.>

> [!warning]
> <Pitfalls: deadly fight, potential dead end.>

**Encounter: <Encounter Name>**
- Enemies: <N> × [[<statblock-file>]], <N> × [[<statblock-file>]]
- Tactics: <how the enemies fight>
- Terrain: <features that matter in the fight>
- Treasure: <loot, wikilink items if they have files>

### Outcomes

- <Possible result> → leads to [[<file>|<scene or act>]]
- <Possible result> → leads to [[<file>|<scene or act>]]

## Scene: <Next Scene Name>

<Repeat the scene skeleton for every scene in this act.>
````

- [ ] **Step 2: Verify**

Run: `ls Adventures/_templates/act-template.md`
Expected: file listed; scene skeleton labels match the guide exactly (Purpose, Trigger, Setup, What Happens, Outcomes).

- [ ] **Step 3: Commit**

```bash
git add Adventures/_templates/act-template.md
git commit -m "docs: add adventure act template"
```

---

### Task 4: NPC + stat block templates and shared Monsters folder

**Files:**
- Create: `Adventures/_templates/npc-template.md`
- Create: `Adventures/_templates/statblock-template.md`
- Create: `Adventures/Monsters/README.md`

**Interfaces:**
- Consumes: NPC and stat block specs from Task 1 (NPC: appearance, personality with mannerism, motivation, secrets, relationships, stat block link; stat block: `system:` frontmatter, one creature per file, hybrid storage rule).

- [ ] **Step 1: Write the NPC template**

Write `Adventures/_templates/npc-template.md` with exactly this content:

````markdown
---
title: <NPC Name>
tags: [npc]
---

# <NPC Name>

- **Role:** <ally / villain / wildcard / patron>
- **Appearance:** <one or two vivid details>
- **Personality:** <temperament, plus one mannerism to roleplay at the table>
- **Motivation:** <what they want and why>
- **Secrets:** <what they hide; when and how it can come out>
- **Relationships:** <ties to other NPCs and factions, as wikilinks>
- **Stat block:** [[<statblock-file>]] <!-- only if the NPC can fight -->
````

- [ ] **Step 2: Write the stat block template**

Write `Adventures/_templates/statblock-template.md` with exactly this content:

````markdown
---
title: <Creature Name>
system: <RPG system this stat block is written for>
tags: [statblock]
---

# <Creature Name>

<One-line description of the creature and how it behaves.>

```
<Stat block in the declared system's native format.>
```

- **Found in:** <shared Monsters/ if generic, or the adventure's statblocks/ if unique>
````

- [ ] **Step 3: Write the Monsters folder README**

Write `Adventures/Monsters/README.md` with exactly this content:

```markdown
# Shared Monsters

Reusable, generic stat blocks (wolves, guards, giant spiders) shared across all adventures — one creature per file, kebab-case filenames, using [[statblock-template]].

Adventure-specific creatures (named villains, unique horrors) do NOT belong here; they live in the adventure's own `statblocks/` folder.

Before creating a new stat block for a generic creature, check whether it already exists here.
```

- [ ] **Step 4: Verify**

Run: `ls Adventures/_templates/ Adventures/Monsters/`
Expected: `_templates/` contains all four templates (overview, act, npc, statblock); `Monsters/` contains `README.md`.

- [ ] **Step 5: Commit**

```bash
git add Adventures/_templates/npc-template.md Adventures/_templates/statblock-template.md Adventures/Monsters/README.md
git commit -m "docs: add npc/statblock templates and shared Monsters folder"
```
