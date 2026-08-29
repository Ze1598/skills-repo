---
name: videogame-infographic
description: "Generate a paste-ready image generation prompt that turns a Substack essay (URL or pasted text) into a game-UI-styled infographic. Picks one of five game UI formats based on the essay's structural shape, locks a consistent visual identity across the series, and outputs a single finished prompt optimized for Nano Banana or ChatGPT image gen. Trigger when the user provides an essay URL or pasted essay and asks to generate an infographic, cover visual, or image prompt for the post."
---
 
# Infographic Generator Skill
 
## Overview
 
Generate one paste-ready image generation prompt that turns an essay into a game-UI-styled infographic. The visual must demonstrate the essay's principle structurally, not narrate it with captions or pull-quotes.
 
Input: a Substack URL or pasted essay text.
Output: one finished prompt for Nano Banana or ChatGPT image gen, plus the extracted theme (core message, felt experience, visual primitive) and the format choice.
 
The skill picks the format itself. No options, no variants, no back-and-forth. The point is daily automation.
 
**Critical ordering:** the skill extracts the theme first (core message → felt experience → visual primitive), then picks the format that displays the primitive most legibly. The format is the dressing. The primitive is the body. Getting the primitive right is the crux — format selection without a clear primitive produces useless infographics.
 
## Core Principle: Simplicity Over Sounding Smart
 
The visual must communicate the principle structurally — through layout, color, scale, and iconography — not through text descriptions inside the image.
 
**Why this matters:** image generation models cannot reliably render long text. Multi-line descriptions, sentences, and paragraph-style stat blocks come out as garbled mush ("miscoostatment," "construtiors," "bouff"). A prompt that depends on text inside the image to carry the meaning will fail every time.
 
**Hard text budget per visual element:**
- Headers and section titles: 1–3 words
- UI labels (stat names, counter labels, channel names, button text): 1–3 words
- Numerical values (turn counts, percentages, HP totals): allowed
- Sentences, descriptions, taglines, multi-line stat effects: forbidden
**The structural-communication test:** if every word of text were stripped from the visual, a viewer should still get the gist of the principle from the layout, color, scale, and iconography alone. Text is supplementary, not load-bearing.
 
If the chosen format requires multi-line text descriptions to land the principle, the format is wrong for that essay. Pick a different format.
 
## Locked Visual Identity
 
These elements never vary across infographics. They are what makes the daily feed read as a series.
 
**Palette**
- Background: warm off-white (#fff7ed)
- Primary: deep navy (#1e2a3a)
- Accent: burnt orange (#d97706)
- Muted state (for "before," "stuck," or "low" states): cool grey (#9ca3af)
- Focal-point glow only: soft yellow (#fbbf24), used sparingly on the single element that carries the mechanism
**Typography**
- UI elements (labels, counters, stat names, table headers): clean monospace, sentence case
- Headers inside the visual: pixelated or blocky display font, sentence case
- All text inside the visual is functional UI text, never decorative pull-quotes or motivational captions
**Composition**
- Aspect ratio: 4:5 portrait (LinkedIn and Substack optimized)
- Generous negative space, balanced layout, no clutter
- Flat geometric shapes, slight grain texture
- No photorealism, no 3D rendering, no gradients except the focal-point glow
- Aesthetic anchor: "feels like game UI design printed as an editorial infographic"
## The Five Format Options
 
All five are game UI dialects. They function as the dressing layer — each one provides the furniture (HP bars, stat panels, drop tables, skill nodes, status icons) that displays a visual primitive most legibly. Format selection (Phase 4) takes the primitive as input.
 
### 1. Encounter / Boss Fight UI
 
**When to pick it:** the essay describes a stuck state that gets broken by a specific move. The shape is deadlock → action → unlock. The "move" can be either an action (do X) or a non-action (stop doing Y, refuse to engage, walk away from the fight). Recognizing a trap and not taking the bait is a move.
 
**In-game reference:** turn-based JRPG combat screen, top-down isometric encounter view, HP bars, turn counters, action prompts.
 
**Layout structure:** split-panel (before/after) or stacked iterations showing the same encounter looping until the move appears. UI elements include turn counter, progress bar that doesn't fill in the "before" state and starts filling in the "after," reaction gauges or speech indicators on characters reacting to the move.
 
**Example mapping (Speed essay):** three weeks of stuck meetings = three identical encounter rounds with TURNS TAKEN: ∞. The prototype = a glowing item carried into the room that triggers REACTION gauges and flips the conversation HUD from REACTIVE to PRODUCTIVE.
 
**Example mapping (Moral Victories essay):** the player character stuck in a long fight against a small, weak NPC, turn counter climbing high, while the actual quest objective sits greyed out and untouched in the corner. The "move" is leaving the fight — disengaging from a battle that was never the player's quest to begin with.
 
### 2. Character Stat Comparison Screen
 
**When to pick it:** the essay corrects a misread signal, exposes hidden context behind a surface judgment, or compares two paths that look similar but ran very different distances.
 
**In-game reference:** RPG character select screen, stat sheets side by side, class cards, attribute breakdowns.
 
**Layout structure:** two character cards in parallel. Each card shows a starting-stats panel and a current-stats panel, with a visible "distance traveled" indicator (XP earned, levels grinded, terrain crossed) between them. The current stats can look identical while the starting stats and distance differ dramatically.
 
**Example mapping (Delta essay):** Character A starts with low resource stats, traverses a long uphill path, arrives at "stable adult life" stats. Character B starts with maxed resource stats, takes two steps forward, arrives at the same stats. Both end-state cards look identical. The starting-line panels and the path-traveled visualizations make the delta obvious without a single explanatory word.
 
### 3. Drop Rate / RNG Table
 
**When to pick it:** the essay is about probability, repetition, coverage, or compounding attempts. The shape is one shot has low odds → multiple shots across formats raise the odds.
 
**In-game reference:** loot drop tables, gacha pull rates, RNG percentage rolls, multi-attempt rolls displayed as a grid or table.
 
**Layout structure:** a stat table or roll grid showing one attempt with a low success indicator on the left, multiple attempts across different "drop tables" or channels on the right with cumulative success indicators filling. Channels are labeled as the formats from the essay (group chat, printed sign, follow-up reminder; or short video, long essay, X thread).
 
**Example mapping (Repeat Yourself essay):** one chat message = one roll on a low-percentage drop table, success indicator dim. Three formats across time = three rolls across three different drop tables, success indicators stacking until the cumulative chance lights up.
 
### 4. Skill Tree / Crafting Recipe
 
**When to pick it:** the essay describes a sequence, prerequisites, or building toward something through ordered components.
 
**In-game reference:** RPG skill trees, crafting menus, recipe grids with input → process → output.
 
**Layout structure:** node-based progression diagram with locked and unlocked nodes, or a crafting grid showing inputs combining into a result. Connections between nodes show prerequisite logic.
 
**Example mapping:** an essay about building a habit stack would show foundational nodes unlocking dependent nodes, with locked nodes greyed out until prerequisites are met.
 
### 5. Status Effect / Buff-Debuff (Fallback — use rarely)
 
**When to pick it:** the first four genuinely don't fit, even after re-examining with the action-or-inaction lens. Use only when the essay's mechanism is fundamentally about how perspective changes what something is, when the same condition is an advantage for one person and a drag on another, or when the topic resists structural mapping entirely.
 
**In-game reference:** RPG status effect icons, buff/debuff bars, condition tooltips with effect descriptions and durations.
 
**Layout structure:** a status panel showing the same condition rendered twice — once as a buff icon (green border, upward arrow indicator), once as a debuff icon (red border, downward arrow indicator) — applied to two different character contexts shown as small portrait icons. The buff/debuff distinction must be carried by **color, border, and icon shape**, not by text descriptions. Labels are 1–3 words maximum: "buff" / "debuff" / context name. No multi-line effect descriptions.
 
**Why it's the fallback and why to avoid it when possible:** this format is the most text-dependent of the five. Image gen models render long status descriptions as garbled text, and the buff/debuff verdict requires the viewer to accept a label on faith without seeing structural evidence. If the principle can be visualized as an encounter, comparison, RNG roll, or sequence instead, those formats communicate more reliably. Default to fallback only when no other format fits.
 
## Theme Extraction (Phases 1–3)
 
The crux of the skill. Get this wrong and the format choice doesn't matter. Run these three phases in order before touching format selection. Each phase feeds the next.
 
### Phase 1 — Core Message
 
State the essay's core principle in one sentence, the way the author would say it back if asked "what's this essay really about." Not the headline. Not the topic. Not a structural breakdown. The actual principle the essay teaches.
 
**Test for a good core message:** if you handed this sentence to a stranger who hasn't read the essay, they would understand what the essay is arguing. If the sentence requires reading the essay to make sense, it's too vague — extract again.
 
### Phase 2 — Felt Experience
 
Translate the core message into what the principle *feels like* when it's happening to a reader. Not the abstract principle — the visceral experience of being inside it.
 
**Test for a good felt experience:** the description is concrete, sensory, and emotional. It uses verbs of physical or psychological state ("being puppeted," "burning fuel for someone else," "running on a treadmill someone else turned on"). It's not a definition. It's a sensation.
 
**Examples of the translation:**
- Core message: "responding to someone's doubt is letting them set your agenda" → Felt experience: "being puppeted by someone who walked away three minutes ago"
- Core message: "showing up with a working prototype changes the conversation more than another meeting" → Felt experience: "the room flips from theoretical to reactive the second something real lands on the table"
- Core message: "where someone ends up tells you nothing about how far they had to travel" → Felt experience: "two people standing on the same line, one carrying a heavy pack and one with empty hands"
### Phase 3 — Visual Primitive
 
Find the smallest game UI element that carries the felt experience. A primitive is one tiny piece of furniture from the game UI vocabulary: a quest log entry, a debuff icon, a stamina drain, an HP bar at zero, an equipment slot with the wrong item locked in, a turn counter ticking up, a reaction gauge mid-fill, a greyed-out quest objective, an inventory slot full of junk, a status icon attached to a portrait.
 
**The primitive is the body of the visual.** Everything else (the format, the layout, the dressing) exists to display the primitive clearly.
 
**Three rules for picking the primitive (apply in order):**
 
1. **Do not use metaphors the essay already states.** If the essay says "it's a moral victory," do not put a trophy with "moral" written on it. If the essay says "speed is a super skill," do not put a speed buff icon. Find the underlying felt experience and map that to a primitive the author did not write.
2. **Concept-to-Primitive Rule.** When the right concept maps to something complex, reduce the concept to its simplest renderable form — do not switch to a different (lesser) concept. Agenda hijack via reactive work is the right concept for the Moral Victories essay; the primitive is "a quest log where someone else's doubt is the active quest while your real goal sits greyed out." Don't abandon the concept and switch to a generic buff/debuff just because the first version felt complex. Find the simpler version of the right concept.
3. **Emotional resonance over conceptual cleverness.** The primitive captures how the essay feels, not what the essay explains. Visceral, not intellectual. Physical manifestation of the psychological state.
**Examples of primitive extraction:**
- Felt experience: "being puppeted by someone who walked away three minutes ago" → Primitive: a quest log with "[Stranger]'s doubt" sitting as the active tracked quest, while "Your goal" sits below it greyed out and untouched
- Felt experience: "the room flips the second something real lands on the table" → Primitive: a turn counter at ∞ in the before, dropping to a real number with a progress bar starting to fill in the after, triggered by one glowing item entering the scene
- Felt experience: "two people on the same line, one carrying a heavy pack" → Primitive: two character cards with identical end-state stats, but one card shows a long uphill terrain segment between starting and current stats while the other shows two flat steps
### The 80% Test (gate before Phase 4)
 
Before picking a format, run this test on the primitive: if every word of text were stripped from the primitive, would 80% of the message still land from layout, color, scale, and iconography alone?
 
If no, the primitive is too text-dependent. Refine it — do not move forward and try to fix it with format selection. The primitive is the body. If the body is wrong, the dressing won't save it.
 
## Format Selection (Phase 4 — the dressing layer)
 
The format is the costume. The primitive is the body. Pick the format that displays the primitive most legibly.
 
The format selection takes the **primitive** as input, not the essay's structural shape. Run these questions in order. Stop at the first match.
 
1. **Is the primitive about a stuck encounter, a turn counter ticking up, a quest log entry, or anything that fits inside a turn-based combat scene?** → Encounter / Boss Fight UI
2. **Is the primitive about two characters or paths with similar end states but different starting stats or distance traveled?** → Character Stat Comparison Screen
3. **Is the primitive about probability, multiple attempts, drop chances, or coverage across channels?** → Drop Rate / RNG Table
4. **Is the primitive about prerequisites, ordered nodes, crafting components, or building toward a result?** → Skill Tree / Crafting Recipe
5. **The primitive doesn't fit any of the four formats cleanly?** → Re-examine the primitive first. The primitive may be wrong. Most essays' primitives fit one of the four formats. Only if the primitive genuinely cannot be displayed in the four formats, fall back to Status Effect / Buff-Debuff.
If two formats seem to fit, pick the one that gives the primitive the most room to communicate — the format where the primitive is the focal point, not a corner detail.
 
**Critical:** if you find yourself reaching for Status Effect, the primitive is probably underspecified. Go back to Phase 3 and refine the primitive before defaulting to fallback.
 
## Forbidden Visuals
 
Mirror of the daily-newsletter forbidden-phrases discipline. If a visual element is doing the work the essay's mechanism is doing, it's fine. If it's decoration or generic motivation, it's out.
 
- No rocket ships, mountains, summits, ladders, staircases
- No lightbulbs, gears, brain icons, puzzle pieces
- No upward arrows representing "growth" or abstract progress
- No handshake icons, target/bullseye icons, trophy icons, finish-line ribbons
- No abstract "person silhouette with idea bubble" stock-image energy
- No motivational stock photography aesthetics
- No clip-art emoji clusters
- No inspirational pull-quotes overlaid on the visual
- No closing captions, taglines, or essay summaries inside the image
- No metaphor that requires having read the essay to understand — the visual must communicate structurally on its own
The only text inside the visual is functional UI text: stat names, channel labels, turn counters, table headers, short status labels. Functional UI text earns its place because it's part of the format. Decorative text doesn't. Every text element is bound by the 1–3 word text budget rule above.
 
## Prompt Assembly Template
 
Output the prompt as descriptive prose optimized for Nano Banana or ChatGPT image gen. Structure each prompt in this order:
 
1. **Opening sentence** — names the format and overall aesthetic in one line. Example: "A split-panel infographic styled as a retro JRPG boss-battle UI screen, rendered in clean pixel-art-meets-vector hybrid style."
2. **Style and palette block** — specifies the locked visual identity. Background color, primary and accent colors, typography choice, texture notes.
3. **Panel-by-panel walkthrough** — describes each part of the visual in detail. For split-panel formats, describe left and right panels separately. For single-panel formats (skill tree, RNG table, status effect), describe the layout sections in reading order. Use specific UI element language: "HP bar," "turn counter," "stat panel," "drop table row," "buff icon."
4. **Style notes block** — flat geometric shapes, slight grain, no photorealism, no 3D, no gradients except focal-point glow, balanced negative space.
5. **Aspect ratio specification** — 4:5 portrait.
**Text budget enforcement (hard rule):** every text element specified in the prompt must be 1–3 words maximum. Numerical values (turn counters, percentages, HP totals) are allowed. Sentences, multi-line descriptions, taglines, and paragraph-style stat effects are forbidden. If the prompt specifies "label reads X" or "text says Y," count the words. If over 3, rewrite.
 
**Examples of allowed text inside the visual:**
- "Turn count: 124"
- "Quest: ignored"
- "HP: 100"
- "Channel: chat"
- "Reaction"
- "Locked"
**Examples of forbidden text inside the visual:**
- "proof built to correct misstatement, task agenda set by other"
- "this is a debuff because the work was reactive"
- "resource spend unrelated to internal goals"
- Any sentence-length stat description
The prompt must be self-contained and generate the complete infographic in a single pass. Never include fallback instructions, alternative compositing paths, or "if this doesn't work" clauses inside the prompt. Hedges like that signal the multi-panel composition is optional and degrade the output. The prompt is treated as a single complete instruction.
 
## Output Format
 
Return one document with these sections in order:
 
### 1. Theme Extraction
Three lines, one each for the three extraction phases:
 
- *Core message: [one sentence stating the essay's principle as the author would say it back]*
- *Felt experience: [one sentence describing what the principle feels like, visceral and sensory]*
- *Visual primitive: [the smallest game UI element that carries the felt experience, described in one sentence]*
### 2. Format Chosen
One line stating the format and a one-line reason — specifically why this format displays the primitive most legibly.
 
Example: *"Format: Encounter / Boss Fight UI — the format gives the quest log primitive a turn counter and combat scene to anchor the agenda-hijack mechanic."*
 
### 3. The Image Generation Prompt
The full prompt, copy-paste ready, wrapped in a markdown code block (triple backticks) so the user can copy it in one click. The prompt itself is a single block of descriptive prose following the assembly template above.
 
That's it. No variants, no alternative directions, no closing commentary.
 
## Workflow
 
1. Receive essay URL or pasted text. If URL provided, fetch the essay.
2. **Phase 1:** Extract the core message — one sentence stating the essay's principle as the author would say it back.
3. **Phase 2:** Translate the core message into a felt experience — concrete, sensory, and emotional, not abstract.
4. **Phase 3:** Find the visual primitive — the smallest game UI element that carries the felt experience. Apply the three rules: no author-stated metaphors, concept-to-primitive reduction, emotional resonance over conceptual cleverness.
5. **Run the 80% test on the primitive.** If 80% of the message wouldn't land from layout/color/scale/iconography alone, refine the primitive. Do not move on with a weak primitive.
6. **Phase 4:** Pick the format that displays the primitive most legibly, taking the primitive as input.
7. **Phase 5:** Assemble the prompt following the template, enforcing the text budget.
8. **Phase 6:** Verify against the quality checklist.
9. Deliver the three-section output.
## Quality Checklist
 
Before delivering, verify:
 
**Theme extraction (must pass before format selection):**
- [ ] Core message stated in one sentence — would make sense to a stranger who hasn't read the essay
- [ ] Felt experience is concrete, sensory, emotional — not a definition or a restatement of the core message
- [ ] Visual primitive is a single small game UI element (quest log entry, debuff icon, turn counter, equipment slot, stamina bar, etc.) — not a whole scene
- [ ] Primitive does not reuse a metaphor the essay already states verbatim
- [ ] If the right concept felt complex, primitive was reduced to its simplest renderable form — not switched to a different concept
- [ ] Primitive captures the felt experience emotionally, not just structurally
- [ ] **80% test passes:** if every word of text were stripped from the primitive, a viewer who has not read the essay would still get 80% of the message from layout, color, scale, and iconography alone
**Format selection:**
- [ ] Format picked by running selection logic against the primitive (not the essay's structural shape), stopping at first match
- [ ] If fallback (Status Effect) was reached, the primitive was re-examined first — fallback is not the default path
- [ ] Format gives the primitive room to be the focal point, not a corner detail
**Visual identity and text budget:**
- [ ] Locked visual identity applied: warm off-white background, navy primary, burnt-orange accent, monospace UI typography, 4:5 aspect ratio
- [ ] **Text budget enforced:** every text element in the prompt is 1–3 words maximum (numerical values exempt). No sentences, no multi-line descriptions, no paragraph-style stat effects
- [ ] No forbidden visuals (rocket ships, lightbulbs, growth arrows, stock-image silhouettes, decorative pull-quotes, closing captions)
- [ ] Only functional UI text inside the visual — no taglines, no summaries, no motivational text
- [ ] Focal-point glow used on exactly one element (the primitive itself, the mechanism carrier) — not scattered
**Output:**
- [ ] Prompt is descriptive prose suitable for Nano Banana or ChatGPT image gen — not Midjourney parameter syntax
- [ ] Prompt is wrapped in a markdown code block (triple backticks) for one-click copy
- [ ] Prompt contains no fallback instructions, alternative compositing paths, or "if this doesn't work" clauses
- [ ] Output document has three sections in order: Theme Extraction, Format Chosen, Image Generation Prompt
- [ ] No closing commentary, no variants, no alternative directions offered
