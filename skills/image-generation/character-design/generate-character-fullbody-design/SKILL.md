---
name: generate-character-fullbody-design
description: Extend one cropped character image into a complete head-to-toe reference while preserving its identity, visible upper-body design, expression, and original art style. Use for full-body extensions or reference images from portraits and partial-body artwork. Default to a 9:16 canvas, a neutral three-quarter standing pose turned toward the viewer's left, and a plain gray studio background. Do not use for multi-view turnarounds or character showcase sheets.
---

# Generate Fullbody Character

Create one full-body image from the user's supplied character artwork. Extend the character; do not redesign or restyle it.

## Read the input

- Inspect the supplied image before generation. Use it as the sole authority for identity and art style.
- Preserve the face, hair, colors, defining features, visible anatomy, upper-body clothing, accessories, and facial expression unless the user requests a change.
- Use the user's clothing notes to complete unseen areas. If notes are absent, choose a simple continuation consistent with the visible outfit. Ask only when a missing defining detail prevents a faithful result.
- Treat expression and clothing as character-specific inputs. Do not make a depressed expression, hoodie, sweats, or socks defaults for other characters.

## Preserve the art style

Match the source's linework, facial construction, stylization, proportions, palette, shading, highlights, hair detail, fabric treatment, and level of detail. Carry the same rendering into the new lower body.

Do not impose flat cel shading, realism, glossy rendering, extra detail, or a different head-to-body ratio. Do not use another character or an earlier failed generation as a style reference. Preserve the supplied upper-body design as closely as the new standing pose allows; change its pose only as required. Do not mirror asymmetric clothing, hair, or markings to achieve the requested orientation.

## Use the default composition

- Use a 9:16 portrait canvas.
- Show one complete character, head to toes, including all hair, head accessories, and footwear or sock-covered feet.
- Use a neutral three-quarter standing pose. Turn the torso and face toward the left edge of the image, from the viewer's perspective. Keep both eyes visible; do not use a side profile or a right-facing pose.
- Keep the arms away from the torso, hands visible, fingers distinct, and legs separated. Use a relaxed stance, not a T-pose or an exaggerated spread.
- Preserve the source expression. Do not substitute a head tilt, slouch, smile, or dramatic emotion for the actual facial expression.
- Keep anatomy consistent with the source's stylization. Fit the figure through framing and margins; do not stretch the torso or legs to fill the canvas.
- Use a simple gray studio background and restrained ground shadow. Remove the source scene without changing the character's rendering style.
- Exclude text, borders, panels, extra views, props, and extra characters unless requested.

Honor explicit user changes to these defaults.

## Generate

Use the built-in image-generation tool with the inspected original image as the reference. Keep the prompt close to this template; fill brackets from the supplied image and user notes, then remove the brackets:

> Extend the referenced character into a complete full-body design while preserving the referenced upper body, character identity, and original art style. Neutral three-quarter standing pose, complete head-to-toe view, arms away from torso, clear leg separation, clear finger separation. [Character-specific clothing and footwear.] Preserve [the reference's facial expression or the requested expression]. Simple gray studio background, accurate anatomy consistent with the source's stylization. Character is turned toward the viewer's left, with face and torso angled toward the left edge and both eyes visible. 9:16 portrait canvas with the entire figure inside the frame. Preserve the source's linework, proportions, shading, colors, and level of detail throughout the new full-body image. One character, no text or panels.

Do not replace generation with a prompt-only response unless the user asks for a prompt.

## Check the result

Compare the result with the original image. Check identity, expression, visible costume, and art style before judging polish. Confirm left-facing three-quarter orientation, complete 9:16 framing, natural proportions, gray background, and readable limb and finger separation. If a requirement fails, correct that failure while retaining the original image as the source of truth. Do not repair style drift by borrowing another character's style.
