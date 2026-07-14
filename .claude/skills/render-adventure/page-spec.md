# GM Screen — Page Spec

The single source of truth for the rendered page: file rules, layout, content mapping, widget kit. Every rule here binds every render; content that fits no rule is a gap, put to the user per [SKILL.md](SKILL.md).

## File

- Output: `<adventure folder>/gm-screen.html` — one file, GM-only: every secret stays on the page.
- Self-contained: token CSS inlined verbatim, component CSS and JS inline, images as data URIs. The one external request is the design system's Google Fonts `@import`; every family declares a serif fallback, so the page degrades gracefully offline.
- Vanilla HTML/CSS/JS, no frameworks, no build step. Component CSS is derived from the design system captured in the Skin step — visual facts (voices, borders, shadows, spacing) live there, not here.
- Root: `<body class="gr-app" data-system="<theme>">` with the `.gr-vignette` and `.gr-grain` overlays from `motifs.css`.

## Layout

- **Sidebar** — sticky left, collapsing to a toggle on narrow screens: the act/scene tree from the overview's Structure section as anchor links, current section highlighted on scroll, appendix links (Cast, Bestiary, Locations, Items, Handouts) below, clock chip (see Clock tracker) at the top.
- **Hero** — cover image (chosen in Map; `.gr-media` placeholder if none), mono eyebrow = campaign name, title in the head voice at hero scale, meta strip from frontmatter: system · levels · party size · sessions · status.
- **Chapters** — Overview first, then one chapter per act in numeric order. The overview's Structure section is consumed by the sidebar and appears nowhere else.
- **Appendices** — Cast (NPC dossiers), Bestiary (stat cards), Locations, Items, Handouts (handout markdown rendered as in-world documents in the flavor voice; handout images as figures).
- **Footer** — render date and the Reset control (see State).

## Content mapping

| Markdown | Component |
|---|---|
| Premise & Hook | flavor-voice prose |
| Background (GM only) and other overview prose | body prose |
| Cast & Factions table | cast table; name cells link to the dossiers |
| Act Overview bullets | act intro panel: mono-label rows (PURPOSE / STATE OF THE WORLD / WAYS IT CAN END) |
| `## Scene:` heading | scene panel; its Purpose/Trigger/Setup bullets become a mono-label meta row in the panel header area |
| `> [!quote] Read Aloud` | read-aloud block: flavor voice, accent left border, READ ALOUD eyebrow — unmistakable at a glance, because it is spoken verbatim |
| `> [!tip] GM Guidance` | aside on accent-soft ground with a GM eyebrow |
| `> [!warning]` | danger panel on the danger tokens |
| `> [!info]+` stat block callout | stat card (see Stat cards) |
| `**Encounter:**` / `**Hazard:**` bold-label blocks | encounter panel (see Encounter panels) |
| `### Outcomes` | scene footer: each outcome an arrow row linking its target scene/act anchor |
| bold-label bullet lists (NPC, location, item files) | definition rows: mono label + body text |
| table | styled table — or clock tracker, if designated a clock in the Map step |
| in-scope wikilink | anchor link with hover-card (see Hover-cards) |
| out-of-scope wikilink | inert emphasized text with a `title` tooltip naming where it lives |
| image embed | `<figure>` with data URI and caption |

## Widgets

**State.** All widget state lives in `localStorage` under the single key `gm-screen:<adventure slug>` — stable across re-renders, so a rebuilt page keeps the table's progress. The footer Reset control clears the key via a two-click arm-then-confirm (no browser dialog).

**Collapse.** Every scene panel, encounter panel, stat card, and appendix entry carries a minimize toggle in its header; collapsed state persists.

**Hover-cards.** An in-scope wikilink shows its target rendered as a card — stat card, dossier, item, or location — in a popover on hover or tap; click navigates to the anchor. One implementation: the popover reuses the same markup as the target's appendix entry, so the GM never leaves the running scene to check a stat.

**Encounter panels.** The block's bold labels (Enemies, Tactics, Terrain, Treasure / Effect, Counter) become mono-label rows. Each enemy line expands to HP tracker rows: one row per creature instance with max HP seeded from its stat card, − / + controls, an editable current value, and a grayed "down" style at 0 (recoverable). Dice-count enemies (`1d4+1 ×`) start at the dice minimum with an add-instance button. All tracker state persists.

**Stat cards.** Header = title + level + collapse toggle; the callout's stat line as a mono row; the ability table as a grid; traits as bold-label paragraphs. A card whose creature fights in a rendered encounter carries the same HP tracker inline.

**Clock tracker.** A table designated a clock in the Map step renders its steps checkable, in order; the current step row is highlighted, and the sidebar's clock chip names it from anywhere on the page.

**Notes.** Every scene panel ends with a collapsed session-notes textarea; a scene with notes shows a dot in its panel header and its sidebar entry.
