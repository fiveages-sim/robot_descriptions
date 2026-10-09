# Taku Description

This package contains an **inferred** description of the Dyna Taku / DVT1 wheeled dual-arm robot (4-module swerve chassis, folding lift + waist, 3-DoF head, dual 7-DoF arms, Dynaclaw two-jaw grippers).

> **Not official Dyna specs.** Kinematics (tree / `xyz` / `rpy` / axes) come from the public `dvt1_kin.json` on https://www.dyna.co/dyna-2.1 . Joint limits come from a mesh self-collision sweep snapped to integer degrees that still contain the recorded trajectory ranges. Inertias are scaled from OpenArm v1, Galaxea R1 and Agilex Ranger Mini. Links without a usable reference (waist, torso, head, gripper jaws) have no `<inertial>`. Evidence and sources are in [`doc/taku_params.md`](doc/taku_params.md).

Meshes are per-link GLBs split from Dyna's public viewer GLB. Arm links live under `meshes/arm/` (left/right kept separate — they are not geometric mirrors). Dynaclaw jaws live under `meshes/dynaclaw/` and are shared by both sides. The front lidars use RoboSense Airy and the rear lidar uses Livox MID-360 meshes from [`sensor_models`](../../../common/sensor_models).

## 1. Build

```bash
cd ~/ros2_ws
colcon build --packages-up-to taku_description sensor_models --symlink-install
```

## 2. Visualize the robot

### 2.1. Full robot

```bash
source ~/ros2_ws/install/setup.bash
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

## 3. Files

* `xacro/robot.xacro`: full robot
* `xacro/component.xacro`: component modules selected by `type`
* `xacro/dynaclaw.xacro`: Astribot-style standalone Dynaclaw entry
* `xacro/components/`: `chassis.xacro`, `body.xacro`, `head.xacro`, `arm.xacro` (`TakuArm` with `name` / `direction` / `standalone`), `dynaclaw.xacro` (`TakuDynaclaw`), `gripper.xacro` (thin include of Dynaclaw)
* `xacro/ros2_control/`: `robot.xacro` (mock / gz / isaac hardware), `interfaces.xacro`
* `config/ros2_control/ros2_controllers.yaml`: joint state broadcaster, W2-style `ocs2_arm_controller` / `ocs2_wbc_controller`, plus basic chassis / body / head / arm / Dynaclaw controllers. Homes are the zero pose.
* `config/ocs2/`: `fixed_base_tcp.info` (W2 fixed-base TCP pattern; no head-follow), `target_manager.yaml`

No invented official dynamics. Head-follow / head-tracking (W2 `HEAD_GAZE`, `headCoupling`, `headTrackingEE`, `headMidpointGaze`) are omitted; head joints are removed from the MPC model and driven only via `head_joint_controller`.
