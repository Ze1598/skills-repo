---
name: godot-ps1-art-direction
description: Establish or maintain a coherent PS1-inspired 3D visual style in Godot across environments, characters, textures, lighting, animation and presentation. Use when PS1/retro 3D art direction is requested or established; do not impose it on unrelated Godot projects.
---

# Godot PS1 Art Direction

Make the style intentional across the scene. Preserve readable gameplay, stable architecture and responsive controls. Derive the treatment from the current game's references and needs; PS1-inspired does not automatically mean horror, dark palettes, first person, low output resolution or deliberately unstable geometry.

## Establish a small visual contract

Use the user's established direction and approved examples first. Resolve only material gaps: how stylized the models should be, palette/texture treatment, lighting approach, optional retro artifacts, UI readability and motion comfort. Keep numerical budgets and platform choices in the current project.

For a new look, create a small representative sample containing architecture, a prop, a character silhouette and lighting/fog as relevant. Review that sample before multiplying assets when a major creative choice remains unresolved. Existing approved direction authorizes routine consistent implementation.

The bundled [visual examples](assets/visual-examples.md) include actual copied images. Inspect their pixels with an image viewer when useful. They illustrate shape, texture and atmosphere relationships; their layouts, colors, setting and characters are not defaults for future games. They require no original project files.

## Apply the treatment consistently

Read the bundled [visual and technical treatment guide](assets/visual-treatment.md) for modelling, materials, texture imports, lighting, fog, animation and optional effects.

- Establish silhouette and large forms before texture detail. Allocate geometry to what the camera can read and what must deform.
- Keep texture density and detail scale coherent across adjacent assets. Use a controlled material/palette family; inspect floor and wall textures during movement.
- Compose light and color so routes, interactable objects and character poses remain legible. Pick simple shading where it supports the look, with deliberate contrast and depth cues.
- Preserve smooth input, camera behavior and collision even if visual poses update at a lower rate. Treat deliberate retro effects as adjustable presentation choices.
- Combine atmospheric concealment with real visibility/LOD policy. Never claim that adding fog automatically removes distant rendering work.
- Preserve supplied originals and create separate runtime derivatives. Verify identity, silhouette, skinning and animation after simplification or restyling.

## Review and handoff

Compare changed assets together at actual gameplay distance, near interaction distance and during camera movement. Check joins, texture shimmer, silhouettes against the background, lighting transitions and the UI. Inspect animation loops and control handoffs where affected. Fix accidental z-fighting, clipping, missing surfaces and camera jitter as defects.

Verify style-specific settings against the installed Godot version and export renderer. State the visual choices made and their expected technical costs; measure performance before claiming savings. Do not silently lower render resolution or remove required visual features. Keep any agreed exceptions explicit and local to the project.

All supporting examples and authored guidance are bundled in this skill's assets. Its use does not depend on another skill being installed.
