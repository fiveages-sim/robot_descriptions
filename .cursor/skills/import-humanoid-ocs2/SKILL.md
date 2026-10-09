---
name: import-humanoid-ocs2
description: >-
  Import a wheeled dual-arm humanoid into this stack: split-body task.info,
  full-body WBC fixed_base_tcp.info, bodyFrame, bodyRelative x band, HEAD_GAZE.
  Use when adding a new robot, 导入机器人, porting W2/Bot2/Taku .info, 竖直模式,
  bodyRelative, bodyFrame, 身体追踪, HEAD_GAZE, muUpright, head roll, or
  jointVelocityLimits.
---

# Import a humanoid into OCS2

Bring a new wheeled dual-arm into `robot-descriptions` + `ocs2_arm_controller` /
`ocs2_wbc_controller`. Copy **layout** from W2 / Bot2 / Taku, never their
**meters, weights, or joint indices** without measuring this robot.

Chassis meshes / `collider:=simple` / `selfCollision`: [split-chassis-glb](../split-chassis-glb/SKILL.md).
Worked numbers: [reference.md](reference.md).

## Progress

```
- [ ] 1. Two .info files + ATM yaml; Pinocchio order and headInputStart
- [ ] 2. bodyFrame = ROS X-forward Z-up dummy, not CAD torso
- [ ] 3. Measure rest-pose bodyFrame local-x; set bodyRelative band around it
- [ ] 4. Gaze camera (stereo midline), muUpright + deadband, head marker off
- [ ] 5. Velocity / effort in .info, not xacro, unless asked
- [ ] 6. Simple colliders before selfCollision
```

## 1. Files and state

| File | Controller | Typical content |
|------|------------|-----------------|
| `config/ocs2/task.info` | `ocs2_arm_controller` (`topology:=dual`) | arms only |
| `config/ocs2/fixed_base_tcp.info` | `ocs2_wbc_controller` | body + arms + head |
| `config/ocs2/target_manager.yaml` | ATM | `enable_head_control: false` |

Full-body state follows Pinocchio DFS on the **planning** URDF (wheels and grippers in `removeJoints`). Count joints, then set `headInputStart` to the first head input (after body + both arms). Wrong index silently couples the wrong joints.

`manipulatorModelType 0` if the WBC does not plan the chassis (usual). Type 4 only if this robot actually unlocks an omni base in MPC.

Default full-body schedule is typically `HM_DUAL_RELATIVE_FIXED_BASE` + `HEAD_GAZE` when both capabilities exist.

## 2. Body tracking frame

`model_information.bodyFrame` is shared by RELATIVE and TRACKING.

Add a dedicated dummy whose axes are **ROS X-forward Y-left Z-up**, coinciding with the torso at identity if the folding/waist chain is already ROS. Do not point `bodyFrame` at a CAD/collision link whose +X is not forward.

If the CAD torso is not ROS, put the rotation on the dummy joint, not in OCS2.

## 3. 竖直模式 = `BODY_RELATIVE`

UI「竖直」→ `BODY_RELATIVE`: penalize base-frame **local x** only outside `[xLowerBound, xUpperBound]`; keep roll/pitch upright. y / z / yaw unconstrained.

**Always FK the rest (HOME / all-zero) pose.** `localX = bodyFrame.x` in `base_link` (fixed-base) or chassis yaw frame (mobile).

- Band must **contain rest x**. Width ~0.25–0.35 m is the usual idea; the **center** is this robot, not Bot2.
- Bot2 `body_link4` is in **front** of `base_link`, so `[0, 0.25]` is a Bot2 number. A folding zigzag often parks the chest **behind** (negative x). Copying `[0, 0.25]` then yanks the torso forward; parallelogram joints also lift it.
- `muPosition` / `muOrientation` on `bodyRelative` and `bodyTrackingEE` need to be large enough to bite (order **5**, not 0.5) relative to `inputCost`. Folding/waist R stiffer than arm R.

## 4. Head gaze

Optical camera frame: **+X right, +Y down, +Z forward**.

Stereo with a lateral mount offset: `cameraFrame` = midpoint of the two optical centers, same orientation as the camera base. A single eye makes roll fight the offset.

| Key | Rule |
|-----|------|
| `muUpright` | 3-DoF head: keep camera +X world-horizontal (`R(2,0)`). Default **on** for a new 3-DoF import. |
| `uprightDeadbandDeg` | Default **2**. Residual `max(0, \|R(2,0)\| - sin(deadband))`. Without it, 1-iter SLQ chatters through roll=0. |
| `muHandsHorizon` | Off unless asked. Equal-height hands at different depths keystone-tilt the image line and roll the head. Mutually exclusive with `muUpright`. |
| `q_roll → 0` | Do not substitute this for gravity upright. |
| Jacobian | Solver already masks gaze to the head window; 3-DoF look-at uses yaw/pitch only, upright uses roll only. 2-DoF heads must not drop the last look-at column. |
| ATM | `enable_head_control: false`. Head follows OCS2. Split-body teleop uses `head_joint_controller`, not a joint marker. |
| Head `inputCost` | ~**0.1**, not `1e-4` (too cheap vs upright → chatter). |

`muUpright` default in the solver is 0 (old tasks stay 3-D). A **new** 3-DoF import should set it explicitly.

## 5. Limits

User says arm speed ±x → `jointVelocityLimits` in **both** `.info` files. Do not edit xacro `<limit velocity>` unless they ask.

Keep folding/waist/head conservative unless this robot has a spec. Do not invent official dynamics.

## 6. Colliders

`collider:=simple` before `selfCollision.activate true`. Never pair against visual GLB meshes. See split-chassis-glb §8.

## Overlay rebuild

`.info` / YAML: restart the controller. Constraint C++ in an overlayed `ocs2_wheel_humanoid`:

```bash
colcon build --packages-select ocs2_wheel_humanoid --allow-overriding ocs2_wheel_humanoid
```
