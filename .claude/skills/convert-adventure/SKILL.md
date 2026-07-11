---
name: convert-adventure
description: Convert a pen-&-paper RPG adventure (any system, any language) into this vault's adventure structure, stat blocks converted to Shadowdark. Argument: path to the source folder or files.
disable-model-invocation: true
---

# Convert Adventure

Convert a source adventure into a vault adventure. `shadowVault/Adventures/Adventure Structure Guide.md` is the single source of truth for the target structure — read it first and follow it exactly. This skill defines only the conversion process.

The conversion is **faithful**: the source's story, tone, and mechanics survive restructuring and translation intact. Invent nothing silently — see Gaps.

## Gaps

A **gap** is content the target structure demands but the source doesn't supply: a scene without Outcomes, an NPC without a motivation, an ambiguous act boundary, an enemy no stat block covers.

Routine conversion work is not a gap: translating, writing connective phrasing, snapping DCs to the Shadowdark ladder, deriving ability modifiers from a creature's fiction.

Everything else — anything adding story content or mechanics the source lacks — is asked, never invented. Collect the gaps for the file you are about to write and put them to the user in one AskUserQuestion round, each gap with a concrete proposal as the recommended option.

## Process

1. **Extract.** Get every source into markdown in the scratchpad, whatever its format:
   - Formats the Read tool handles natively (PDF, markdown, plain text, images): read directly.
   - Office formats it can't (`.odt`, `.docx`): use the extractor bundled with this skill — `python scripts/extract_odt.py <file.odt>` — extending it if a new office format appears.
   - Non-document sources (a video, a web page): fetch the transcript or page text and save that as the extracted text.

   Done when every source is either extracted as text or catalogued as an asset (images, maps, handouts).

2. **Inventory.** Read all extracted text end to end and table every act, scene, location, NPC, creature, item, puzzle, and read-aloud passage with its source file. The inventory is the completeness contract the final step verifies against. Done when nothing in the source is missing from it.

3. **Mapping checkpoint.** Present the proposed conversion and wait for approval:
   - adventure type and target location (one-shot / single adventure / campaign adventure — and for the latter, which campaign, creating its folder if new)
   - English adventure title and the act/scene breakdown (source section → target file)
   - cast, creature, item, and location lists, each entry placed per the guide's Placement Rule (shared / campaign `Global/` / adventure) — checking wider scopes for existing files first; non-fightable threats marked as hazards (inline mechanics, no stat block)
   - asset and handout plan: kebab-case target names and which scene links each
   - all gaps found so far

   Translation of names: descriptive names are translated ("Schädelklippe" → "Skull Cliff"); invented proper nouns keep their spelling ("Rauthorn").

4. **Write.** Follow the guide's "Generating an Adventure" checklist: scaffold the folder, then overview → act files → NPCs → stat blocks per [shadowdark-statblocks.md](shadowdark-statblocks.md) → copy assets into `assets/`. Resolve each file's gaps per the Gaps rule before writing it. A file is done when every inventory row assigned to it appears in it.

5. **Verify.** Reconcile the finished adventure against the inventory and report the reconciliation: every inventory row placed (or dropped with the user's sign-off), every wikilink resolving, every encounter enemy owning a stat block file, every asset copied and linked from a scene. Done at zero unaccounted rows and zero broken links.
