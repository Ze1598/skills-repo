# Transparent sprite generation from approved boards

## Why extraction fails

Generated boards are flat opaque composites with a uniform background. Color-keying
(background removal by pixel color) works ONLY when the background color does not
appear inside any design. For dark-navy boards, this fails immediately: black hair,
dark clothing, shadows, and dark outlines all share the background color range.
Keying eats holes through characters. This is not a tolerance-tuning problem — it is
a fundamental ambiguity.

**Rule: generate transparent PNGs directly. Never color-key generated boards.**

## Pipeline architecture

Use a single reusable script + YAML manifest:

```
media/assets/_process/generate.py       # pipeline (one for the whole project)
media/assets/_process/manifest.yaml      # all image definitions
```

### generate.py

- Accepts `--manifest <path>`, `--only <id>...`, `--dry-run` flags.
- Each manifest entry: `id`, `prompt`, `target`, `aspect_ratio`, `references`, `upscale`.
- Encodes local references as JPEG data URLs (max 1200px, quality 88) to stay under HTTP 413.
- Calls `tools.image_generate_tool.image_generate_tool` (the existing Hermes wrapper — preserves auth routing).
- Downloads to `target`, verifies PNG decode + alpha channel, writes per-asset metadata JSON.
- Skips already-generated assets on retry (idempotent by target path).
- Writes a run log with all results.

### manifest.yaml

```yaml
- id: ignara
  prompt: >
    Generate a single full-body front-facing idle pose pixel-art sprite...
  target: media/assets/characters/ignara.png
  aspect_ratio: portrait
  references:
    - media/pixel_art_reference.png
    - media/assets/review-v1/01-playable-characters.png
    - media/original_designs/Ignara.png
```

## Enabling `background="transparent"`

GPT Image 2 supports `background="transparent"` natively. The Hermes FAL wrapper
silently drops any parameter not in the model catalog's `supports` whitelist
(`_build_payload` filters `if k in supports or k in required`).

**Fix: add `background` to the catalog entry.**

In `~/.hermes/hermes-agent/tools/image_generation_catalog.py`, for `fal-ai/gpt-image-2`:

```python
defaults={"quality": "medium", "num_images": 1, "output_format": "png", "background": "transparent"},
supports={"prompt", "image_size", "quality", "num_images", "output_format", "sync_mode", "background"},
```

And the same `background` key in `edit_supports` for the edit endpoint. Once set, every
generation outputs RGBA PNGs with transparent background by default.

## One sprite per image

Generate ONE sprite per API request. Do NOT generate strips containing multiple assets (e.g. "3 fire attacks on one strip"). Strips with particles, effects, or anti-aliased edges cannot be reliably auto-sliced — connected-components detection finds hundreds of tiny regions from noise/particles, and flood-fill from corners fails when content touches frame edges.

Exception: animation frames for a single logical asset (e.g. 4-frame projectile sequence) may share one image since they're divided by fixed grid cropping, not content detection.

For N similar assets (e.g. 12 icons, 6 pickups), write N manifest entries — one prompt, one output file each. The loop is deterministic compute, not per-asset agent cognition.

## Content policy failures

Some prompts trigger `content_policy_violation` from the provider. Common triggers:
- "adult" (use "mature" or omit age descriptors)
- "showing teeth" (use "confident expression" or "slight smile")
- "no legs" + creature descriptions (describe as "tentacle lower body" without negation)

**Fix: rephrase the prompt, not the design.** The content filter is keyword-based.

Rephrase by softening triggering descriptors, not by deleting design-identity traits. Dropping
a defining trait (e.g. skin color, exact limb count) makes the model free to invent a
substitute, so after a sanitized retry succeeds, spot-check the regenerated sprite against
the identity constraints that were softened (limb count, skin/hair color, clothing). State
non-negotiable traits explicitly even in sanitized wording (e.g. "TWO arms only").

## Verification

Vision tools render transparent PNGs on white/checkerboard — they cannot verify alpha.
Always check programmatically:

```python
from PIL import Image
img = Image.open(path)
assert img.mode == 'RGBA'
pixels = list(img.getdata())
transparent_pct = sum(1 for p in pixels if p[3] == 0) / len(pixels) * 100
```

A good sprite is 40-85% transparent. 0% means transparency failed; >95% means
the sprite may be empty.

## Folder convention

Assets go directly under `media/assets/` by category — not in versioned subdirectories:

```
media/assets/characters/
media/assets/enemies/
media/assets/bosses/
media/assets/effects/
media/assets/ui/
media/assets/environment/
```

Do not create intermediate folders like `game/` or `game-v2/` — these are clutter.
Clean up test/prototype folders before the user asks.

## Staged generation

Generate in stages by category. After each stage:
1. Present the actual images for review.
2. Wait for approval before generating the next category.
3. The user may readjust prompts or references between stages.

This avoids spending the full batch budget on assets that need revision.

## Rate limits and mid-batch failures

The FAL image gateway enforces a sliding request limit (~200 per window). Hitting it returns
`RATE_LIMIT_EXCEEDED` per-image; the generate.py loop marks that entry FAILED and continues —
it is not a fatal batch error and prior successes already persisted.

- After a run, read the summary (N succeeded, M failed) and list the failed `id`s.
- Retry the failed ids with `--only <failed id...>`; a short delay between sequential retries
  lets the window reset. Run several independent batches concurrently to stay under the burst
  ceiling, but re-run single retries serially.
- A "succeeded" count less than the requested count, or full-strip outputs left in the target
  folder, means some entries silently did not generate — reconcile against the expected ids
  rather than trusting the exit code.

## Review transparent sprites without vision tools

The vision stack renders RGBA PNGs on white/checkerboard, so it cannot confirm transparency and
its topic descriptions are unreliable on small or cropped sprites — running it is wasted spend.
Review generated sprite output with the art tooling the game actually uses (a checkerboard preview
page) plus the programmatic alpha checks above; reserve vision for large concept boards where it
adds value.
