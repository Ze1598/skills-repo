# Rendering and visibility decisions

## Features and pixel work

Inspect the renderer actually used by the export, including platform overrides. Pick the least complex renderer that satisfies the required features and hardware; do not universally force Mobile, Compatibility or Forward+. Renderer and driver are separate choices. [Renderer overview](https://docs.godotengine.org/en/stable/tutorials/rendering/renderers.html).

Inspect active light counts/ranges, shadow passes, SSAO/GI/reflections, antialiasing, material variants, transparency and fullscreen passes. Match the style with appropriate unlit, vertex-lit, baked or dynamic lighting. Emissive fixture surfaces can provide a visual cue without a live point light at every fixture. Check readability and required moving-object lighting after changes. Do not report disabling a feature that was never enabled.

Profile overlapping transparent surfaces and screen-reading shaders. Simplify invisible or redundant layers; use opaque/cutout materials where they fit the appearance. Reuse material/shader configurations. Viewport effects and texture updates have their own cost even when the main 3D scene is simple. [GPU optimization](https://docs.godotengine.org/en/stable/tutorials/performance/gpu_optimization.html).

## Visibility ownership

Assign rooms, floors or spatial chunks explicit ownership at construction/import time. Keep each visible enclosure complete: floor, ceiling, walls, thresholds, doors, fixtures and props. Shared structural faces may belong to different rooms. Preserve ownership through static merging and instancing.

Set activation from the active viewing camera and reachable sightlines, including authored views. Load or activate the next region early enough to cover approach and preparation. Use hysteresis around boundaries. A current-plus-neighbors policy is one possible layout-specific policy, not a universal three-floor rule.

Visibility, process mode, animation, audio, collision and navigation require separate decisions. Hiding meshes does not automatically stop simulation. Rendering groups are not the same as disk/resource streaming. Disabling collision merely because a region is offscreen can break NPCs, projectiles or return routes.

Merge or instance static repeated meshes within useful spatial cells. One enormous batch can defeat fine culling. Shared props often suit MultiMesh; unique moving objects still need appropriate ownership and control. Account for all viewports and shadow passes in totals. [MultiMesh](https://docs.godotengine.org/en/stable/tutorials/3d/using_multi_mesh_instance.html).

## Distance, fog and assets

Use fog to conceal planned distance transitions while explicitly reducing distant geometry through visibility ranges, simplified substitutes or LOD. Confirm important lights/landmarks remain available. Match silhouettes and transitions from moving viewpoints; alpha fades can add overdraw. [Visibility ranges](https://docs.godotengine.org/en/stable/tutorials/3d/visibility_ranges.html).

Audit triangle density, skinning cost, material surfaces, textures and import settings. Preserve supplied originals and create runtime derivatives. Verify reduced meshes in silhouette and animation, including skin bindings and root-motion behavior. Automatic LOD can need correction on skinned meshes. [Mesh LOD](https://docs.godotengine.org/en/stable/tutorials/3d/mesh_lod.html).

Secondary viewports should update only when needed and use an intentional resolution. Test alignment, aspect, fog and foreground occlusion when using a distant-world substitute. Size changes should be event driven.

## Transition stalls

If group activation stutters, distinguish visibility toggling from resource loading, material/pipeline preparation and excessive scene construction. Preparing assets before they enter view or compiling static geometry during authoring may help. Measure cold and warm paths; prewarming is not free and must not move an unexplained stall elsewhere.
