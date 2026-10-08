# taku_description

Inferred description of the Dyna Taku / DVT1 mobile manipulator, built so it can sit next to the other robots in this repo.

**These limits and inertias are not official Dyna specs.** Kinematics (`xyz` / `rpy` / axis / tree) are taken from the public `dvt1_kin.json` on https://www.dyna.co/dyna-2.1 . Meshes are per-link STLs split from the public damping GLB (`dvt1_body.glb.txt`), except `head_yaw_link` and `head_pitch_link`, which exist only in the coarser body GLB.

- Joint limits: mesh self-collision sweep, then snapped to integer degrees that still contain recorded trajectory ranges. Wheel spin and steering had no resolved stop and are `continuous`.
- Inertias: scaled from public OpenArm v1, Galaxea R1 (`r1_v2_1_0.urdf`), and Agilex Ranger Mini on this branch. Links with no usable analog have no `<inertial>`.
- `effort` / `velocity` on limited joints are copied from the reference robot that supplied the inertia, or set to 0 when no reference exists (head).

See `doc/taku_params.md` for the evidence table. Same text is also at `/workspace/dyna-probe/taku_params.md` in the probe workspace.
