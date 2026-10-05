# Runtime work, allocation and lifetime

## Typed hot paths and cached state

Type changed GDScript state, parameters, returns and collections where the installed version supports it. Inference can be static; dynamic JSON/dictionary input still needs boundary validation. Types enable optimized operations, but they cannot repair a GPU bottleneck. [Static typing](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/static_typing.html).

Cache stable references and query objects during initialization or binding. Rebind when scenes/owners change. Avoid recurring get_node/tree searches, resource loads, duplicate ray updates and string formatting in hot callbacks. React to events for UI, resize, settings and visibility changes; avoid writing unchanged server properties.

Measure recurring allocations such as arrays, dictionaries, strings, scene/resource construction and repeated duplication. Reuse buffers and query parameter objects when it preserves ownership and correctness. Vector2/Vector3 are value types: constructing one is not equivalent to allocating a scene or a reference-counted container. Do not replace readable vector math with convoluted state mutation without evidence.

Use appropriate built-in math, geometry and packed-array operations for bulk work; packed buffers are useful for homogeneous numeric data. Avoid converting to/from packed forms on every iteration. Keep transient allocation outside the measured loop where feasible.

## Frequency and inactivity

Decouple AI planning, perception, animation posing, UI redraw and physical movement. Choose update frequency based on responsiveness and measured cost; preserve collisions and input timing. For low-rate visual animation, accumulate time but apply transforms only on a new pose tick. Offscreen behavior can still matter to gameplay.

A hidden subtree or viewport may retain active scripts, animation, sound or physics. Disable each unnecessary subsystem deliberately and restore it on activation. Prefer bounding the active workload to traversing all distant objects each frame.

## Pools and servers

Pool repeated expensive instances when spawn/free churn matters. Define acquisition, reset, release, capacity and exhaustion behavior; stop stale tweens, awaits, signals, audio and queries before reuse. Pooling trades memory for reuse and is unnecessary for many one-off objects.

Consider MultiMesh or RenderingServer/PhysicsServer for proven high-count workloads where scene-tree overhead dominates. Godot's servers are local engine APIs, not network server-side execution. Respect RID ownership, lifetime and thread-safety boundaries. Avoid manipulating a node's internally owned resources inconsistently with the node. [Server optimization](https://docs.godotengine.org/en/stable/tutorials/performance/using_servers.html).

Test repeated activation/deactivation and checkpoint reuse. Check node/resource counts and memory trends across equivalent cycles, distinguishing allocator caching from unbounded growth. Validate hit detection, navigation, control and camera ownership after changing update or lifetime policy.
