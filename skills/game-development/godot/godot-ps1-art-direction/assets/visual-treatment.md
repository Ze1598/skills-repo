# A coherent modern PS1-inspired treatment

## Form and architecture

Start with a readable silhouette and intentional planes. Allocate edges to important contours, joints and held objects; avoid density that disappears below a pixel at gameplay distance. A flat-shaded style can use deliberate hard edges, while some forms benefit from limited smooth normals. Low-poly meshes alone do not determine the look.

Use consistent scale and modular proportions. Keep inhabited spaces structurally plausible: connected doorways, supported fixtures, complete intended enclosures and usable stairs/landings. Detail should explain use, wear and history. Repetition can establish a place, but vary a few meaningful props, materials or arrangements to support navigation.

Choose asset triangle/material budgets by role and measured scene cost. Keep originals and derive runtime assets. Character simplification must retain facial/silhouette cues needed by the story, joint deformation, bindings and imported animation orientation. Automatic LOD needs animation checks, especially for skinned assets. [Mesh LOD](https://docs.godotengine.org/en/stable/tutorials/3d/mesh_lod.html).

## Texture and material language

Specify texel density across asset families; reserve higher detail for readable story objects. Model silhouettes and large surface changes, and paint small wear or shading where useful. Avoid highly detailed photo textures on adjacent simple stylized models without a deliberate treatment.

Use coherent palettes and value separation. Build texture size/filter choices around viewing distance and intended sharpness. Inspect nearest sampling with mipmaps for receding 3D surfaces; mipmaps help limit shimmer. Compression can damage small pixel-art textures, while large textures may benefit from platform-appropriate compression. Test atlas padding and lower mip levels for bleeding. UI texture choices can differ from world textures. [Image import options](https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/importing_images.html).

Choose rough, unlit, vertex-lit or baked treatments as appropriate. Avoid accidental glossy materials from imports. If lighting is painted into a texture, consider how additional dynamic light affects it. Preserve material sharing and limit unnecessary shader feature combinations.

## Light, atmosphere and visibility

Use broad value/color relationships and local emphasis before expensive effects. A matte scene still needs enough separation to read objects and depth. Vertex lighting depends on vertex placement: a very large polygon may not express a small localized light well. Painted shading, restrained baked light or selective simple lights can provide a better result.

Visible luminous fixtures can be emissive surfaces without each requiring a live shadowed light. Deliberate contact grounding can come from texture, simple decals or baking; avoid making everything appear to float. Use dynamic shadows only where they serve an agreed need and fit the budget.

Fog distance and color affect navigation and threat readability. Preserve the player's required reaction space and key landmarks. Pair the chosen fog envelope with explicit geometry culling or simplified distant silhouettes, testing transitions from both directions. Horror is one application; bright, colorful retro scenes can use the same disciplined shapes and textures.

Confirm feature support for the selected renderer. Mobile, Compatibility and Forward+ have different capabilities and costs; renderer selection belongs to the project's requirements and measurements. [Renderer overview](https://docs.godotengine.org/en/stable/tutorials/rendering/renderers.html).

## Poses, movement and presentation

Prioritize strong poses and restrained gestures that communicate intent. Stepped posing or a lower visual update rate can suit the style, but keep elapsed animation time correct and separate from movement speed. A controller-driven walk must not snap backward at each animation loop. Preserve responsive camera/input and collision timing.

Treat vertex snapping, affine-style texture distortion, palette quantization and dithering as optional. Introduce them individually at restrained strength; verify temporal behavior and interaction readability. They need not be historically exact to support the agreed modern interpretation. No fullscreen effect is free merely because it looks retro.

Use readable typography, consistent UI contrast and a clear distinction between diegetic screens and overlays. Low-resolution world textures do not require unreadable subtitles. Output resolution, 3D render resolution and texture resolution are independent choices; change them only within the agreed project policy.
