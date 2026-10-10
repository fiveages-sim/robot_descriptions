# Worked examples

Use these as **measured robots**, not defaults for the next import.

---

## Taku / DVT1 (head after arms)

Package: `humanoid/Dyna/taku_description`. Inferred description — not official Dyna specs.

### State

Full-body Pinocchio order: `[folding(2)+waist(2) | left(7) | right(7) | head(3)]` = 21.
`headInputStart 18`.
Split `task.info`: 14 arm joints, `baseFrame arm_base`.

`manipulatorModelType 0`. Wheels and Dynaclaw jaws in `removeJoints`.

Default schedule: `HM_DUAL_RELATIVE_FIXED_BASE` + `HEAD_GAZE` (structured
`modeSequence[0]` with `bodyMode` / `headMode`).

### Body

Dummy `torso_tracking_frame`: identity on `torso_body_link` (folding/waist
origins already ROS).

Zero-pose FK of that frame in `base_link`: **x ≈ −0.21 m**, z ≈ 0.85 m, pitch ≈ 0.

```
bodyRelative { xLowerBound -0.35  xUpperBound -0.05  muPosition 5.0  muOrientation 5.0 }
```

`bodyTrackingEE` / `headTrackingEE` mu 5.0 / 5.0.
`inputCost` after `scaling 1e-3`: folding 5, waist 3/2, arms 1.5/1.1, head 0.1.

### Gaze

`head_camera_mid_optical_frame` at xyz `0.025 0.01 0.033203` in
`head_camera_base_frame` (mean of L/R optical centers). Camera base itself is
offset `y=0.025` on `head_roll_link`.

```
headMidpointGaze {
  cameraFrame "head_camera_mid_optical_frame"
  muUpright 1.0
  uprightDeadbandDeg 2.0
  ; no muHandsHorizon
}
```

`target_manager.yaml`: `enable_head_control: false`.

### Limits

Arms ±1.57 in both `.info` files only. Head URDF: yaw ±90°, pitch ±20°, roll ±15°.

### Colliders

Default `collider:=simple`. Pairs: torso / `arm_base` ↔ elbow / wrist_yaw / wrist_roll.

---

## Quanta X1 / Artixon 6A (head before arms)

Package: `humanoid/Quanta/quanta_x1_description` (PR control branch). Chassis
wheels locked by default.

### State (Pinocchio 4 name-order siblings)

Measured after `removeJoints` (grippers + locked chassis):

`[lift(1) | head(2) | left(6) | right(6)]` → `headInputStart 1`.

xacro included head after arms; Pinocchio still ordered head before arms because
`head_*` sorts before `left_*` under the same parent. Controllers must follow
the measured list, not the include order.

### Mode

Fixed chassis → structured:

```
modeSequence {
  [0] {
    bodyMode "HM_DUAL_CUSTOM_LOCK_FIXED_BASE"
    headMode "HEAD_GAZE"
  }
}
```

Do **not** default to `HM_DUAL_BODY_FREE` (mobile; gets capability-degraded).
Keep `fsm_default_humanoid_mode` consistent.

### Pitfalls fixed on this robot

- Flat `modeSequence[0] "HM_…"` → `loadHumanoidModeSchedule` init failure.
- Joints listed as lift|L|R|head while Pinocchio was lift|head|L|R → wrong coupling.
- Isaac convex/CoACD collision meshes briefly added then reverted; keep those out
  of the description PR unless asked.
