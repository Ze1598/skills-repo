# Project decisions to establish

Use an existing project document if it already answers these questions. Record only missing decisions relevant to the work; this is not a mandatory questionnaire or a reason to delay a small change.

| Decision | What to resolve |
|---|---|
| Engine/runtime | Exact Godot version; active scene; build/export workflow |
| Platforms | OS targets, intended input devices, baseline hardware |
| Presentation | Perspective, visual references, readability/accessibility needs |
| Display budget | Output and 3D resolution policy, aspect ratios, frame target/caps |
| Rendering | Renderer and driver separately; required features; effects budget |
| World | Units, player clearance, traversal rules, intended boundaries |
| Interaction | Input actions, reachable targets, carried objects, progression gates |
| Persistence | Save ownership/version, restoration semantics, test fixtures |
| Content | Source of truth, language, adaptation decisions requiring the designer |
| Delivery | Export destination, launch preference, agent checks vs user playtesting |

A technical improvement does not authorize a different camera, language, story beat, resolution or visual style. Existing instructions can already authorize a tradeoff; do not ask again merely because it is mentioned here.

For renderer selection, compare required features and target hardware using the [official renderer overview](https://docs.godotengine.org/en/stable/tutorials/rendering/renderers.html). Mobile is a renderer name and can also serve desktop games; the platform name alone does not determine the choice.

Maintain references portably. When a reference is essential, copy the permitted resource into the project's own assets or the reusable skill's assets as appropriate. Do not leave instructions dependent on an unrelated checkout or temporary screenshot location.
