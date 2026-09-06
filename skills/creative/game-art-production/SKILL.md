---
name: game-art-production
description: "Use when creating game art and approval packs."
metadata:
  hermes:
    tags: [game-art, pixel-art, image-generation, approval, sprites]
---

# Game Art Production

## Standing user preferences

- Clarify consequential requirements before implementation. For this user's games, when artwork approval is requested before code, cover playable characters, enemies, minibosses, final bosses, environment, effects, pickups, and interface—not just heroes.
- Preserve supplied character identities, anatomy, and costumes. Treat original designs as identity references and style sheets as rendering references. Surface meaningful conflicts instead of silently inventing a compromise.
- Revise only the category the user requests; keep approved artwork unchanged and record which version is authoritative.
- Keep internal helpers, explorations, prompts, response metadata, and assistant working notes out of version control when requested, while retaining approved artwork and user-authored briefs.
- Define the approval scope up front: concept direction, final sprites, animation, or all artwork. Do not call the gate closed and then reveal another mandatory approval stage.
- Surface problems immediately. When a technical approach fails (extraction, generation, transport), stop and report — do not iterate through multiple fix attempts unprompted. The user decides the next step. No apologies, no rabbit holes.
- Prefer reusable, parameterized pipelines over one-off scripts. A single `generate.py` that loops through a YAML manifest of image definitions is preferred over per-category generation scripts. Each manifest entry specifies: id, prompt, target path, aspect_ratio, references, upscale.
- Coding style: write reusable code ONCE (cognition), then execute deterministically in a loop (compute). Never repeat agent work that a script can do. Pay for cognition to build the pipeline, pay for compute to run it.

## Procedure

### 1. Inspect and clarify

Read the brief and inspect reference files. Load original images and style sheets with `vision_analyze`. Record silhouette, anatomy, palette, hair, clothing, weapons, and relative scale. Ask only questions that materially change the output.

Translate ambiguous environment terms into substrate, shoreline, weather, mood, perspective, and traversal space. A coast may mean storm-dark sand and rough surf rather than a stone plaza. Keep project-specific design decisions in a project art-direction note, not in this skill.

### 2. Define the review pack

Group boards by coherent category: playable roster; mobs; bosses; environment/props; attacks/effects; UI/pickups. Give each a stable identifier for feedback.

Specify subjects, labels, layout, references, camera perspective, spacing, and exclusions in prompts. Mark new names and lore-like details as proposals. Preserve readable combat ground; push decorative clutter and strong weather effects toward the perimeter.

Request crisp pixel clusters and consistent scale, but label generated boards as visual concepts until native pixel grids, transparency, and frame geometry are verified. Static action poses are not animations.

### 3. Generate with provenance

Verify the actual image backend/model instead of assuming the chat model also generates images. Use the configured image tool and original references. See [reference-generation.md](references/reference-generation.md) for the tested transport and output workflow.

Preserve originals. Save artwork to the requested asset directory; save prompts and metadata separately. Use bounded concurrency and persist each successful output immediately, so retries skip finished work.

### 4. Verify and present

1. Verify image decoding and dimensions.
2. Count outputs programmatically against the requested categories.
3. Inspect every board for identity, missing subjects, clipping, anatomy, labels, and perspective.
4. Reinspect tiny details in focused crops when full-board vision descriptions conflict. A crop boundary is not proof of clipping in the original.
5. Present actual images using platform file delivery, with short labels and explicit review status.
6. Ask for approval or changes by identifier; update the project note when approved and retain superseded art as history.

### 5. Production generation of transparent sprites

Approved concept boards are references, not final assets. Engine-ready transparent sprites are generated with `background="transparent"` set in the image API — never by color-keying the boards.

See [transparent-generation.md](references/transparent-generation.md) for the tested pipeline: reusable generate.py + YAML manifest, the `background="transparent"` catalog fix, and the failure modes that block extraction.

Rules:

- Generate transparent PNGs directly from the image API. Do not attempt background removal on generated boards — color-keying fails when the board background color appears inside designs (dark hair, dark clothing, shadows), which is the common case.
- Use a single `generate.py` pipeline that reads a YAML manifest. Each manifest entry: `id`, `prompt`, `target`, `aspect_ratio`, `references`, `upscale`. Loop through entries; skip already-generated assets on retry.
- Generate in stages by category (characters first, then enemies, etc.) so the user can review and readjust before spending on the next batch.
- Audit source crops at intended game scale before processing. Report failures without calling an image service.
- If source artwork cannot support an item, stop that item and propose a specific paid replacement batch with a request cap and verified cost basis. Do not silently lower visual quality or spend money.
- Render UI text separately in-engine; baked labels, stats, and height markings from generated boards are illustrative unless explicitly approved.

### 6. Repository hygiene

Keep the working tree free of prototype/strip/test folders before handing off (the path is "v2"
alongside "v1", which is clutter), and cache only the artifact variants you actually want the
runtime to load — for transparent sprites the runtime asset dir will be inspected on disk,
so leave no opaque/composite/strip remnants beside a "clean" regenerated sprite with a
similar name (a leftover stripped or opaque output silently shadows or competes with the
regenerated one).

Inspect existing `.gitignore`, `git status --short --untracked-files=all`, and `git ls-files` before editing ignores. Add narrow patterns for actual internal artifacts: project `.hermes/`, asset `_process/` and `_explorations/`, review metadata/working notes, Python caches, and `.DS_Store`.

Commit a unit test (pytest or plain Python asserts) that checks every produced asset exists, has the expected alpha/transparency range, is not blank, and meets minimum dimensions. Run it instead of ad-hoc inspection. When the user says "run checks," that test suite (plus a checkerboard preview page for art-side review) is the verification path — vision tools are wasted spend on transparent sprites.

Game-art builds are long-running by nature and frequently resumed. Before starting work in a
new session of an existing project, reconcile the repo (see [session-handoff.md](references/session-handoff.md)):
tree on disk vs ROADMAP/notes vs git. Persist canonical paths, the registry-to-test contract,
and run commands into the pipeline docstring and manifest banner so a later session gets them
even without reading the roadmap. After any restructure, search docs for stale path tokens and
old counts and correct them in place. Keep approved-or-superseded state explicit.

Do not blanket-ignore asset folders or all JSON/Markdown; future runtime manifests and user briefs must remain includable. Test both ignored and retained paths with `git check-ignore --stdin`. Ignore rules do not untrack files; do not remove tracked content without authorization.
