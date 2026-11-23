# DACH TRON2B validation

## Source and model differences

LimX Dynamics TRON2 robot description, revision
`d81d2a83a3c718bc68deca4e8804fdc984dc34f7`, directory
`tron2b/DACH_TRON2B/urdf`. The structural comparison uses
`robot_grasper.urdf`. The TCP offset comes from
`robot_zeromass_graser.urdf`, where it is defined relative to each flange.
The package applies that offset relative to the corresponding gripper base.

| Scope | Cases | Links / joints per case | Result |
|---|---:|---:|---|
| Full robot, GLB and STL visuals | 2 | 48 / 47 | Pass |
| Body, both side arguments and visual formats | 4 | 6 / 5 | Pass |
| Head, both side arguments and visual formats | 4 | 6 / 5 | Pass |
| Arm, both sides and visual formats | 4 | 8 / 7 | Pass |
| Gripper, both sides and visual formats | 4 | 12 / 11 | Pass |
| ROS control, four hardware plugins and both visual formats | 8 | 48 / 47 | Pass |

All 26 expanded cases passed `check_urdf` and every mesh reference resolved.
The four hardware cases check URDF generation and plugin selection.
Runtime checks covered mock and Isaac TopicBasedSystem.

The factory URDF has 45 links and 44 joints. All factory joints are present.
Joint type, parent/child, origin, axis, limits, mimic and dynamics match
within numeric tolerances (absolute 1e-8, relative 1e-6).
All 45 shared links match for inertial data. Intentional differences:

| Change | Scope |
|---|---|
| Base mounting frame | Added fixed `dach_base_mount` and ROS `base_link` above factory `base_Link` |
| TCP frames | Added fixed `L_ee_Joint` and `R_ee_Joint` with the matching TCP links and factory offset |
| Visual elements | 37 shared links differ in mesh references, materials or transforms for component reuse |
| Collision elements | 25 shared links differ in mesh references or simplified geometry |

Of 22 STL files, 19 are referenced by at least one expanded variant. The
three unreferenced files were retained for review:
`proximal_yaw_collision.stl`, `wrist_roll_collision.stl`, and `fixed.stl`.
All 19 GLB files are referenced. All 12 configured OCS2 collision pairs
resolve to links with box or cylinder geometry. Dynamic per-pair coverage
is outside this validation.

## HOME and grasp regression

| Test | Result |
|---|---|
| Mock, standalone HOME from closed | Left and right reached 0.7730 rad |
| Isaac, standalone HOME from 0 rad | Both reached within 0.0005 rad of the target |
| Isaac, right-side bottle grasp | Bottle lifted 123.9 mm and passed the 35 mm / 1 s criterion |

The package demo launches one ROS node for HOME in both backends. Gripper
positions come from `home_grippers` in the same configuration file as
the arm HOME positions. Isaac implements physics and does not publish a
second set of HOME commands.

## Contact inspection

Two world-space mesh snapshots were taken in the right-arm bottle scene,
after closure and after the successful lift. Both clamp-finger visual
meshes were compared with the closed bottle triangle mesh. The table
lists the closest sampled surface points on each finger. Both samples
had zero tested points inside the bottle by more than 0.1 mm.

| Phase | Left finger clearance | Right finger clearance |
|---|---:|---:|
| After closure | 1.31 mm | 1.39 mm |
| After lift | 1.23 mm | 1.36 mm |

The displayed jaw vertices match the PhysX collision-source vertices to
within 0.001 mm in this run. The top and side views are projections of
the saved meshes and source convex hulls. They do not show the exact
cooked PhysX hull. Mesh distance uses vertices and triangle centroids
in 3D. The result applies to the two sampled poses and does not provide
continuous collision coverage throughout the motion.
