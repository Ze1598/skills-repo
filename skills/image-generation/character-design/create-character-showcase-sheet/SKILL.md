---
name: create-character-showcase-sheet
description: Create a polished tall-portrait original-character showcase sheet from character artwork, a full-body pose reference, and written character notes. Use when the user asks for a character sheet, expression sheet combined with a full-body showcase, original-character dossier, or another sheet matching the established left-side full-body and right-side face-grid format.
---

# Create Character Showcase Sheet

Create one finished raster image with a fixed information hierarchy and a visual treatment adapted to the character.

## Inputs

Collect:

- A character identity reference that shows the face, hair, colors, and defining features.
- A full-body or pose reference when the user wants a specific pose, outfit, or silhouette.
- The character name and introduction or profile notes.

Accept one image for both identity and full-body roles when it shows enough detail. If a requested pose or defining feature is not visible, ask for the missing reference before generation. Treat extra style or layout images as supporting references and state each image's role in the generation prompt.

## Derive the copy

Compress the introduction into these elements without inventing traits:

1. A large character name.
2. A short subtitle that captures the central contrast or hook.
3. Three profile blocks:
   - identity, style, or self-presentation;
   - first impression;
   - true nature, hidden contrast, or defining behavior.
4. Three short personality-trait plaques.

Use a short uppercase heading and one direct sentence for each profile block. Keep the sentence compact enough to read inside the sheet. Do not place biography paragraphs in the image. Preserve blunt or specific character details instead of replacing them with vague praise.

## Use the fixed layout

Use `assets/character-showcase-layout-reference.png` as the composition reference only. Never copy Miyako's identity, costume, palette, ornaments, or personality into another character.

Build the page in this order:

1. Match the layout reference's tall portrait canvas: approximately 0.64 width-to-height (near 5:8), with a narrow border or framing system suited to the character. Do not use 4:5.
2. Place the name and subtitle across the top.
3. Reserve about 43% of the main width on the left for one large, unobstructed, head-to-feet full-body view.
4. Reserve the upper right for eight equal square face close-ups in a clean 2-column by 4-row grid.
5. Place a compact four-cell `DETAIL STUDY` panel below the expression grid.
6. Place the three profile blocks in a lower information band across the page.
7. Place the three personality plaques across the absolute bottom.

Keep the hierarchy ordered. Do not use a scattered scrapbook composition.

## Build the expression grid

Make each cell a tight face crop like a gacha expression sheet:

- Show the face and enough hair to preserve identity.
- Exclude torso, hands, props, decorative portrait frames, captions, and expression names.
- Keep all eight cells the same size.
- Preserve the same facial proportions, colors, makeup, markings, and age in every cell.
- Make the expressions distinct enough to read without labels.

Choose expressions that expose both the public impression and private personality described in the introduction. A useful range includes neutral, faint smile, startled, affectionate, cheerful, eyes closed, flustered, and playful, but adapt the set when the character calls for different emotions.

## Build the detail study

Choose four identity-bearing details visible in the supplied references, such as jewelry, fabric construction, markings, hands or nails, footwear, weapon fittings, or signature accessories. Use tight visual crops. Do not invent important costume parts that the references do not support.

## Match the character

Adapt the border, background, motifs, typography, and palette to the character while preserving the fixed layout. Match the rendering medium of the identity reference unless the user requests another style. Present sensual clothing as character design and self-expression; do not change the pose into pin-up staging unless requested.

Use the built-in image-generation workflow. Identify each input image's role in the prompt and repeat the identity, pose, costume, text, layout, and exclusion constraints. Generate directly once the required inputs are present.

## Validate and correct

Inspect the result before delivery. Confirm:

- tall portrait format matching the layout reference, approximately 0.64 width-to-height (near 5:8), not 4:5;
- one complete full-body view on the left;
- eight unlabeled face-only squares on the right;
- one consistent identity across all nine depictions;
- four detail studies below the expression grid;
- title, subtitle, three profile blocks, and three bottom traits;
- readable copy with no filler text;
- no unrequested characters, props, costume changes, or watermarks.

If the generator turns face cells into bust portraits, scatters the expressions, adds labels, or changes identity, regenerate with that single failure stated as the dominant correction. Do not accept a result that misses the left/right structure.
