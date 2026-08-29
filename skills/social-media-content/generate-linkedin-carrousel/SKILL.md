---
name: generate-linkedin-carrousel
description: Convert a leadership or organizational essay into a square LinkedIn carousel PDF with a flat charcoal-and-amber visual system. Use Proof-Promise-Plan across one causal workplace case, expose the mechanism late, preserve the legitimate part of the failed response, and finish with the smallest operational correction and a reflection question for professionals building leadership experience before or beyond a formal title. Do not create an essay summary spread across slides.
---

# Purpose

Convert one of the user's leadership or organizational essays into a finished LinkedIn carousel PDF.

Input is normally:

- the full text of a Substack essay; or
- a public Substack essay URL.

Output is:

- one finished multi-page PDF;
- one square carousel slide per PDF page.

Use the complete visual and export specification embedded in this skill. Do not fetch an external template or repository.

---

# Core Format

## This is not an essay summary

Do not split the source essay into shortened sections.

Do not create:

- introduction;
- problem;
- consequence;
- lesson;
- solution;

as generic buckets.

The carousel must reconstruct the essay as **one causal sequence**.

One concrete workplace case should carry the carousel whenever the essay provides one.

Treat one slide as one causal beat, not one sentence or essay paragraph. Each slide should change something:

- somebody acts;
- information moves;
- ownership changes;
- an assumption becomes fixed;
- a gap survives;
- somebody behaves differently because of it;
- the reader learns what the real mechanism was.

If two slides describe the same state of the situation, combine them.

---

# Narrative Model

Use the same narrative architecture as the Leadership Visual Essay format. Change the medium and wording density, not the causal structure.

Use Proof-Promise-Plan exactly as defined below. Use the causal beats to construct the Plan.

Bracket the source essay with a Hook and a closing reflection question. Write both fresh. Do not compress or paraphrase the essay's opening and closing sentences into these beats.

The default architecture is:

```text
Proof + Promise Opener
  -> Establish the Situation
    -> Concrete First Action
    -> Reasonable Response (competent, not naive)
      -> Immediate Improvement (the response genuinely helps)
        -> Point Where Control Ends (the exact break or failed assumption)
          -> Surviving Failure Path (the gap persists across time)
            -> Visible Consequence (behavior changes because of the gap)
              -> Mechanism Named in Full
                -> Balanced Counterweight (preserve what was legitimate)
                  -> Reframe (generalize the mechanism)
                    -> Smallest Correction / Operational Close (the source thesis as bookend)
                      -> Reflection Question / CTA (new writing; direct and specific)
```

Skip beats that do not exist in the source.

Do not invent events to fill the architecture.

Keep the order when the beats apply.

---

# Proof-Promise-Plan

## Proof

Open with a concrete event, result, failure, or decision.

Do not begin with abstract teaching when the case can make the point.

Proof does not require revealing the final consequence early. Preserve the causal timeline. If revealing the final outcome would force the carousel to jump backward and restart the story, begin with the first event that produces it.

Name enough of the person, action, and result for the event to make sense without slide 2. An unidentified person's contradiction is not useful Proof.

Bad:

"His standard changed when nobody else was in the room."

Better:

"He called his team's work excellent. Then approved work he knew fell short."

The remaining case beats supply the evidence that proves the hook. Do not treat Proof as one unsupported claim followed by a different story.

## Promise

Expose the mechanism the story will reveal.

Keep the Promise to one compact statement. Do not explain the whole carousel before the case demonstrates it.

The Promise must make the value of swiping visible. Give the reader a useful claim, test, distinction, or mechanism they can recognize in work they influence, review, recommend, or help deliver. Do not write promotional scaffolding such as "By the end, you will learn..."

Because slide 1 must earn the swipe, combine Proof and Promise on the opener when one slide can carry both. Default to a header-only opener with three short sentences when the case supports three distinct contextual beats. Render each sentence as its own paragraph. Proof and Promise must share the slide, not necessarily one sentence.

### Opener Clarity

Choose clarity over compression.

Use complete declarative sentences with explicit subjects. Do not fuse several causal beats into one sentence, use a dangling clause, or depend on line breaks to make compressed prose understandable.

Treat the opener as a hook, not a compressed synopsis. Leave supporting context, motives, and secondary details for the later slides that already carry those beats.

Prefer a definite, known subject when the source presents one specific case. Write `the delivery manager`, `the engineer`, or `the team` instead of introducing the same role with `a`. This gives the opener the authority of a case already in progress. Use an indefinite article only when the subject is intentionally generic or one of several interchangeable examples.

Build impact through contrast between the setting and what the subject did. When the case supports it, give the three opener paragraphs these jobs:

1. Establish the setting and the known subject.
2. State the decision, shift, or outcome the situation required.
3. Expose the subject's failed move, contradiction, or consequence.

Keep each beat to one short sentence. Do not add facts that the rest of the carousel will explain.

Aim for three sentences that let the reader establish the case in three steps. Give each sentence one job and render it as one paragraph. Use two sentences only when a third sentence would repeat information or invent a beat the source does not contain. Do not pad the opener to reach three.

Example:

```text
The delivery manager went into Monday's team meeting with one decision.

Focus needed to shift from feature development to fixing defects.

Yet she lost attention while rambling through a preamble no one cared about.
```

When the case turns on a contradiction between a requested behavior and a rewarded behavior, prefer this sequence:

1. State the concrete result or event.
2. State the conflicting request or expectation.
3. State which behavior the incentives made more valuable.

Bad:

"A developer led the team in tickets closed. His manager asked for teamwork—then kept rewarding the number that made collaboration cost him."

Better:

"A developer led the team in tickets closed. His manager asked for teamwork. Yet the incentives made it clear that ticket output mattered more."

Pattern:

```text
Title / Proof: concrete event, result, failure, or decision
Body / Promise: the useful mechanism or standard the case will expose
```

Example:

```text
He praised excellent work, then approved defects.

Your real standards are the work you knowingly allow to ship.
```

Do not delay the Promise until the late Mechanism Reveal. The late reveal explains and earns the Promise; it should not be the reader's first sign of value.

## Plan

Walk through one continuous causal sequence:

1. Establish the situation.
2. Show the action or instinct that appears reasonable.
3. Show what it achieves.
4. Show where it stops controlling the outcome.
5. Show the consequence.
6. Name the mechanism once the reader can see it.
7. State the smallest correction that addresses it.
8. Close with the operational implication.

Do not alternate between the case and a parallel abstract explanation. The case is the explanation.

Preserve what was legitimate, isolate the failure, and state the smallest actions that change the outcome. Use a dash-list slide when the correction contains a real set of parallel actions.

Keep the Plan proportionate to the case. Do not turn one operational correction into a broad leadership transformation program.

---

# Narrative Beat Definitions

## Hook

The first slide is the Proof-Promise opener, not a title card.

Do not default to the essay title.

The opener should expose:

- a concrete event, result, failure, or decision; and
- the value of understanding the mechanism the case will reveal.

It should create a question the reader expects the carousel to answer without hiding the reason the answer matters.

A good test:

If slide 1 could be used as the essay's opening paragraph without changing anything, it is probably too literal.

Write the opener fresh.

Do not use generic LinkedIn clickbait.

Bad:

- "Communication silos are killing your team."
- "Here are 5 ways to communicate better."
- "Most managers get this wrong."

Better:

- state the concrete Proof;
- preview the useful mechanism as the Promise;
- let the remaining case earn and explain that Promise.

The essay title can be used in the PDF filename or metadata. It does not need to appear on slide 1.

---

## Concrete First Action

Show what somebody actually did.

Use:

- the real role;
- the real decision;
- the real work.

Avoid abstract setup.

Bad:

"Cross-functional communication became difficult."

Better:

"Operations and design defined the reporting process before engineering entered the discussion."

The reader should be inside the case by this point.

---

## Reasonable Response

The other party should behave like a competent person.

Do not turn the story into:

smart protagonist vs stupid organization.

If the failed response was reasonable at the time, show why.

This is important because a mechanism is useful only when competent people can fall into it.

---

## Immediate Improvement

If the response solved part of the problem, say so.

Do not rewrite every failed system as broken from the first second.

Examples:

- the architect improved the pre-sales call;
- the meeting answered the question;
- the process reduced one class of errors;
- the manager's intervention worked in the short term.

This creates the contrast required for the later failure.

---

## Point Where Control Ends

Find the exact moment where the solution stops protecting the outcome.

This is one of the most important slides.

The point should be concrete.

Examples:

- the architect leaves the call;
- commercial discussions continue without technical review;
- the answer passes through another team;
- the manager assumes the message will travel;
- the requirement changes after approval.

Do not use vague language such as:

"communication broke down."

Show where it broke.

---

## Surviving Failure Path

Show how the gap continues to exist.

The failure should survive because the organization keeps operating around it.

This is different from saying:

"then there were communication problems."

Track what moves through the system.

Examples:

- the answer moves through intermediaries;
- the contract keeps changing;
- each team builds against its own definition;
- the unsupported behavior becomes normal;
- a missing review stays missing across several decisions.

---

## Visible Consequence

Show a change the reader can observe.

Examples:

- another meeting appears;
- somebody stops asking for informal help;
- the wrong requirement reaches delivery;
- multiple implementations emerge;
- a customer commitment becomes impossible to meet.

Do not substitute abstract consequences such as:

"trust decreased"

when the essay provides observable behavior.

---

## Mechanism Reveal

This is the payoff.

Do not state the thesis too early.

By this point the reader should understand the case.

Now name what has actually been happening.

This slide should make the previous slides click together.

Examples of mechanism forms:

- every handoff stripped context;
- the fix controlled one meeting, not the commitment process;
- the team optimized the visible failure instead of the source;
- specialization became control over who could exchange information.

The reveal should generalize the case without abandoning it.

Prefer one strong statement.

A header-only slide can work well here.

---

## Balanced Counterweight

Preserve what was legitimate.

Do not attack specialization, meetings, delegation, process, management, or expertise when the essay's real argument is narrower.

State:

- what was right;
- where the mistake started.

Pattern:

```text
X was not the problem.
The mistake was assuming X also accomplished Y.
```

Examples:

"Specialization wasn't the problem. Making specialization control who could speak to whom was."

"The architect belonged in pre-sales. The mistake was assuming one reviewed call protected every commitment made afterward."

This line can be original writing when required to express the source thesis accurately.

Do not distort the author's thesis for the sake of artificial balance.

---

## Reframe

Move from the specific case to the general operational rule.

The reframe should explain what category of failure the case belongs to.

Do not turn it into generic leadership philosophy.

Bad:

"Communication is important."

Better:

"If information must cross three people to reach the person who needs it, every handoff becomes part of the system design."

---

## Smallest Correction / Operational Close

End the argument with the smallest operational change that solves the mechanism shown.

Use the essay's own thesis or strongest operational line as the closing bookend when possible. Keep it close to the source rather than replacing it with a generic takeaway.

Do not finish with a broad transformation program unless the essay requires one.

Prefer:

- change who joins one conversation;
- add one review point;
- connect two roles directly;
- remove one unnecessary handoff;
- define one required behavior.

The correction should feel proportionate to the failure.

---

## Reflection Question / CTA

The final slide should contain one direct question tied to the exact mechanism.

This is new writing, not a paraphrase of the essay's conclusion.

Do not use:

- "What do you think?"
- "Agree?"
- "Have you experienced this?"
- "Like and follow for more."

Ask something the reader can apply to their own organization.

Example:

"Where does information still need a messenger when the people doing the work could speak directly?"

Keep it quieter than the mechanism reveal or operational close.

Write for a technically competent professional who is progressing fast and wants more leadership responsibility. They may not hold a manager title or have direct reports, but they may already mentor junior colleagues, lead technical decisions, act as a project lead or architect, run interviews, review work, or influence standards.

Do not assume formal authority. Avoid questions that require the reader to manage a department, set company policy, or instruct direct reports.

Target a decision, standard, behavior, or piece of work the reader could already influence. Prefer verbs such as:

- mentored;
- reviewed;
- recommended;
- approved;
- endorsed;
- challenged;
- modeled.

Bad:

"What rule will you require your direct reports to follow?"

Better:

"What did the last piece of work you endorsed teach others was acceptable?"

---

# Slide Count

Default to approximately **8-12 slides**.

This is based on causal beats, not a fixed LinkedIn formula.

Do not map sentences to slides. Group sentences that belong to one state change, and split only when the state changes again.

Use fewer slides if several beats collapse into one state change.

Use more if the source contains more required causal steps.

Do not create filler to reach a target count.

Do not compress several critical state changes into one overloaded slide just to stay below ten slides.

---

# Slide Types

Use three semantic slide types.

## Header Slide

Contains:

- one large statement.

Use it when the sentence itself is the full beat.

Good uses include:

- Hook;
- Mechanism Reveal;
- Smallest Correction / Operational Close;
- Reflection Question / CTA;
- occasional major pivot.

Do not use header slides as generic section separators.

A header slide must advance the argument.

---

## Content Slide

Contains:

- title;
- supporting copy.

Use when the state change requires context.

The title should state what changed.

The body should show enough evidence or action to make it concrete.

## Bullet Content Slide

Contains:

- title;
- `2-5` parallel items introduced with ASCII hyphens.

Use it when one causal beat contains a real enumeration, such as several signals, work items, consequences, or parts of one operational rule.

Do not use bullets to summarize the carousel, list sequential story events, or replace causal transitions. If the items happen one after another and change the state, they belong on separate slides.

Keep every bullet grammatically parallel. Use a plain `-` followed by one space. Do not use round bullets, icons, checkmarks, numbered lists, or decorative markers.

Prefer one line per bullet. Wrap only when the source idea cannot be preserved in one line.

---

# Carousel Writing Style

## Written, not spoken

The video skill rewrites body copy as spoken narration.

Do not import that rule into this format.

Carousel text is read on screen.

Use compact written prose.

Remove connective language that exists only to make speech flow.

Avoid:

- "And here's where things got interesting."
- "Slowly, something started to change."
- "But that wasn't the real problem."

unless the sentence carries information.

Prefer the actual event.

---

# Titles

Slide titles should communicate a state change, discovery, or mechanism.

Aim for approximately **3-9 words** when possible.

Examples:

- "The engineers came in later"
- "The answer needed another messenger"
- "The meeting solved one question"
- "Then the same gap came back"
- "The handoff was the system"

Avoid labels:

- "The Problem"
- "The Issue"
- "What Happened"
- "The Solution"
- "Key Takeaway"

---

# Body Copy

Body copy should contain evidence, action, or consequence.

Target approximately **20-55 words**.

This is a range, not a quota.

A slide can use one short sentence.

Do not pad it.

Prefer 2-3 direct sentences over one large paragraph.

Do not copy full essay paragraphs.

Do not remove the concrete nouns and roles that make the story understandable.

# Bullet Copy

Keep the complete bullet list within the same `20-55` word density range as ordinary body copy.

Use compact phrases or short sentences derived from the source. Do not turn full paragraphs into bulleted fragments.

Make the title frame the shared meaning of the list so the bullets do not need a separate introductory paragraph.

---

# Preserve Strong Source Lines

The user's strongest lines should remain close to the original where possible.

Priority candidates include:

- the thesis;
- the mechanism reveal;
- the balanced counterweight;
- the operational correction;
- a strong consequence line.

Do not rewrite good writing because the workflow says "transform."

Rewrite only when required by:

- carousel density;
- sequencing;
- context;
- clarity.

---

# No Villains

Do not manufacture stupidity.

Avoid writing slides that imply:

- management ignored something obvious;
- another team was incompetent;
- somebody chose the failure knowingly;

unless the source says this.

The stronger pattern is:

```text
reasonable action
-> incomplete protection
-> hidden gap
-> visible consequence
```

This allows the reader to recognize their own systems instead of dismissing the case as bad management somewhere else.

---

# One Throughline

Do not turn the carousel into a montage of examples.

If the source essay contains one primary case, stay with it.

Do not add:

- hypothetical companies;
- unrelated leadership examples;
- extra scenarios;
- invented dialogue.

One case should expose one mechanism.

---

# Causal Integrity

Before accepting a slide sequence, test every transition.

For each pair of slides ask:

**Why does slide B happen because slide A happened?**

If there is no answer:

- a beat is missing;
- the order is wrong;
- or the slides are grouped by topic instead of causality.

Fix the sequence.

The carousel must not feel like a list.

---

# Mechanism Timing

Preview the mechanism in the Promise, then let the case earn it before naming it in full.

Bad sequence:

1. An isolated anecdote with no visible reader value.
2. Several case details.
3. The useful thesis appears near the end.
4. The reader had no reason to reach it.

The reader has nothing to discover.

Better sequence:

1. Concrete Proof plus a compact Promise of useful insight.
2. Reasonable setup.
3. Reasonable response.
4. Response helps.
5. Control ends.
6. Gap survives.
7. Consequence appears.
8. Name the promised mechanism in full.
9. Preserve what was valid.
10. Correct the mechanism.
11. Question.

---

# Visual Specification

Treat every value in this section as the source of truth.

## Fixed Color System

Use this palette on every slide:

- flat charcoal background: `#15100F`;
- amber-gold title and body text: `#EEA530`.

Derive this palette from the user's Leadership Stories visual identity: the charcoal field and illuminated amber edge between active nodes.

Do not use:

- gradient or image backgrounds;
- white text;
- alternate accent colors;
- decorative gradients, textures, glows, borders, or node graphics unless the user requests them.

Keep the pages flat and minimal. The palette connects the carousel to the Leadership Stories identity. Do not copy the reference diagram into the carousel.

## Canvas and Page

- Render each slide on a `1200 x 1200 px` RGB canvas.
- Use a `1:1` aspect ratio.
- Use `120 px` left and right margins.
- Keep text within a `960 px` maximum width.
- Do not show page numbers.
- Do not add logos, labels, frames, or decorative elements beyond the continuation cue defined below.

## Shared Text Vertical Region

- Apply this vertical region to header, content, and bullet content slides.
- Treat `y = 1007 px`, the top of the shared bottom-right cue zone, as the lower boundary of the unobstructed text area. This boundary works for both the swipe cue and the comment cue.
- Center the complete text block between the top of the canvas at `y = 0 px` and the cue boundary at `y = 1007 px`.
- Place the visual center of every complete text block at `y = 503.5 px`, rounded to `y = 504 px` when integer coordinates are required.
- Calculate the block's top position as `504 - (complete text block height / 2)`.

## Typography

- Use DejaVu Sans Bold for titles.
- Use DejaVu Sans Regular for body copy.
- Use the closest metrically compatible sans-serif only when DejaVu Sans is unavailable.
- Use normal word spacing and letter spacing.
- Do not use a contrasting text outline, shadow, glow, or transparency.
- Wrap by words. Never split a word to force a fit.

## Header Slide Layout

- Use title text only.
- Use DejaVu Sans Regular, not bold.
- Add a `1 px` same-color stroke when DejaVu Sans Medium is unavailable. This creates medium visual weight without making the header bold.
- Set the text block from `x = 120 px` to `x = 1080 px`: exactly `960 px` wide with equal `120 px` left and right margins.
- Do not use a narrower default measure for header slides.
- Use greedy width-based word wrapping across the full `960 px` measure. Add words to the current line until adding the next word would exceed `960 px`; then begin the next line.
- On the opener slide, force a paragraph break after each of its three sentences. Wrap each paragraph greedily and independently within `960 px`.
- On other header slides, treat sentence boundaries as ordinary spaces during wrapping. Do not force each sentence onto a new line.
- A header line is invalid if the first word on the next line, including its preceding space, would still fit within the current line's remaining width.
- Apply the unused-width test within each opener paragraph. Do not apply it across an intentional paragraph boundary.
- Do not shorten a line to preserve a preferred phrase. The available measure takes priority over rhetorical grouping.
- If greedy wrapping creates an isolated one-word or two-word final line, rewrite the copy or adjust the permitted header font size, then wrap greedily again. Do not repair the orphan by leaving avoidable unused width on earlier lines.
- Size short headers of up to 12 words at `96 px`.
- Size medium headers of 13-16 words at `84 px`.
- Size long headers of 17 words or more at `68 px`.
- Adjust a size only when the greedily wrapped text produces an unacceptable orphan or cannot fit the safe vertical region.
- Use one fixed line pitch for the complete header: the active font size plus approximately `18%` of that size.
- On the opener slide, leave a paragraph gap equal to `55%` of the active font size, rounded to the nearest pixel. Add this gap after each paragraph except the last.
- Include the opener paragraph gaps when calculating the complete text block height and centering it at `y = 504 px`.
- Do not calculate each vertical advance from the individual line's glyph bounds. Variable glyph heights create visibly uneven line spacing.
- Center the complete header text block at `y = 504 px` using the shared text vertical region.
- Keep all header lines left-aligned.

## Content Slide Layout

- Use a `70 px` bold title.
- Use `18 px` title line spacing.
- Use a `46 px` regular body.
- Use `22 px` body line spacing.
- Use a fixed `88 px` title line pitch: `70 px` font size plus `18 px` spacing.
- Use a fixed `68 px` body line pitch: `46 px` font size plus `22 px` spacing.
- Advance every line by its fixed pitch. Do not derive vertical movement from the visible glyph bounds of each line.
- Leave `54 px` between the title block and body block.
- Center the combined title-and-body block at `y = 504 px` using the shared text vertical region.
- Keep the title and body left-aligned.

## Bullet Content Slide Layout

- Use the same `70 px` bold title and `46 px` regular body type as a standard content slide.
- Render each marker as the ASCII sequence `- ` in the amber-gold text color.
- Place each dash at the `120 px` left margin and begin its text at `x = 162 px`.
- Use a hanging indent: align every wrapped continuation line with the bullet text at `x = 162 px`, not with the dash.
- Use `22 px` line spacing within a wrapped bullet and `30 px` between bullet items.
- Use the same fixed `68 px` body line pitch for every wrapped bullet line, regardless of ascenders or descenders.
- Leave `54 px` between the title block and the first bullet.
- Center the combined title-and-list block at `y = 504 px` using the shared text vertical region.
- Keep the full list within the `960 px` content width and the standard safe margins.

## Interaction Cues

### Swipe Cue

- Add three adjacent open chevrons pointing right to every slide except the final slide.
- Grade the three chevrons from dark to light as they move right: left `#35302F`, middle `#433E3C`, right `#514C4A`.
- Keep the cue inside the bottom-right `120 px` margin.
- On the `1200 px` canvas, use chevron left anchors at `x = 1014`, `1037`, and `1060 px`.
- Draw each chevron from `y = 1026 px` through a point `17 px` to the right at `y = 1043 px`, then back to its left anchor at `y = 1060 px`.
- Use a `7 px` stroke with rounded joins and ends.
- Do not place the chevrons inside a circle or add text beside them.
- Replace the swipe cue on the final slide with the comment cue below.

### Comment Cue

- Add one original speech-bubble icon to the final slide to invite a comment on the reflection question.
- Keep it in the same bottom-right visual zone as the swipe cue.
- Draw a rounded rectangle from `(1002, 1007)` to `(1080, 1056)` with a `13 px` radius, a `5 px` outline, and grey `#514C4A`.
- Add an open lower-left tail using points near `(1018, 1053)`, `(1009, 1071)`, and `(1038, 1054)`. Use the background color to remove the rectangle edge behind the tail, then draw the tail with the same `5 px` grey outline.
- Draw three rounded horizontal message lines inside the bubble. Grade them from dark to light as they move down: top `#35302F`, middle `#433E3C`, bottom `#514C4A`.
- Use a `4 px` stroke. Draw the lines at `y = 1021`, `1032`, and `1042 px`, all starting at `x = 1016 px`, with right endpoints at `x = 1065`, `1058`, and `1048 px`.
- Keep the top and bottom message lines equally inset from the bubble's inner top and bottom edges. Do not move the bottom line closer to the outline.
- Keep the bubble outline one flat grey. Apply the color grading only to the three message lines.

## Density Guardrail

Keep title and body sizes fixed on content slides. If copy does not fit, tighten or split the causal beat before changing type size. Use smaller type only as the final correction, and never below `58 px` for titles or `38 px` for body copy.

---

# PDF Generation

Generate the finished carousel as a square multi-page PDF.

Render each page from the `1200 x 1200 px` RGB slide image and export at `144 DPI`, producing a `600 x 600 pt` square PDF page. Preserve one slide per page and the original slide order.

The workflow is:

1. retrieve and read the complete essay;
2. build causal beats;
3. write carousel copy;
4. render slides with the embedded visual specification;
5. combine slides into one PDF;
6. render the PDF pages back to images;
7. inspect every page;
8. correct layout or copy failures;
9. regenerate if required;
10. return the final PDF.

---

# Layout Failure Rules

If copy does not fit:

1. cut repetition;
2. tighten wording;
3. split a real causal beat if it contains two state changes;
4. reduce font size only after those options fail.

Do not rescue bad scripting with tiny typography.

No page should contain:

- clipped text;
- unsafe margins;
- unequal left and right margins on a header slide;
- overlapping text;
- broken wrapping;
- an avoidable one-word or two-word orphan caused by aggressive wrapping;
- variable header line spacing caused by glyph-based vertical advances;
- missing background;
- unexpected font substitution;
- unreadable density.

---

# Pre-Render Narrative Audit

Before creating the PDF, inspect the script as one sequence.

Check:

- Does the full script follow Proof-Promise-Plan?
- Does slide 1 contain a concrete event, result, failure, or decision as Proof?
- Does slide 1 contain enough person, action, and result context to make sense without slide 2?
- Does slide 1 make the value of swiping visible through a compact Promise?
- Does slide 1 work as a hook rather than a compressed synopsis of later slides?
- Does slide 1 use a definite, known subject when the source establishes one specific case?
- Does the opener create impact through the contrast between the setting, the required shift, and the subject's failed move or consequence?
- Were supporting context, motives, and secondary details left for later slides?
- Does the opener use three short sentences with one contextual job each when the source supports three beats?
- Is each opener sentence rendered as its own paragraph with the specified paragraph gap?
- Does the opener remain clear when read as plain prose without its line breaks?
- Does every opener sentence contain an explicit subject and a complete thought?
- Are Proof and Promise separated into short sentences when combining them would make the sentence harder to parse?
- Do the line breaks support clear writing rather than repair compressed writing?
- Does the opener begin the causal sequence rather than previewing a later event and restarting the story?
- Is the opener new writing rather than a paraphrase of the source opening?
- Is there one primary workplace case?
- Is the first action concrete?
- Does the failed response make sense at the time?
- Did it improve anything?
- Can the exact point where control ends be identified?
- Does the gap survive through a clear path?
- Is there an observable consequence?
- Is the mechanism previewed without being fully explained before the reader has evidence?
- Does the reveal explain the previous slides?
- Does the Promise give the reader a useful claim, test, distinction, or mechanism?
- Does the Plan remain one continuous causal sequence rather than alternating between case and abstract explanation?
- Does the counterweight preserve what was legitimate?
- Is the correction the smallest useful operational change?
- Does the Plan contain concrete actions rather than broad transformation language?
- Does the operational close preserve the source thesis as a bookend?
- Does the final question target this exact mechanism?
- Is the final question new writing rather than a paraphrase of the source conclusion?
- Can a reader with leadership experience but no formal management title answer the final question?
- Does every bullet slide contain one real enumeration within one causal beat?
- Are sequential events still separated into slides rather than flattened into bullets?
- Do all header slides use the full `960 px` measure with equal `120 px` side margins?
- Were all header lines wrapped greedily against their measured pixel width rather than a phrase boundary or word-count target?
- For every non-final header line, would the first word of the next line fit within the remaining width? If yes, the wrapping fails and must be corrected.
- Is every complete text block centered at `y = 504 px`, within the area above the bottom-right cue zone?
- Does every line in a header block use one fixed line pitch?

If these answers are weak, fix the script before rendering.

---

# Compression Audit

For every slide ask:

- Does this introduce a new state?
- Does it contain information the reader needs later?
- Would deleting it break the causal chain?

If not, delete it.

Do not keep slides because their wording is good.

The sequence matters more than individual sentences.

---

# Output Filename

Derive the filename from the essay title.

Format:

`<essay-title>-linkedin-carousel.pdf`

Use lowercase kebab-case where practical.

Example:

`meetings-keep-communication-silos-alive-linkedin-carousel.pdf`

---

# Final Response

Return the PDF.

Keep the delivery message short.

Example:

`[Download the LinkedIn carousel PDF](...)`

State the number of slides only when useful.

Do not paste the complete carousel script unless the user requests it.

---

# Default Decision Rules

When uncertain:

- causal sequence over thematic grouping;
- one concrete case over multiple examples;
- observable behavior over abstract explanation;
- competent actors over manufactured villains;
- mechanism reveal over early moralizing;
- preserve legitimate actions before isolating the failure;
- smallest correction over transformation theatre;
- strong source lines over unnecessary rewriting;
- fewer meaningful slides over filler;
- readable copy over dense pages;
- embedded visual and export specification over external templates;
- author's thesis over generic LinkedIn conventions.
