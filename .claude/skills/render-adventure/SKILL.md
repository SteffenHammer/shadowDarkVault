---
name: render-adventure
description: Render a vault adventure into a single interactive HTML GM screen, styled live from the vault's DesignSystem. Argument: the adventure folder (path or name).
disable-model-invocation: true
---

# Render Adventure

Render one adventure into one self-contained HTML file — a **GM screen**: everything the GM needs to run the adventure at the table, spoilers included, with live table tools (collapsible scenes and encounters, HP trackers, clock trackers, persistent notes). [page-spec.md](page-spec.md) is the single source of truth for the page: architecture, content mapping, and the widget kit.

The rendering is **faithful**: every line of the adventure's markdown lands on the page, restyled but unrewritten. The look comes from the design system, read fresh every run — it may have changed since the last render.

## Gaps

A **gap** is anything the page-spec doesn't decide: a callout type or section outside the Structure Guide's grammar, a wikilink whose target file doesn't exist, a table that could be a clock tracker or plain reference, no clear cover image, no `theme:` in the frontmatter. Collect the gaps and put them to the user in one AskUserQuestion round, each with a concrete proposal as the recommended option — content is asked about, never silently dropped or restyled ad hoc.

## Process

1. **Ingest.** Read the adventure folder end to end in numeric order — frontmatter, `00-overview.md`, act files, then `npcs/`, `statblocks/`, `locations/`, `items/`, `assets/` — and follow every wikilink outward once: campaign `Global/` files and shared monsters it reaches are in scope; anything beyond (other adventures, the campaign overview) is out of scope. Done when every wikilink is classified in-scope or out-of-scope and every asset is catalogued with the scene(s) that reference it.

2. **Skin.** Read the whole design system fresh: every file in `shadowVault/DesignSystem/tokens/` (inlined verbatim into the page) and every demo in `DesignSystem/guidelines/` (the visual spec the page's component CSS is derived from — if `DesignSystem/styles.css` exists, inline it instead of deriving). Theme: the adventure's `theme:` frontmatter key names the `data-system` scope; a missing key is a gap. Done when every token file is captured and the theme is fixed.

3. **Map.** Assign every markdown element of every in-scope file to a page-spec component and decide which tables are clocks. Everything unmappable is a gap; resolve all gaps in the one AskUserQuestion round now. Done when every element has a component and no gap is open.

4. **Build.** Write `<adventure folder>/gm-screen.html` per the page-spec. Done when every in-scope file's content appears on the page, every image is embedded as a data URI, and the file's only external request is the design system's Google Fonts import.

5. **Verify.** Open the file in a browser and exercise it: navigate from the sidebar to every act, open a hover-card, collapse and reopen a scene, run an HP tracker to 0 and back, add an instance, tick the clock, write a note — then reload: all state must survive. Done when every widget type has been exercised, state survives reload, and console and network panels are clean (fonts excepted).
