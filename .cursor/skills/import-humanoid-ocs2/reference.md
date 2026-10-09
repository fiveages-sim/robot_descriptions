# Worked example: Taku / DVT1

Package: `humanoid/Dyna/taku_description`. Inferred description — not official Dyna specs.

Use these as **one measured robot**, not defaults for the next import.

## State

Full-body Pinocchio order: `[folding(2)+waist(2) | left(7) | right(7) | head(3)]` = 21. `headInputStart 18`.
Split `task.info`: 14 arm joints, `baseFrame arm_base`.

`manipulatorModelType 0`. Wheels and Dynaclaw jaws in `removeJoints`.

## Body

Dummy `torso_tracking_frame`: identity on `torso_body_link` (folding/waist origins already ROS).

Zero-pose FK of that frame in `base_link`: **x ≈ −0.21 m**, z ≈ 0.85 m, pitch ≈ 0.

```
bodyRelative { xLowerBound -0.35  xUpperBound -0.05  muPosition 5.0  muOrientation 5.0 }
```

`bodyTrackingEE` / `headTrackingEE` mu 5.0 / 5.0.
`inputCost` after `scaling 1e-3`: folding 5, waist 3/2, arms 1.5/1.1, head 0.1.

## Gaze

`head_camera_mid_optical_frame` at xyz `0.025 0.01 0.033203` in `head_camera_base_frame` (mean of L/R optical centers). Camera base itself is offset `y=0.025` on `head_roll_link`.

```
headMidpointGaze {
  cameraFrame "head_camera_mid_optical_frame"
  muUpright 1.0
  uprightDeadbandDeg 2.0
  ; no muHandsHorizon
}
```

`target_manager.yaml`: `enable_head_control: false`.

## Limits

Arms ±1.57 in both `.info` files only. Head URDF: yaw ±90°, pitch ±20°, roll ±15°.

## Colliders

Default `collider:=simple`. Pairs: torso / `arm_base` ↔ elbow / wrist_yaw / wrist_roll.
