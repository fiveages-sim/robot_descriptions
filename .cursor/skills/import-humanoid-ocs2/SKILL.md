---
name: import-humanoid-ocs2
description: >-
  Import a wheeled dual-arm humanoid into this stack: ros2_control, split-body
  task.info, full-body WBC fixed_base_tcp.info, Pinocchio joint order,
  modeSequence bodyMode/headMode, bodyFrame, bodyRelative x band, HEAD_GAZE.
  Use when adding a new robot, 导入机器人, 补运控, porting W2/Bot2/Taku/Quanta
  .info, 竖直模式, bodyRelative, bodyFrame, 身体追踪, HEAD_GAZE, muUpright,
  head roll, jointVelocityLimits, headInputStart, modeSequence, or
  HM_DUAL_* / fixed-base WBC.
---

# Import a humanoid into OCS2

Bring a new wheeled dual-arm into `robot-descriptions` + `ocs2_arm_controller` /
`ocs2_wbc_controller`. Copy **layout** from W2 / Bot2 / Taku / Quanta X1, never
their **meters, weights, or joint indices** without measuring this robot.

Prior stage (plain URDF → xacro package): [urdf-to-xacro-package](../urdf-to-xacro-package/SKILL.md).
Chassis meshes / `collider:=simple` / `selfCollision`: [split-chassis-glb](../split-chassis-glb/SKILL.md).
Worked numbers: [reference.md](reference.md).

## Work where the user can relaunch

- Prefer edit + symlink-install on the **local ROS machine** so the user can
  relaunch immediately. Push the feature branch after it works locally.
- Do **not** put `ROS_DOMAIN_ID` into package READMEs. Domain isolation is a
  local shell `export` only.
- Keep Isaac Sim convex-hull / CoACD decompose meshes **out** of the description
  PR unless the user asked for that package; hand those to the Isaac Sim side.
- New robot work gets its own branch from `main`. Never force-push. Do not mix
  unrelated dirty trees into the skills or control commit.

## Progress

```
- [ ] 0. Peer scope; chassis lock default; grippers; delete stale static urdf/
- [ ] 1. Two .info files + ATM yaml; measure Pinocchio order + headInputStart
- [ ] 2. Structured modeSequence {bodyMode, headMode}; fixed-base if wheels locked
- [ ] 3. bodyFrame = ROS X-forward Z-up dummy, not CAD torso
- [ ] 4. Measure rest-pose bodyFrame local-x; set bodyRelative band around it
- [ ] 5. Gaze camera (stereo midline), muUpright + deadband, head marker off
- [ ] 6. Velocity / effort in .info, not xacro, unless asked
- [ ] 7. Simple colliders before selfCollision
- [ ] 8. Local launch: WBC init + single-joint order check; then push
```

## 0. Peers and deliverables

Choose 1–2 closest peers by topology (lift + dual arm + head, fixed vs movable
chassis, gripper style). Typical deliverables:

- Chassis joints locked by default (`chassis_joints_movable:=false` / fixed
  wheel and caster joints), same as wheeled-arm peers. List chassis joints in
  OCS2 `removeJoints` for movable-URDF fallback.
- `config/ros2_control/ros2_controllers.yaml` and matching xacro hardware
  interfaces (mock / gz / isaac as peers do).
- Grippers: follow the peer style the user names (e.g. ARX Ark
  `*_gripper_joint` + `adaptive_gripper_controller`).
- OCS2: `config/ocs2/task.info` for split-body; `fixed_base_tcp.info` (+
  `target_manager.yaml`) for `ocs2_wbc_controller` full_body.
- Delete stale static `urdf/` trees if peers generate from xacro only.

## 1. Files and Pinocchio state order

| File | Controller | Typical content |
|------|------------|-----------------|
| `config/ocs2/task.info` | `ocs2_arm_controller` (`topology:=dual`) | arms only |
| `config/ocs2/fixed_base_tcp.info` | `ocs2_wbc_controller` | body + arms + head |
| `config/ocs2/target_manager.yaml` | ATM | `enable_head_control: false` |

**Pinocchio joint order is the source of truth** — not xacro include order and
not URDF declaration order. Full-body state is Pinocchio DFS on the **planning**
URDF after `removeJoints` (wheels, grippers, mimics, locked chassis).

On **Pinocchio 4**, siblings under the same parent (e.g. `head_*` and `left_*`
under `lift_link`) may be visited in **name order**. Putting head after arms in
`robot.xacro` does **not** guarantee head-last in the model.

Always measure:

1. `buildModelFromUrdf` on the planning URDF.
2. Drop joints listed in `removeJoints`.
3. List remaining joint names in model order.

Then align **exactly**: `ocs2_wbc_controller.joints`, `home_*`, `initialState`,
`jointVelocityLimits`. Set `headInputStart` to the input index where head DOFs
begin. The WBC supports both layouts:

| Layout | When | `headInputStart` |
|--------|------|------------------|
| Head after arms | Pinocchio ends with head (Taku) | `>= waistEnd + leftDof + rightDof` |
| Head before arms | Name-order siblings put head first (Quanta: lift\|head\|L\|R) | Right after waist (often `1` for a single lift) |

Wrong index silently couples the wrong joints. Update comments to the **measured**
order; do not claim include-after-arms fixes DFS.

`manipulatorModelType 0` if the WBC does not plan the chassis (usual). Type 4
only if this robot actually unlocks an omni base in MPC.

## 2. Humanoid mode schedule

Modern `loadHumanoidModeSchedule` requires **structured** entries. A flat string
under `[0]` fails with
`must be a structured entry with bodyMode and headMode`:

```
modeSequence
{
    [0]
    {
        bodyMode "…"
        headMode "…"
    }
}
```

Match the chassis policy:

| Chassis | Prefer | Avoid as default |
|---------|--------|------------------|
| Fixed (wheels locked in xacro) | `HM_DUAL_CUSTOM_LOCK_FIXED_BASE`, `HM_DUAL_IDLE`, or `HM_DUAL_RELATIVE_FIXED_BASE` | `HM_DUAL_BODY_FREE` (mobile; capability-degraded → base locked, head DISABLED) |
| Mobile base planned in MPC | Mobile presets such as `HM_DUAL_BODY_FREE` when capabilities exist | Fixed-base-only presets |

If using `HM_DUAL_CUSTOM_LOCK_FIXED_BASE`, activate `customJointLock` the way the
peer does (empty lock indices leave the lift free). Keep
`fsm_default_humanoid_mode` in `ros2_controllers.yaml` consistent with
`initialModeSchedule`. Align `model_information` frames (`baseFrame`, `eeFrame`,
`eeFrame1`, `bodyFrame`, `headFrame`) with real link names.

When both RELATIVE and gaze exist on a fixed base, a common default is
`HM_DUAL_RELATIVE_FIXED_BASE` + `HEAD_GAZE` (Taku). Quanta-style fixed chassis
often uses `HM_DUAL_CUSTOM_LOCK_FIXED_BASE` + `HEAD_GAZE`.

## 3. Body tracking frame

`model_information.bodyFrame` is shared by RELATIVE and TRACKING.

Add a dedicated dummy whose axes are **ROS X-forward Y-left Z-up**, coinciding
with the torso at identity if the folding/waist chain is already ROS. Do not
point `bodyFrame` at a CAD/collision link whose +X is not forward.

If the CAD torso is not ROS, put the rotation on the dummy joint, not in OCS2.

## 4. 竖直模式 = `BODY_RELATIVE`

UI「竖直」→ `BODY_RELATIVE`: penalize base-frame **local x** only outside
`[xLowerBound, xUpperBound]`; keep roll/pitch upright. y / z / yaw unconstrained.

**Always FK the rest (HOME / all-zero) pose.** `localX = bodyFrame.x` in
`base_link` (fixed-base) or chassis yaw frame (mobile).

- Band must **contain rest x**. Width ~0.25–0.35 m is the usual idea; the
  **center** is this robot, not Bot2.
- Bot2 `body_link4` is in **front** of `base_link`, so `[0, 0.25]` is a Bot2
  number. A folding zigzag often parks the chest **behind** (negative x).
  Copying `[0, 0.25]` then yanks the torso forward; parallelogram joints also
  lift it.
- `muPosition` / `muOrientation` on `bodyRelative` and `bodyTrackingEE` need to
  be large enough to bite (order **5**, not 0.5) relative to `inputCost`.
  Folding/waist R stiffer than arm R.

## 5. Head gaze

Optical camera frame: **+X right, +Y down, +Z forward**.

Stereo with a lateral mount offset: `cameraFrame` = midpoint of the two optical
centers, same orientation as the camera base. A single eye makes roll fight the
offset.

| Key | Rule |
|-----|------|
| `muUpright` | 3-DoF head: keep camera +X world-horizontal (`R(2,0)`). Default **on** for a new 3-DoF import. |
| `uprightDeadbandDeg` | Default **2**. Residual `max(0, \|R(2,0)\| - sin(deadband))`. Without it, 1-iter SLQ chatters through roll=0. |
| `muHandsHorizon` | Off unless asked. Equal-height hands at different depths keystone-tilt the image line and roll the head. Mutually exclusive with `muUpright`. |
| `q_roll → 0` | Do not substitute this for gravity upright. |
| Jacobian | Solver already masks gaze to the head window; 3-DoF look-at uses yaw/pitch only, upright uses roll only. 2-DoF heads must not drop the last look-at column. |
| ATM | `enable_head_control: false`. Head follows OCS2. Split-body teleop uses `head_joint_controller`, not a joint marker. |
| Head `inputCost` | ~**0.1**, not `1e-4` (too cheap vs upright → chatter). |

`muUpright` default in the solver is 0 (old tasks stay 3-D). A **new** 3-DoF
import should set it explicitly.

## 6. Limits

User says arm speed ±x → `jointVelocityLimits` in **both** `.info` files. Do
not edit xacro `<limit velocity>` unless they ask.

Keep folding/waist/head conservative unless this robot has a spec. Do not invent
official dynamics.

## 7. Colliders

`collider:=simple` before `selfCollision.activate true`. Never pair against
visual GLB meshes. See split-chassis-glb §8.

Isaac convex hull / CoACD: out of this description PR unless asked.

## 8. Validate locally, then push

```bash
colcon build --packages-select <pkg> --symlink-install
# relaunch peer full_body / split_body launch
```

Confirm:

- `ocs2_wbc_controller` initializes (no modeSequence / joints-vs-armDim errors).
- Moving a single joint in mock matches the expected link (order check).
- No spurious `HM_* requires unsupported capabilities` warn for the chosen default mode.

Then commit and push the feature branch / PR. Never force-push.

## Overlay rebuild

`.info` / YAML: restart the controller (symlink-install). Constraint C++ in an
overlayed `ocs2_wheel_humanoid`:

```bash
colcon build --packages-select ocs2_wheel_humanoid --allow-overriding ocs2_wheel_humanoid
```

## Report

Measured Pinocchio joint order, `headInputStart`, chosen body/head mode, peers
copied, commit hash / PR URL, and what the user should relaunch.
