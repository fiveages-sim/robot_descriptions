# INEX chassis split (reference)

Package: `humanoid/Rokae/rokae_inex_description`

Assembled source nodes (after the user split in Blender):

- Body: `Chassis`, `Chassis.001`, `Chassis.002`
- Steer / wheel: `fl|fr|rl|rr steer`, `fl|fr|rl|rr wheel`
- Rolling accessories joined into `wheel.glb` after the tire AABB origin:

| Corner | Accessory nodes |
|--------|-----------------|
| fl | `Chassis.007`, `Chassis.009` |
| fr | `Chassis.003`, `Chassis.005` |
| rl | `Chassis.015`, `Chassis.017` |
| rr | `Chassis.011`, `Chassis.013` |

CAD local → ROS: `(x, y, z) -> (z, x, y)`.

Measured ROS origins (meters):

| Corner | Steer circle (joint xyz) | Wheel AABB | Notes |
|--------|--------------------------|------------|--------|
| fl | `0.075  0.21725 -0.0395` | `0.075  0.2205 -0.145` | r_circle ≈ 0.0802, r_tire = 0.075, thickness = 0.0575 |
| fr | `0.075 -0.21875 -0.0395` | `0.075 -0.2155 -0.145` | steer `rpy="0 0 π"` |
| rl | `-0.331  0.21725 -0.0395` | `-0.331  0.2205 -0.145` | |
| rr | `-0.331 -0.21875 -0.0395` | `-0.331 -0.2155 -0.145` | steer `rpy="0 0 π"` |

Shared wheel offset in steer frame: `0 0.00325 -0.1055`.

Outputs: `meshes/chassis/{chassis,steer,wheel}.glb`.

Xacro: `xacro/components/chassis.xacro` (`RokaeInexSwerveModule`, `joints_movable`).
OCS2: `config/ocs2/task.info` type 4 + `removeJoints` on the eight wheel joints. `split.info` stays type 0.

## Simple collision (node-xform AABB)

Boxes are **after** glTF node world transforms (what RViz shows). Raw accessor AABB swaps/flips axes.

| Link | Node | `origin xyz` | `box size` |
|------|------|--------------|------------|
| `base_link` | +90° X | `-0.128 0 0` | `0.68 0.64 0.40` |
| `body_link1` calf | 180° X | `0 0.005 0.205` | `0.16 0.20 0.57` |
| `body_link2` thigh | 180° X + t z=0.48 | `0 0.006 0.24` | `0.16 0.24 0.64` |
| `body_link3` waist | 180° X | `0 0.008 0.067` | `0.16 0.15 0.29` |
| `body_link4` chest | 180° Y + t z=0.2156 | `-0.008 0 0.045` | `0.21 0.35 0.34` |
| `head_link1` | 180° Y | — | none (simple) |
| `head_link2` | 180° Y | `-0.010 0 0.023` | `0.14 0.19 0.17` |
| dual `arm_base` | same as chest | `-0.008 0 0.045` | `0.21 0.35 0.34` |

Wheels: cylinder `r=0.075` `L=0.0575`, `rpy="${PI/2} 0 0"`. Arms: `AR5_CCS_V2` cylinders when `collider:=simple` (`link1` has no simple collider).

`selfCollision` (`task.info`): `body_link4` ↔ `left|right_link{3,4,5,7}`.  
`split.info` (dual): same pairs on `arm_base`.

Arm wrapper must pass `collider` / `skin` into `AR5_CCS_V2`. Full `robot.xacro` also reuses `eefs.xacro`, `eef_type_resolver`, `left|right_tcp_offset`.
