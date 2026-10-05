# State, time and ownership

## Scenes and shared resources

Keep a clear owner for each state change and use explicit inputs/outputs across scene boundaries. Prefer reusable self-contained scenes where practical; dependencies should be bound deliberately. Imported resources can be shared across instances. Duplicate a material/animation only when it needs per-instance edits, and retain shared resources where variation is unnecessary. See [scene organization](https://docs.godotengine.org/en/stable/tutorials/best_practices/scene_organization.html).

## Authored sequences

For every sequence, define entry conditions, current phase, temporary ownership and cleanup. Typical temporary state includes player control, active camera, mouse capture, collision, audio, subtitle/skip handling, animation, screen overlays and active tweens.

Finish and cancellation must both restore a coherent state. Use a sequence generation/token or comparable mechanism so continuations after await cannot change a newly loaded checkpoint. Check validity after waits. Pause semantics must match the timers, tweens, animation and dialogue used by the sequence. Avoid waiting for an event whose emitter has been disabled or freed.

A checkpoint reconstructs a stable state from validated data, including its schema version. Save semantic progression and necessary transforms; avoid depending on live node identity. Test loading during a transition as well as after completion. Reapplying a stable checkpoint should not duplicate effects, actors or signal subscriptions.

## Camera and animation timing

Separate physical transforms, visual animation and camera feedback. If the controller drives motion, remove the walk clip's horizontal drift through import configuration, an in-place clip or a deliberate root-motion implementation; verify several animation loops against the collision body. Bone local axes may differ from actor/world axes.

Use one deliberate interpolation scheme. Avoid layering manual interpolation over inherited automatic interpolation. Inspect moving parents and global/local coordinates. Keep mouse look responsive, and reset interpolation history after teleports and camera/control transfers. Test at the supported frame limits and with uneven frame delivery. [Godot camera interpolation](https://docs.godotengine.org/en/stable/tutorials/physics/interpolation/advanced_physics_interpolation.html).

## Reuse and inactivity

Hidden objects may still process, simulate, animate, emit audio or render a SubViewport. Set these lifecycles explicitly. A pooled instance needs a reset contract covering transforms, velocity, targets, timers, signals, materials, audio and animation state. Bound the pool; retained instances consume memory.

Test the transitions actually changed: enter, finish, skip, pause/resume, cancel/reload and reuse. Do not automatically replay an entire game for a local fix.
