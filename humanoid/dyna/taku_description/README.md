# Taku Description

This package contains an **inferred** description of the Dyna Taku / DVT1 wheeled dual-arm robot (4-module swerve chassis, folding lift + waist, 3-DoF head, dual 7-DoF arms, two-jaw grippers).

> **Not official Dyna specs.** Kinematics (tree / `xyz` / `rpy` / axes) come from the public `dvt1_kin.json` on https://www.dyna.co/dyna-2.1 . Joint limits come from a mesh self-collision sweep snapped to integer degrees that still contain the recorded trajectory ranges. Inertias are scaled from OpenArm v1, Galaxea R1 and Agilex Ranger Mini. Links without a usable reference (waist, torso, head, gripper jaws) have no `<inertial>`. Evidence and sources are in [`doc/taku_params.md`](doc/taku_params.md).

Meshes are per-link GLBs split from Dyna's public viewer GLB. The front lidars use RoboSense Airy and the rear lidar uses Livox MID-360 meshes from [`sensor_models`](../../../common/sensor_models).

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
| `upper_body` | body + head + dual arms, no chassis and no grippers                      |
| `head`       | head yaw / pitch / roll + stereo camera frames                           |
| `arm`        | both arms with grippers                                                  |
| `left_arm` / `right_arm` | one arm with its gripper                                     |
| `gripper`    | one gripper (`side:=left` or `side:=right`)                              |

Hide the sensor_models lidar meshes for an Isaac asset import with `xacro_isaac:=true`.

## 3. Files

* `xacro/robot.xacro`: full robot
* `xacro/component.xacro`: component modules selected by `type`
* `xacro/components/`: `chassis.xacro` (`TakuChassis`, `TakuSwerveModule`), `body.xacro` (`TakuBody`), `head.xacro` (`TakuHead`), `arm.xacro` (`TakuArm`, `direction:=1` left / `-1` right), `gripper.xacro` (`TakuGripper`)
* `xacro/ros2_control/`: `robot.xacro` (mock / gz / isaac hardware), `interfaces.xacro`
* `config/ros2_control/ros2_controllers.yaml`: joint state broadcaster plus position controllers for the body, head, arms and grippers. All home poses are the zero pose.

No OCS2 config yet. The MPC weights cannot be inferred from public data.
