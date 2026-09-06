# Sprite extraction from approved boards

> **Deprecated for subject sprites.** Color-keying/region extraction of character-and-critter boards was tried and rejected by the user: it keys the dark-navy background out of dark-internal designs (hair, clothing, shadows), producing hole-riddled sprites. The user then chose to regenerate every asset as an individual transparent PNG. For characters, enemies, bosses, and props follow [transparent-generation.md](transparent-generation.md) (individual API generation, never extraction).

## Minor use that survives

Extraction still has a valid, narrow role for artifacts whose design colors do NOT overlap the board background and that do not need per-subject regeneration: full-scene paintings, large environment/composite tiles, and scale-reference strips kept as source material. Key these sparingly with the tolerance method below and verify the design has no internal pixels near the background color range before committing.

## When the user rejects extraction, pivot once

If a keyed result comes back with holes eaten out of dark regions, do NOT iterate tolerances or try flood-fill tricks. Surface it and expect the user to choose regeneration. The mechanism is a fundamental ambiguity, not a tuning error: dark board backgrounds share a color range with dark design interiors, so no color rule can separate them reliably.

---

_Historical color-keying method retained below for its narrow valid uses._

## Pitfall: boards are not layered files

Generated boards are flat opaque composites. Backgrounds are approximately uniform but may include subtle gradients, decorative borders, anti-aliased edges, or glow effects that resist clean color-keying. Audit crops at game scale before committing to a keying strategy. Report what cannot be cleanly extracted instead of promising production-ready cutouts.

## Background color-key removal

Most pixel-art boards use a near-uniform dark navy background (~`#12172a`). Remove it with a per-channel tolerance:

```python
from PIL import Image

def key_out(img, bg=(0x12, 0x17, 0x2a), tolerance=45):
    img = img.convert('RGBA')
    pixels = img.load()
    for y in range(img.height):
        for x in range(img.width):
            r, g, b, a = pixels[x, y]
            if (abs(r - bg[0]) <= tolerance and
                abs(g - bg[1]) <= tolerance and
                abs(b - bg[2]) <= tolerance):
                pixels[x, y] = (0, 0, 0, 0)
    return img
```

After keying, trim transparent borders with `img.getbbox()` + `crop()`.

### Tolerance selection

- Too tight (<30): leaves background fringes, especially on anti-aliased pixel edges.
- Too loose (>60): eats dark parts of the sprite (black clothing, dark hair, shadows).
- 40-50 is the typical working range for navy boards. Verify by counting opaque pixels that still match the background color — if a keyed sprite has >100 such pixels, the tolerance may be too tight.

## Region-based cropping

Boards arrange sprites in predictable grids. Crop by region, then key:

```python
def extract_region(board_path, region, out_path, key=True):
    img = Image.open(board_path).convert('RGBA')
    cropped = img.crop(region)
    if key:
        cropped = key_out(cropped)
        cropped = crop_transparent(cropped)
    cropped.save(out_path)
```

Determine region coordinates by inspecting board dimensions and grid layout. Character boards typically have evenly-spaced columns; enemy boards use NxM grids. Record the regions used so extractions are reproducible.

## Do not key these

Full scene paintings, prop-panel strips, and reference composites should be extracted with `key=False` — they are source material for in-engine tiling or further manual slicing, not individual sprites.

## Verify alpha programmatically

Vision tools render transparent PNGs on white/checkerboard and cannot be trusted for alpha verification. Always check programmatically:

```python
img = Image.open(path)
assert img.mode == 'RGBA'
pixels = list(img.getdata())
transparent = sum(1 for p in pixels if p[3] == 0)
leftover_bg = sum(1 for p in pixels if p[3] > 200 and color_matches_bg(p))
```

A cleanly extracted sprite has high transparent percentage and near-zero leftover opaque background pixels.

## Generate preview page

After extraction, emit an HTML page showing every sprite on a checkerboard background at actual pixel size. This is the user's verification tool before game coding. Embed PNGs as base64 data URLs; no server needed.

```html
.checker {
  background-image: linear-gradient(45deg, #1e2530 25%, transparent 25%), ...;
  image-rendering: pixelated;
}
```

## Known limitations

- Wide strips (environment panels, attack rows) often contain multiple motifs per file — these are source strips, not individual sprites.
- Glowing effects (fire, ice nova, lightning) have soft edges that don't key cleanly. Extract with glow intact rather than trying to hard-cut.
- Sprites from the same board share a pixel density but may differ in exact dimensions. Normalize in-engine, not by rescaling source.
