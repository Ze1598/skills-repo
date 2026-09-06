# Reference-guided image generation

## Model and routing

Distinguish the conversation model, image model, and service routing. Record the actual endpoint; do not describe GPT chat orchestration as direct image synthesis. State whether generation is local or remote and whether source images leave the machine.

A validated route used GPT Image 2 (`fal-ai/gpt-image-2`) through Hermes' configured Nous/FAL service, with reference edits at `openai/gpt-image-2/edit`. These are known-working identifiers, not permanent defaults; check the live model catalog before changing settings. Do not silently change global image settings.

## Prepare reference transport

Use the image tool's supported reference path first. If a remote provider receives a filesystem path rather than image bytes, inspect the installed handler and embed the reference using a supported data URL instead of repeatedly submitting an inaccessible path or publishing private artwork to public hosting.

The working helper imported Hermes' existing `tools.image_generation_tool.image_generate_tool`, preserving configured auth/routing. Discover the installed source and Python environment; do not copy personal absolute paths into reusable tooling.

For transport copies only:

```python
from PIL import Image
from io import BytesIO
import base64

image = Image.open(source_path).convert('RGB')
image.thumbnail((1200, 1200))
buffer = BytesIO()
image.save(buffer, format='JPEG', quality=88, optimize=True)
reference = 'data:image/jpeg;base64,' + base64.b64encode(buffer.getvalue()).decode()
```

Keep originals unchanged. JPEG is a payload tradeoff, not a pixel-art production export; prefer lossless references when exact pixels matter and payload limits allow. For oversized requests, reduce dimensions, compact encoding, or reference count before switching models. Diagnose the actual HTTP status rather than accepting a generic model-availability explanation.

Call the existing generator with `image_url`, additional `reference_image_urls`, a complete prompt, aspect ratio, and `upscale=False`. Avoid creative upscalers on pixel-art references because they may redraw faces, text, and edges.

## Persist and check outputs

Download each returned image immediately. Verify via `PIL.Image.open(path).verify()` and reopen for dimensions. Save prompt, reference paths, actual model, returned URL, local path, dimensions, and success status in a sidecar. Persist per output rather than only at batch completion.

Use visual QA for likeness and layout; successful decoding is not artistic verification. Generated pixel-art appearance is not deterministic downsampling, manual painting, background removal, sprite slicing, or animation. Report only transformations actually executed, and do not promise exact reproducibility without pinned seeds/model revisions.
