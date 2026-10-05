# Traversable 3D construction

## Establish space before decoration

Draw the adjacency and elevation of the changed area: entry, exit, doors, corridors, stairs, optional spaces and boundaries. Use consistent units. Size passages for the actual player collider and door sweep, not merely a plausible screenshot. Build and walk the connection before repeating modules.

For enclosed architecture, model the enclosure deliberately: floor, ceiling, outer walls, openings and end boundaries. Outdoor routes may use intentionally open boundaries, but reachable areas still need an explicit traversal policy. Support physical signs, lights and props on real geometry.

## Make joins unambiguous

Assign ownership to each visible face. Shared slabs can have an upper face belonging to one room and a downward ceiling face belonging to the room below. Keep collision ownership separate from visual ownership. When grouping floors/rooms, include their enclosure and sightlines before the camera enters.

Use a consistent join policy: shared meshes or clean butt joints where possible; deliberate offsets only for genuinely layered surfaces. Inspect frame headers, both sides of doors, sills, floor thresholds and landings. Find duplicate/coplanar faces before changing depth precision or hiding the symptom with an arbitrary offset. Audit normals, winding and material assignment as well.

For procedural geometry, calculate exposed faces against the complete relevant structure before dividing render batches. Grouping must not resurrect hidden internal faces. Visual meshes can be simplified or batched while colliders retain the authored traversal shape.

## Doors and stairs

A door leaf rotates around a hinge parent or hinge-aligned origin. Specify its closed transform and bounded open angle; repeated interactions should not accumulate rotations. Keep frame/collider clearance and interaction reach valid in both states. Handle interruption and close/reopen transitions explicitly.

Test stairs ascending, descending, entering the first tread and leaving the top landing with the actual controller. Check head clearance, side rails, landing room and collision masks. If an invisible ramp is an intentional controller design, align and validate it; do not add one blindly to conceal broken treads or guards. Disable removed visual guards' colliders too.

## Focused verification

Walk the changed route, reverse it, approach joins diagonally and interact from intended positions. Check floor boundaries while the neighboring render group is inactive. For moving geometry, observe the whole transition and restored control. Include the nearest optional exploration area if the change affects its access.

Useful upstream details: [3D rendering limitations](https://docs.godotengine.org/en/stable/tutorials/3d/3d_rendering_limitations.html). Verify version-specific settings rather than treating a depth or transparency workaround as a geometry repair.
