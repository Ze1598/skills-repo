---
name: godot-foundations
description: Build or change Godot gameplay, scenes, interactions, save state, imported assets, and traversable 3D spaces with clear ownership and targeted native verification. Use for Godot implementation work; performance investigations and PS1 art direction have their own focused skills.
---

# Godot Foundations

Build changes that work through the player's actual controls and survive scene transitions, pause and restoration. Apply these rules to the requested scope; a small fix does not require reorganizing the whole game.

## Establish the working contract

Inspect existing project instructions and the active entry scene. Identify the installed Godot version, target platforms/hardware, renderer and driver, art direction, input model, output-resolution policy, frame target, language and test/build expectations. Preserve established answers. Ask about consequential creative gaps while progressing independent work; resolve routine implementation details yourself.

For a new project or an unclear contract, use the bundled [project profile](assets/project-profile.md). Keep the resulting decisions in that project. Never inherit a previous game's platform, resolution, perspective, story, layout or save-point policy as a universal default.

## Implementation decisions

- Give movement, world construction, interaction, progression, UI, audio and persistence clear owners. Prefer reusable scenes/resources and narrow signals or APIs. Keep a single authoritative source for progression; visuals reflect it.
- Use static types in changed GDScript: parameters, returns, member state and collections. Sound inference is acceptable; validate and convert dynamic input at its boundary. Cache stable node/resource references during initialization or binding. Refresh caches when their owners change, rather than traversing the tree in frame callbacks. See [Godot static typing](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/static_typing.html).
- Build one playable slice through the real inputs before multiplying rooms or content. For 3D construction, read [spatial construction](assets/spatial-construction.md).
- Keep physical movement authoritative in physics updates. Choose animation-driven root motion or controller-driven movement explicitly. Investigate animation reset and camera timing independently from collision geometry.
- Give authored sequences explicit enter, finish and cancel paths. Read [state and lifecycle](assets/state-and-lifecycle.md) when touching cutscenes, pause, pooling, checkpoints or camera ownership.
- Preserve original supplied assets. Put runtime resources inside the project, use reproducible import/derivative settings, and verify scale, orientation, skinning, materials and animations. Avoid dependencies on a user's temporary landing folder.
- Choose renderer features to serve the agreed game and hardware. Query the installed version before applying settings or APIs from moving online documentation. Keep simple work simple; introduce batching, streaming or direct server APIs only when the scene design/counts warrant them.

## Completion evidence

Match verification to the change: parse/import checks first, then meaningful interaction/state checks, then a short native-renderer traversal of changed geometry or camera behavior. A screenshot shows appearance; it does not establish collision, event order or control return. If the user owns playtesting, do focused technical checks and state the remaining manual checks.

Use separate test saves/settings. Verify changed resources in the actual export when a build is requested. Launch it when requested by the project/user. Report changes, evidence and limitations without claiming a full replay from a partial test.

All local supporting resources are bundled within this skill. No prior project checkout is required.
