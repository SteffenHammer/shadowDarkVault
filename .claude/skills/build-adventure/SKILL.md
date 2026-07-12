---
name: build-adventure
description: Build a full vault adventure from a ready concept produced by develop-adventure-idea, following the Adventure Structure Guide and templates, stat blocks in Shadowdark format. Argument: the concept file in Adventures/Ideas/ (path or name).
disable-model-invocation: true
---

# Build Adventure

Turn a ready concept from `shadowVault/Adventures/Ideas/` into a complete, playable adventure. `shadowVault/Adventures/Adventure Structure Guide.md` is the single source of truth for the target structure — read it first and follow it exactly, including its "Generating an Adventure" checklist. This skill defines only the build process.

The build is **faithful to the concept**: every section of the concept is a contract. Expanding it is the job — writing scenes, read-alouds, and outcomes around the concept's beats, statting creatures from their fiction, choosing DCs from the Shadowdark ladder, naming minor scenery — all of that is routine build work. What is *not* routine is changing what the concept says or adding load-bearing story content it doesn't contain — see Gaps.

## Gaps

A **gap** is anything load-bearing the build needs but the concept doesn't supply: a scene whose outcome the Structure demands but the concept leaves open, a cast member without a motivation, a reward without a defined effect, a contradiction discovered between concept sections.

Deviations count as gaps too: if expanding a beat reveals it doesn't work as written (a clock that can't tick, an encounter that can't be survived at the declared levels), propose the fix — never silently reinterpret the concept.

Collect the gaps for the file you are about to write and put them to the user in one AskUserQuestion round, each gap with a concrete proposal as the recommended option.

## Process

1. **Ingest.** Read the concept end to end. If its `status` is not `ready`, stop and point the user at `develop-adventure-idea` to finish it. Then read the Structure Guide, and for a campaign adventure: the campaign's `00-campaign.md`, its `Global/` folder, and the overviews of prior adventures — the build must reuse existing NPCs, stat blocks, items, and locations instead of duplicating them, and must keep continuity with what the table actually played.

2. **Build-time flags.** Sweep the concept for everything it explicitly defers to the build: party-keyed content ("roster drafted against the real party"), names left open, "decide/fix at build" and "flag for the build" notes. Resolve them all in one AskUserQuestion round before anything is written — party roster (character names, classes, levels), open names, deferred forms. Done when no deferred decision remains open.

3. **Blueprint checkpoint.** Derive the full file plan from the concept and present it for approval before writing:
   - target folder per the guide's Adventure Types (for a campaign adventure: the next numeric prefix in its campaign)
   - act/scene breakdown: each Structure beat mapped to an act file and its scenes
   - cast → NPC files; Opposition Palette → stat block files vs. inline hazards (non-fightable threats are hazards — no stat block); Rewards → item files; Locations → location files vs. scene Setup — every entry placed per the guide's Placement Rule, checking wider scopes for existing files first
   - LV plan: every stat block's intended LV inside the declared level range, boss at most range-top + 2
   - campaign integration plan: what changes in `00-campaign.md` (adventure list, threads — including replacing any hints the concept has overtaken) and what moves to or joins `Global/`
   - assets plan, if the concept names maps or handouts
   - all gaps found so far

   The blueprint is the completeness contract the final step verifies against. Done when the user approves it.

4. **Write.** Follow the guide's "Generating an Adventure" checklist: scaffold the folder, then overview → act files → NPCs → stat blocks per [../convert-adventure/shadowdark-statblocks.md](../convert-adventure/shadowdark-statblocks.md) → items → locations → assets. Resolve each file's gaps per the Gaps rule before writing it. The concept's **Tone & Table** section binds every scene: its hard constraints (tone, ambiguity rules, off-limits content) override any default the build would otherwise reach for. A file is done when every blueprint row assigned to it appears in it.

5. **Integrate.** Apply the campaign integration plan: update `00-campaign.md`'s adventure list and threads, move or create `Global/` files, and check that wikilinks from prior adventures still resolve. Then mark the concept `status: built` and add a link to the built adventure at the top of the concept — it stays in `Ideas/` as the record of intent.

6. **Verify.** Reconcile the finished adventure against the blueprint and the concept, and report the reconciliation: every blueprint row written (or dropped with the user's sign-off), every concept section traceable to at least one file, every wikilink resolving, every encounter enemy owning a stat block file, every stat block's LV inside the plan, every Tone & Table constraint spot-checked against the scenes it binds. Done at zero unaccounted rows and zero broken links.
