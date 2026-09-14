---
name: split-chassis-glb
description: Split an assembled chassis GLB into chassis/steer/wheel meshes with joint-ready origins, write swerve xacro, and add simple collision boxes from glTF-node AABBs. Use when splitting 底盘 GLB, steer/wheel, 舵轮, swerve chassis, INEX chassis, 简化碰撞, collider:=simple, selfCollision, or GLB 90° / Y-up AABB mismatch.
---

# Split chassis GLB for swerve xacro

Canonical example: [rokae_inex_description](../../../humanoid/Rokae/rokae_inex_description/).

## Why

URDF/xacro cannot reference a named node inside one GLB. One assembled chassis file must become:

| File | Content | Link-frame origin |
|------|---------|-------------------|
| `chassis.glb` | Body only (no steer/wheel/rolling hardware) | `base_link` (ROS) |
| `steer.glb` | One shared steer housing | Largest **horizontal** circle (steer axis = Z) |
| `wheel.glb` | Tire + parts that **roll with the wheel** | Tire AABB center only |

Reuse one `steer.glb` + one `wheel.glb` at four corners (`fl` `fr` `rl` `rr`).

## Workflow

```
Task Progress:
- [ ] 1. Confirm named objects in the assembled GLB
- [ ] 2. Convert vertices to ROS Z-up before measuring
- [ ] 3. Classify every leftover part
- [ ] 4. Measure steer circles and wheel AABB centers
- [ ] 5. Recenter, join wheel accessories, export 3 GLBs
- [ ] 6. Write xacro (right modules yaw 180, no mesh reflect)
- [ ] 7. Verify TF / xacro / no double visuals
- [ ] 8. Simple collision + OCS2 selfCollision (node-xform AABB, not raw accessors)
```

### 1. Named objects

The assembled GLB should already have per-corner objects, e.g. `fl steer`, `fl wheel`, `fr steer`, …. Remaining `Chassis*` pieces are either body or accessories.

Do not export a still-in-world-frame instance as the shared mesh — four wheels would stack at the origin.

### 2. ROS frame first

Measure and export in **ROS**: X forward, Y left, Z up.

Do not trust the glTF node quaternion. INEX CAD local was X=left, Y=up, Z=forward; convert each vertex with `(x, y, z) -> (z, x, y)`, then set the object transform to identity.

Export from Blender Z-up (`export_yup=True`) so RViz/Assimp matches other description GLBs. That write usually leaves a **glTF node rotation** (INEX chassis = +90° about X). RViz applies it; raw POSITION accessor AABB does **not**.

Keep the existing `base_link` origin (do not shift to ground) if lidars/body are already authored in that frame.

### 3. Classify parts

| Goes into | Rule |
|-----------|------|
| `wheel.glb` | Rolls with the tire (hub cap, washer, bolts on the hub) |
| `steer.glb` | Yaws with steering, does not roll |
| `chassis.glb` | Fixed to the body |

**Wheel origin order is mandatory:** compute the tire AABB center on the **pure wheel** mesh, then Join nearby rolling parts (Blender: wheel Active). Joining first pulls the origin off the axle.

Collision cylinder uses **tire** radius/thickness only, not accessory protrusions.

### 4. Measure origins

**Steer:** slice the ROS mesh on Z (≈2 mm), fit a circle in XY, keep the largest radius with low residual (`rms/r < 0.08`, `r > 1 cm`). Joint origin = that circle center `(cx, cy, z_slice)`. Axis is Z.

**Wheel:** AABB center of the tire only (more stable than vertex mean; hubs bias the centroid). Axis is Y. Typical tire is a disk in XZ, thin in Y.

**Wheel joint** in steer frame:

```
wheel_offset = wheel_aabb_center - steer_circle_center
```

INEX used the same offset on all four corners: `xyz="0 0.00325 -0.1055"`.

### 5. Export

From one template corner (usually `fl`):

1. Copy `fl steer`, subtract steer-circle origin, export `steer.glb`.
2. Copy `fl wheel`, subtract tire AABB origin, Join rolling parts, export `wheel.glb`.
3. Join leftover body pieces at identity, export `chassis.glb`.

Overwrite the assembled file only after the three outputs exist. Keep an unused CAD STL if present.

### 6. Xacro

Chain:

```
base_footprint --fixed--> base_link
  --steer_*_joint (revolute Z)--> *_steer
    --wheel_*_joint (continuous Y)--> *_wheel
```

Rules:

- One module macro; instantiate `fl` `fr` `rl` `rr`.
- **Right side (`fr`/`rr`): `rpy="0 0 ${PI}"` on `steer_*_joint`.** Same hardware, yaw 180°. Do **not** `scale="1 -1 1"` (reflect).
- Default `joints_movable:=false` (fixed) on the full robot. `type:=chassis` visualization sets it `true`.
- Wheel collision: `cylinder` with `rpy="${PI/2} 0 0"` so the default Z cylinder aligns with Y.
- Lumped chassis inertia can stay on `base_link`; steer/wheel placeholder masses are fine if OCS2 `removeJoints` the 8 wheel joints.
- Do not add steer/wheel to ros2_control unless the user asks.

OCS2 (if this robot plans a holonomic base): `manipulatorModelType 4`, `removeJoints` the eight `*_steer_joint` / `*_wheel_joint` names, add `omniWheelBasedMobileManipulator` base initial state / `inputCost.R.base` / velocity limits. Hardware `joints` list and `total_dof` stay the arm/waist/head count.

### 7. Verify

- `xacro` + `check_urdf`: 8 named joints; right steers have `rpy="0 0 π"`; no mesh `scale`.
- `robot_state_publisher` TF: `*_steer` at circle centers; `*_wheel` = steer ⊕ offset (right yaw 180 flips the local +Y offset in world).
- RViz `type:=chassis`: no double visuals, steer yaws about the circle, wheel rolls about the tire center.
- If OCS2 type 4: Pinocchio `nq = 3 + armDim` after `removeJoints`.

### 8. Simple collision (required before selfCollision)

Do **not** enable `selfCollision` while visual GLB is the collision mesh. High-poly hpp-fcl is slow and numerically noisy.

Pattern (WCE3 / INEX): `collider` arg default `simple`; each link:

```xml
<xacro:if value="${collider == 'simple'}">  <!-- box / cylinder --> </xacro:if>
<xacro:if value="${collider == 'convex'}">  <!-- same GLB as visual --> </xacro:if>
```

**Box size/origin = AABB after glTF node world transforms**, not accessor `min`/`max`.

1. Load POSITION only (skip NORMAL / other VEC3).
2. Apply each node's `translation` / `rotation` / `scale` (or `matrix`).
3. AABB → `size = max-min`, `xyz = (max+min)/2`.
4. Typical INEX nodes after `export_yup`: chassis **+90° X**; calf/thigh/waist **180° X**; chest/head **180° Y**. Sign of the long axis often flips vs raw accessors (calf `z=-0.205` → `+0.205`).

Wheels stay **cylinders** (`rpy="${PI/2} 0 0"`), independent of `collider`. Head yaw (`head_link1`) has no simple collision (WCE3).

If the robot wraps `AR5_CCS_V2`, pass `collider` and `skin` through. Default `collider:=convex` in that macro means a missing arg silently uses mesh collision. Reuse `eefs.xacro` + `eef_type_resolver` + `*_tcp_offset` on the full `robot.xacro`; do not invent a second `left_eef`.

OCS2 pairs use the **simple** torso link vs arm cylinders:

- Full body: `body_link4` (or `torso_base`) ↔ `left|right_link{3,4,5,7}`
- `topology:=dual`: same pairs on `arm_base` (copy the chest box onto `arm_base`; that tree has no `body_link4`)

INEX numbers: [reference.md](reference.md).

## INEX reference numbers

See [reference.md](reference.md).
