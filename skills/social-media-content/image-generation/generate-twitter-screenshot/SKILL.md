---
name: generate-twitter-screenshot
description: Generate a 1:1 X/Twitter-style post screenshot for José Fernando Costa from supplied post text. Use when the user asks for a Twitter screenshot, X post image, social post mockup, or another image matching the saved @villager1598 design. Keep the account identity, compact centered layout, active repost/like/bookmark states, hidden engagement counts, and randomized recent age and sub-138 view count.
---

# Generate Twitter Screenshot

Create one square raster image from the user's post text.

## Fixed identity and design

- Display name: `José Fernando Costa`
- Handle: `@villager1598`
- Use `assets/profile.png` for the circular avatar.
- Use `assets/twitter-layout-reference.png` as the strict reference for layout, scale, typography, colors, spacing, icon states, and vertical centering.
- Output an exact 1:1 image.
- Center the complete post block vertically with equal white space above and below.
- Keep the compact mobile-post scale. Do not enlarge the interface to fill the square.
- Keep reply and share icons muted gray.
- Show repost as active green, heart as active solid pink, and bookmark as active solid blue.
- Show no engagement numbers beside any toolbar icon.
- Include the visibility icon, overflow dots, thin dividers, white background, dark post text, and blue-gray metadata.
- Do not add a header, back arrow, verification badge, attached media, browser chrome, watermark, disclaimer, or mockup label.

## Workflow

1. Take the user's supplied post text verbatim. Preserve its spelling, punctuation, capitalization, paragraph breaks, and line breaks when practical.
2. Run `python3 scripts/randomize_metadata.py` from this skill directory. Read its JSON output.
3. Format the metadata line exactly as `<hours> hours ago · <views> Views`.
4. Confirm that `hours` is from 3 through 20 inclusive and `views` is from 3 through 137 inclusive. Run the script again if either value is outside its range.
5. Load both bundled PNG assets with the image-viewing tool before generation so they are visible to the image workflow.
6. Use the built-in image-generation tool with both images as references:
   - `twitter-layout-reference.png`: strict UI and composition reference.
   - `profile.png`: high-resolution avatar source.
7. In the prompt, quote the post text and metadata line as exact verbatim text. Repeat all fixed design rules above. State that the complete content block must remain inside the square without cropping.
8. Inspect the output. Verify the account identity, exact post text, random metadata values, 1:1 ratio, centered content block, icon states, and absence of toolbar counts.
9. If one item is wrong, make one targeted edit and preserve all correct elements.
10. Return the generated image. Do not expose the internal randomization or generation prompt unless the user asks.

## Metadata rules

- Randomize once per requested image.
- For multiple images, run the script once for each image.
- Do not infer engagement counts from the view count.
- Never show toolbar engagement counts.
- Keep `Views` capitalized.
- Use `hours` for all permitted values.
