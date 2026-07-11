---
name: develop-adventure-idea
description: Interview the user relentlessly until a vague adventure idea becomes a coherent, build-ready concept in Adventures/Ideas/. Argument: the idea, or the name of an in-progress concept to resume.
disable-model-invocation: true
---

# Develop Adventure Idea

Turn a vague idea into a concept document the build skill can consume without asking anything. `shadowVault/Templates/adventure/concept-template.md` is the single source of truth for what a concept must contain; this skill defines only the interview that fills it.

A concept is **coherent** when it passes the **stranger-GM test**: a GM who wasn't in the room could pitch the adventure from the Logline alone and prep the first session without inventing anything load-bearing. That test is the exit condition below.

You are a story editor, not a stenographer: propose, sharpen, and challenge — and the user's answer always wins. The concept names monsters, hazards, items, and beats; statting them and scaffolding files belongs to the build skill.

## Process

1. **Seed.** If the argument names a concept in `shadowVault/Adventures/Ideas/` (or one there has `status: in-progress`), resume: read it, list the sections that fail their theme's vagueness test, and continue at step 3. Otherwise restate the idea in one sentence, propose an adventure type (one-shot / single-adventure / campaign) with an expected session count, and create the concept file from the template (`status: in-progress`) once the user confirms both. Done when the file exists and the user has confirmed restatement and type.

2. **Pitch.** If the seed could still become two very different adventures, write 2–3 deliberately divergent one-paragraph pitches — vary whatever is most open (tone, antagonist logic, structure), not surface details — and let the user pick one or mix. Skip when the seed already fixes the direction. Done when one direction is chosen.

3. **Interrogate.** Work through the themes in [interview-themes.md](interview-themes.md) in order, one theme per round — a theme the seed already answers still gets its vagueness test, usually a one-line confirm. Round mechanics:
   - Open with the theme's current state in a sentence or two.
   - Every open point comes with 2–3 concrete proposals to pick, edit, or reject (AskUserQuestion where options fit) — never a blank "so, what do you want?".
   - Apply the theme's vagueness test to each answer: restate it concretely; while the restatement still fits two different adventures, keep drilling in the same round.
   - Check each answer against the whole concept so far; surface any contradiction immediately, with a proposed resolution.
   - Close the round by updating the concept file — an interrupted interview must resume from the file alone.

   Done when every template section except the Logline is filled and passes its theme's vagueness test.

4. **Ready gate.** Read the finished concept end to end and run the stranger-GM test; anything load-bearing still missing gets one final round. Then write the Logline — the three-sentence distillation the test reads — set `status: ready`, and present the Logline plus a one-line summary per section. Done when the user signs off.
