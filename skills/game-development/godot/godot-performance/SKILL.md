---
name: godot-performance
description: Diagnose and improve Godot frame time, stuttering, loading spikes, memory use, and excessive rendering or processing cost using reproducible measurements. Use for performance investigations or high-count runtime systems; preserve the project's visual and gameplay requirements.
---

# Godot Performance

Find the work responsible for the reported cost, reduce it, and verify the result. Keep scope proportional to the evidence. A low-poly appearance does not establish a cheap rendering pipeline.

## Start with a reproducible case

Read the project's established hardware, renderer, output-resolution, frame-target and art requirements. Preserve them. Reproduce the reported camera movement, route or interaction on the intended native renderer and window mode. Distinguish continuous low throughput, isolated stalls, input/camera judder and startup/loading time.

Record engine/build, hardware, renderer and driver, physical drawable and 3D render sizes, scaling, frame cap, VSync, test scene/state and timing method. Retina/HiDPI drawable sizes can exceed logical window dimensions. Keep diagnostic saves/settings separate from normal play.

Use the bundled [measurement procedure](assets/measurement.md) before drawing conclusions from frame timings. Its [frame analyzer](assets/frame_report.py) summarizes captured intervals; it does not capture GPU or presented-frame timings by itself.

## Diagnose and intervene

Use CPU/script/physics and rendering evidence to form a specific hypothesis. Make a bounded change, then repeat the same case. Frame-cap waits can obscure throughput improvements; visual judder can persist despite fast rendering. Record these separately. See [Godot's general optimization guidance](https://docs.godotengine.org/en/stable/tutorials/performance/general_optimization.html).

Choose the relevant bundled guide:

- [Rendering and visibility](assets/rendering.md): lighting, effects, floor/room groups, fog, materials, batching, LOD, viewports and shader warmup.
- [Runtime work and reuse](assets/runtime.md): typed hot paths, cached references, allocations, queries, pools, animation/AI update rates and server APIs.

Prefer eliminating unnecessary work and fixing ownership/update design before adding low-level complexity. Optimize the measured bottleneck; changing mesh triangles will not necessarily improve an expensive fullscreen shader or physics stall.

## Preserve the agreed result

Do not silently reduce output/3D resolution, remove required effects, change gameplay visibility or alter control responsiveness. Apply already-authorized tradeoffs without asking again; otherwise present the concrete tradeoff. A temporary diagnostic quality change must be isolated and restored unless approved for delivery. Report render scale separately from structural optimizations and compare at equal resolution when claiming those gains.

Culling must preserve visible enclosure, next-space continuity, cutscene cameras and required collision/simulation. Pooling must preserve reset and cancellation behavior. Verify the affected interactions and appearance after an optimization.

## Evidence and stopping conditions

Compare representative steady-state and transition cases. Record frame distributions, spikes and relevant counters rather than only average FPS. Report timing limitations, sample length, active caps and cold/warm behavior. Retain raw data and clearly identify regressions or inconclusive results.

When the agreed target passes representative checks, stop broadening the pass unless new evidence requires it. Verify the exported build when delivery includes one. Distinguish measured performance from untested thermal behavior, longer sessions, other hardware and a full playthrough.

The bundled resources are portable and contain no dependency on another game or checkout.
