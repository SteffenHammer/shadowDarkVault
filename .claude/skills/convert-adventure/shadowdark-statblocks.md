# Shadowdark Stat Blocks — Format & Conversion

Each creature gets one file from the vault's `statblock-template.md` with `system: Shadowdark` in the frontmatter. Flavor (looks, behavior, when it flees) goes in a short paragraph above the card; the card itself is pure mechanics in this canonical shape — an expanded-by-default callout:

```markdown
> [!info]+ Creature Name — LV 4
> **AC** 13 · **HP** 22 · **MV** near (climb) · **AL** C
>
> **ATK** 2 claw +4 (1d6+2)
>
> | STR | DEX | CON | INT | WIS | CHA |
> |:---:|:---:|:---:|:---:|:---:|:---:|
> | +2  | +1  | +1  | -2  | +1  | -1  |
>
> **Talent Name.** What it does, stated mechanically.
>
> **Other Talent (1/day).** Limited-use effects keep their tag.
```

Format rules:

- The six stats are modifiers only (−4…+4), never scores.
- **MV** uses Shadowdark ranges, not feet: `close` (~5 ft), `near` (~30 ft), `double near` (~60 ft), `far` (within sight). Movement modes go in parentheses: `near (climb)`, `near (fly)`, `near (swim)`.
- **ATK**: `<count> <name> +<bonus> (<damage>)`. Alternative attacks joined with `or`, simultaneous ones with `and`. Ranged attacks note their range: `(1d6, far)`.
- **AL** is `L`, `N`, or `C`.
- **LV** measures threat; a creature is a fair fight for a party of roughly its LV.
- No morale, CR, skills, senses, or condition lists — that is not part of a Shadowdark stat block. Fold flee-behavior and instincts into the flavor line, or into the encounter's Tactics line in the act file.

## Converting from other systems

| Source stat | Shadowdark conversion |
| --- | --- |
| AC | Keep as-is (both systems live around 10–18). |
| HP / Hit Dice | LV = number of hit dice (±1 for elite/weak). HP ≈ LV × 4.5 + CON mod per LV; keep the source HP if it lands within that ballpark. |
| Attack bonus | Keep if it's ≤ +7; otherwise cap at +7 and raise damage instead. |
| Speed in feet | ≤ 10 ft → `close`; 20–40 ft → `near`; 50–70 ft → `double near`. |
| Saving throws ("WIS save DC 13") | Become stat checks: "DC 12 WIS check". Snap every DC to the Shadowdark ladder 9 / 12 / 15 / 18. |
| Advantage / disadvantage | Same mechanic in Shadowdark — keep. |
| Morale score | Drop the number; express it as behavior ("flees below half HP", "fights to the death"). |
| Conditions (frightened, restrained, …) | State the mechanical effect plainly ("−1 on attacks for 1d4 rounds", "held: no move, may retry DC 12 STR each turn"). |
| Damage types (necrotic, fire, …) | Keep the dice; keep the type word as flavor only — it carries no rules weight. |
| Resistances / immunities | Keep as a talent: "Half damage from non-magical weapons." |
| Special abilities | Each becomes a short named talent below the stat line. |
| Spells | Talents with an explicit effect and, where a roll is needed, a DC from the 9/12/15/18 ladder. |
| Missing ability scores | Derive modifiers from the fiction (a brute gets S +2, an ambusher D +2, a mindless thing I −3); default +0. Deriving stats is routine conversion work, never a gap. |

Sanity check before finishing a block: the creature's LV must sit inside the adventure's declared level range — bosses at most range-top + 2. Shadowdark is deadlier than most source systems; when in doubt, lower HP rather than the attack bonus.
