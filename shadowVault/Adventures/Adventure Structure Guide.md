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

## Adventure Types

Every adventure is one of three types, and the type decides where its folder lives:

- **One-shot** — designed for a single session, fully self-contained. Lives in `One-Shots/`.
- **Single adventure** — self-contained but multi-session. Lives in `Single Adventures/`.
- **Campaign adventure** — one chapter of a larger campaign. Lives inside its campaign's folder in `Campaigns/`, with a numeric prefix giving the play order.

A **campaign folder** adds two things around its adventures:

1. `00-campaign.md` — the campaign overview (use `campaign-template.md`): premise, the arc only the GM knows, recurring cast, and the linked adventure list. It is the campaign's entry point, exactly as `00-overview.md` is an adventure's.
2. A `Global/` folder — campaign-spanning reference material that no single adventure owns: bios of the recurring cast, campaign artifacts, recurring enemy stat blocks, region maps. It mirrors the adventure subfolders (`npcs/`, `items/`, `statblocks/`, `assets/`), each created when first needed.

The adventure structure itself (overview, acts, scenes, statblocks) is identical for all three types.

## Adventure Concepts

An adventure may begin as a **concept**: a file in `Adventures/Ideas/` built from `concept-template.md` and developed until `status: ready`. A ready concept answers everything the generation checklist below needs — premise, truth, stakes, cast, structure, opposition, rewards, constraints — so building the adventure from it requires inventing nothing load-bearing. After the build, the concept stays in `Ideas/` as the record of intent.

## Folder Layout

Shared, vault-wide resources live at the vault root; `Adventures/` holds only the adventures themselves:

```
<vault root>/
├── Templates/                        ← skeleton files, one subfolder per purpose
│   ├── adventure/                    ← overview-template.md, act-template.md
│   ├── campaign/                     ← campaign-template.md
│   ├── npc/                          ← npc-template.md
│   ├── monster/                      ← statblock-template.md
│   ├── item/                         ← item-template.md
│   └── location/                     ← location-template.md
├── Monsters/                         ← SHARED: reusable generic stat blocks
├── Items/                            ← SHARED: reusable generic items
└── Adventures/
    ├── Adventure Structure Guide.md  ← this guide
    ├── Ideas/                        ← adventure concepts in development (concept-template.md)
    ├── One-Shots/
    │   └── <Adventure Name>/         ← structure below
    ├── Single Adventures/
    │   └── <Adventure Name>/
    └── Campaigns/
        └── <Campaign Name>/
            ├── 00-campaign.md        ← campaign overview, always the entry point
            ├── Global/               ← campaign-spanning material (npcs/, items/, statblocks/, locations/, assets/)
            └── 01-<Adventure Name>/  ← one folder per adventure, numbered in play order
```

New template purposes (spells, locations, …) get their own `Templates/` subfolder.

Every `<Adventure Name>/` folder, regardless of type, contains:

```
<Adventure Name>/
├── 00-overview.md                ← always the entry point
├── 01-<act-name>.md              ← one file per act
├── 02-<act-name>.md
├── npcs/                         ← adventure-specific NPCs
├── items/                        ← adventure-specific items
├── statblocks/                   ← adventure-specific monsters/enemies
├── locations/                    ← adventure-specific reference locations (create when needed)
└── assets/                       ← maps, images, and player handouts
```

## Placement Rule

NPCs, items, stat blocks, locations, and assets live at the **narrowest scope that contains all their uses**:

1. **One adventure** → that adventure's own subfolder (`npcs/`, `items/`, `statblocks/`, `locations/`, `assets/`).
2. **Across a campaign** → the campaign's `Global/` folder — e.g. the recurring villain's bio, a campaign artifact like a legendary blade.
3. **Generic, reusable anywhere** → the vault-root `Monsters/` and `Items/` folders.

Before creating a file, check the wider scopes for an existing one. When something outgrows its scope (an adventure NPC becomes a recurring character), move the file up — wikilinks keep resolving.

## Naming Conventions

- **Numeric prefixes** (`00-`, `01-`, …) keep files in reading order and give the HTML generator a deterministic chapter sequence. `00-overview.md` is always the entry point.
- **kebab-case** for every filename inside an adventure folder (e.g. `01-the-hook.md`, `old-marta.md`).
- The **adventure folder itself** uses the human-readable title (e.g. `The Sunken Crypt/`).

## The Overview File (`00-overview.md`)

Every adventure starts here. Frontmatter:

```yaml
---
title: The Sunken Crypt
type: single-adventure   # one-shot | single-adventure | campaign-adventure
campaign: "[[00-campaign|The Black Sea]]"   # campaign adventures only, omit otherwise
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

### Hazards

Threats that cannot be fought — environmental dangers, unkillable set-pieces, curses — are **hazards**, not enemies. Their mechanics live inline in the scene as a compact block, and they get no stat block file; the enemy-wikilink rule applies only to Encounter blocks:

```markdown
**Hazard: Drowning Hands**
- Effect: DC 12 STR check or dragged under; 1d4 damage per round while submerged
- Counter: reaching a pillar ends the pull; a rope from shore gives advantage
```

### Handouts

Player-facing text handouts (letters, logbooks, puzzle faces) are markdown files in the adventure's `assets/` folder, named `handout-<name>.md` with `tags: [handout]`, and embedded or linked from the scene that hands them out. A handout contains no GM-only information — solutions stay in the act file.

## NPC Files

One page per NPC, covering: appearance, personality (including one mannerism to roleplay at the table), motivation, secrets, relationships, and a wikilink to a stat block if the NPC can fight. Placement follows the Placement Rule.

## Stat Block Files

One creature per file, with a `system:` frontmatter field. The stat format follows whatever system the adventure declares. Placement follows the Placement Rule: generic creatures (wolves, guards) in shared `Monsters/`, campaign-recurring creatures in the campaign's `Global/statblocks/`, unique horrors in the adventure's `statblocks/`.

## Item Files

One item per file (use `item-template.md`), with a `system:` frontmatter field where the item has mechanics. Placement follows the Placement Rule: generic items (potions, standard gear) in shared `Items/`, campaign artifacts in the campaign's `Global/items/`, adventure-specific treasure in the adventure's `items/`.

## Location Files

One location per file (use `location-template.md`) — for places that span scenes or adventures and deserve their own reference page: a ship, a town, a recurring stronghold. Placement follows the Placement Rule (a campaign's home ship lives in `Global/locations/`). A place that appears in a single scene needs no file — it lives in that scene's **Setup**.

## Generating an Adventure — Checklist

0. Decide the adventure type and place the folder accordingly — a ready concept in `Ideas/` supplies this and every following answer. For a campaign adventure whose campaign doesn't exist yet, create the campaign folder with `00-campaign.md` (from `campaign-template.md`) and `Global/` first.
1. Create the adventure folder (human-readable title) with `npcs/`, `items/`, `statblocks/`, `assets/` subfolders.
2. Copy the relevant files from `Templates/` and replace every `<placeholder>`.
3. Write `00-overview.md` first — premise, background, cast, structure.
4. Write one act file per act, scenes using the fixed skeleton.
5. Create NPC, stat block, item, and location files at the scope the Placement Rule dictates — checking wider scopes for existing files first.
6. Verify every wikilink resolves and every enemy in every encounter has a stat block file.
