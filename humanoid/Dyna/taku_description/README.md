# Taku Description

This package contains an **inferred** description of the Dyna Taku / DVT1 wheeled dual-arm robot (4-module swerve chassis, folding lift + waist, 3-DoF head, dual 7-DoF arms, Dynaclaw two-jaw grippers).

> **Not official Dyna specs.** Kinematics (tree / `xyz` / `rpy` / axes) come from the public `dvt1_kin.json` on https://www.dyna.co/dyna-2.1 . Joint limits come from a mesh self-collision sweep snapped to integer degrees that still contain the recorded trajectory ranges. Inertias are scaled from OpenArm v1, Galaxea R1 and Agilex Ranger Mini. Links without a usable reference (waist, torso, head, gripper jaws) have no `<inertial>`. Evidence and sources are in [`doc/taku_params.md`](doc/taku_params.md).

Meshes are per-link GLBs under `meshes/{chassis,body,head,arm,dynaclaw}/`. Both arms share one mesh set with no left/right `scale` (M6 CCS style); shoulder roll/yaw `+90°` is baked into the same joint origins, and the right arm is mirrored only at the shoulder mount. The four swerve modules share `chassis/wheel_steering.glb` and `chassis/wheel_rotate.glb`. Dynaclaw keeps one jaw mesh; the rear jaw is that mesh rotated 180° about z. The front lidars use RoboSense Airy and the rear lidar uses Livox MID-360 meshes from [`sensor_models`](../../../common/sensor_models).

## 1. Build

```bash
cd ~/ros2_ws && colcon build --packages-up-to taku_description --symlink-install
source install/setup.bash
```

## 2. Visualize the robot

### 2.1. Full robot

```bash
ros2 launch robot_common_launch humanoid.launch.py robot:=taku
```

The 8 steering and drive joints are fixed by default (`enable_wheel_joints:=false`), as in the other wheeled robots in this repo.

### 2.2. Component modules

Use `ros2 launch robot_common_launch component.launch.py robot:=taku type:=<type>` with one of these types:

| `type`       | Content                                                                 |
|--------------|-------------------------------------------------------------------------|
| `chassis`    | swerve chassis with steering and drive joints enabled, lidars, IMU frame |
| `body`       | folding lift (`folding_low/high_joint`) + waist pitch / yaw              |
| `upper_body` | body + head + dual arms, no chassis and no Dynaclaw                      |
| `head`       | head yaw / pitch / roll + stereo camera frames                           |
| `arm` / `arms` | both arms with Dynaclaw, mounted on a torso stub                       |
| `left_arm` / `right_arm` | one arm, Ai2-style standalone (unprefixed root)               |
| `gripper` / `dynaclaw` | one Dynaclaw (`side:=left` or `side:=right`)                    |

Standalone Dynaclaw only:

```bash
xacro $(ros2 pkg prefix taku_description)/share/taku_description/xacro/dynaclaw.xacro
```

Hide the sensor_models lidar meshes for an Isaac asset import with `xacro_isaac:=true`.

## 3. Control

Default `hardware:=mock_components`. Layout follows W2 / Bot2: no chassis or per-arm basic controllers. Homes are the URDF zero pose. Head limits: yaw ±90°, pitch ±20°, roll ±15°.

### 3.1. Split body

Arms under `ocs2_arm_controller` (`config/ocs2/task.info`, 14 DoF); planning URDF uses `topology:=dual` rooted at `arm_base`. Folding lift / waist and head stay on `basic_joint_controller`. Dynaclaw uses `adaptive_gripper_controller`.

```bash
ros2 launch ocs2_arm_controller split_body.launch.py robot:=taku
ros2 launch ocs2_arm_controller split_body.launch.py robot:=taku hardware:=isaac
```

| Controller | Role |
|------------|------|
| `ocs2_arm_controller` | dual-arm MPC (14 DoF), `info_file_name: task` |
| `body_joint_controller` | `folding_low/high` + `waist_pitch/yaw` |
| `head_joint_controller` | `head_yaw/pitch/roll` |
| `left/right_gripper_controller` | Dynaclaw (`*_gripper_joint`; mimic jaw in URDF) |

### 3.2. Full body

Whole-body MPC via `ocs2_wbc_controller` (`config/ocs2/fixed_base_tcp.info`, 21 DoF: body 4 + left 7 + right 7 + head 3). Default `headMode` is `HEAD_GAZE`. Grippers same as split body.

```bash
ros2 launch ocs2_arm_controller full_body.launch.py robot:=taku
ros2 launch ocs2_arm_controller full_body.launch.py robot:=taku hardware:=isaac
```

| Controller | Role |
|------------|------|
| `ocs2_wbc_controller` | WBC MPC including head, `info_file_name: fixed_base_tcp` |
| `left/right_gripper_controller` | Dynaclaw |

Wheel joints are not in either control stack (skill: do not add steer/wheel to ros2_control unless asked). Enable only in the chassis component / with `enable_wheel_joints:=true` for viz.

Default `collider:=simple`: folding PCA-OBB cylinders (trimmed ends), waist AABB box, torso/`arm_base` tight Z-cylinder (`r=0.100`, `L=0.300`), arm cylinders (wrist_roll split into housing + palm), Dynaclaw jaw boxes. `selfCollision` is on for torso/arm_base ↔ elbow / wrist_yaw / wrist_roll. Use `collider:=convex` only for mesh viz — do not enable selfCollision with GLB collision.

## 4. Files

* `xacro/robot.xacro`: full robot + `topology:=dual` planning tree
* `xacro/component.xacro`: component modules selected by `type`
* `xacro/dynaclaw.xacro`: Astribot-style standalone Dynaclaw entry
* `xacro/components/`: `chassis.xacro`, `body.xacro`, `head.xacro`, `arm.xacro` (`TakuArm`), `dynaclaw.xacro` (`TakuDynaclaw`), `gripper.xacro`
* `xacro/ros2_control/`: `robot.xacro` (mock / gz / isaac hardware), `interfaces.xacro`
* `meshes/`: `chassis/`, `body/`, `head/`, `arm/`, `dynaclaw/`
* `config/ros2_control/ros2_controllers.yaml`: W2-style `ocs2_arm_controller` / `ocs2_wbc_controller`, plus body / head / Dynaclaw grippers
* `config/ocs2/`: `task.info` (split dual-arm), `fixed_base_tcp.info` (full-body WBC), `target_manager.yaml`

No invented official dynamics. Full-body body tracking uses `torso_tracking_frame` (ROS X-forward Z-up dummy on `torso_body_link`). Head modes follow W2 (`HEAD_GAZE` / `headCoupling` / `headTrackingEE` / `headMidpointGaze` on `head_camera_mid_optical_frame`, the stereo midline; `muUpright` keeps camera +X gravity-level via `head_roll` only, with `uprightDeadbandDeg 2.0` so roll does not chatter about zero); `target_manager.yaml` keeps `enable_head_control: false` so the head follows OCS2 rather than a joint-space marker. Split-body teleops the head through `head_joint_controller` (RViz joint panel, not the head marker).
