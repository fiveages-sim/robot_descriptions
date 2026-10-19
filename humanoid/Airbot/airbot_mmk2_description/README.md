# Airbot MMK2 Description

URDF / xacro and control configs for the Discover Robotics **Airbot MMK2** wheeled dual-arm platform. The original models can be found at [DISCOVERSE](https://github.com/TATP-233/DISCOVERSE).

- Chassis: **Athena2** differential drive (`xacro/components/athena2.xacro`; wheels locked by default)
- Body: fixed lift column (`column_link`) + prismatic lift (`body_joint`) + head yaw / pitch (`head_joint1` / `head_joint2`)
- Meshes: GLB (`chassis.glb` / `base.glb` / wheels / slide / head)
- Arms: Airbot Play (6-DOF) × 2 (from `airbot_play_description`)
- Grippers: built-in parallel jaws; `*_gripper_joint` + `adaptive_gripper_controller`
- Optional hands: `type:=xhand1` mounts XHand1 on both `link6` (offset 0.014 m)
- Wrist cameras (default): `left|right_camera_base` (mesh) + `left|right_camera` (optical); omit with `xacro_camera:=none`

## 1. Build

```bash
cd ~/ros2_ws
colcon build --packages-up-to airbot_mmk2_description --symlink-install
```

## 2. Visualize the robot

### 2.1 Full robot

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch manipulator.launch.py robot:=airbot_mmk2
ros2 launch robot_common_launch manipulator.launch.py robot:=airbot_mmk2 type:=xhand1
ros2 launch robot_common_launch manipulator.launch.py robot:=airbot_mmk2 xacro_camera:=none
```

![airbot mmk2](../../.images/airbot_mmk2.png)

### 2.2 Components

`component.launch.py` loads `airbot_mmk2_description/xacro/component.xacro`。

| `type` | 内容 |
|--------|------|
| `athena2` / `chassis`（默认） | Athena2 底盘；驱动轮默认 **可动** |
| `body` | 升降柱 + slide + 头（空 `base_link`，无底盘） |

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch component.launch.py robot:=airbot_mmk2 type:=athena2
ros2 launch robot_common_launch component.launch.py robot:=airbot_mmk2 type:=chassis
ros2 launch robot_common_launch component.launch.py robot:=airbot_mmk2 type:=body
```

导入 Isaac 资产时去掉 `sensor_models` 视觉（关节和空 link 保留）：

```bash
ros2 launch robot_common_launch component.launch.py robot:=airbot_mmk2 type:=athena2 xacro_isaac:=true
```

## 3. Control (mock)

Uses `xacro/ros2_control/robot.xacro` with `hardware:=mock_components` (also `gz` / `isaac`).

### 3.1 Full body (全身 WBC)

Slide + dual Airbot Play + head in one `ocs2_wbc_controller` (chassis fixed).
Lift-only body: no custom joint lock; initial body mode `HM_DUAL_RELATIVE_FIXED_BASE` (falls back to FREE). Body follow (`BODY_TRACKING` on `torso_tracking_frame`) stays available.
Head follow is on by default (`headMode HEAD_GAZE`: look through the head D435i `head_camera`, not `head_pitch_link`); `homeJointReference` softly pulls joints toward controller `home_1`.
OCS2 model: `config/ocs2/fixed_base_tcp.info`.

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch ocs2_arm_controller full_body.launch.py robot:=airbot_mmk2
ros2 launch ocs2_arm_controller full_body.launch.py robot:=airbot_mmk2 hardware:=isaac
```

### 3.2 Dual-arm OCS2 demo

Airbot Play dual arms via `ocs2_arm_controller`. Slide / head / grippers are separate controllers.

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch ocs2_arm_controller demo.launch.py robot:=airbot_mmk2
ros2 launch ocs2_arm_controller demo.launch.py robot:=airbot_mmk2 hardware:=gz
ros2 launch ocs2_arm_controller demo.launch.py robot:=airbot_mmk2 hardware:=isaac
```

### 3.3 Split body (arms + slide + head)

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch ocs2_arm_controller split_body.launch.py robot:=airbot_mmk2
```

- Arms: `/ocs2_arm_controller/...`
- Slide: `/body_joint_controller/...` (`body_joint` [m]; **positive = down**, range −0.04…0.87)
- Head: `/head_joint_controller/...` (`head_joint1` / `head_joint2`)
- Grippers: `/left_hand_controller`, `/right_hand_controller` (`adaptive_gripper_controller` on `left_gripper_joint` / `right_gripper_joint`)

### 3.4 Official OCS2 Mobile Manipulator demo

Uses `config/ocs2/mobile_demo.info` (wheel-based mobile model, slide as an arm DOF).

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch manipulator_ocs2.launch.py robot_name:=airbot_mmk2 task_file:=mobile_demo
```

### 3.5 End-effector / gripper notes

- Default: `left_gripper_joint` / `right_gripper_joint` (`*_gripper_joint1` follows)
- `type:=xhand1`: XHand1 on both wrists (`left_hand_*` / `right_hand_*`); planning freezes finger DOFs
- TCP frames: `left_gripper_center` / `right_gripper_center` (xhand1: child of `*_hand_ee_link`)

### 3.6 Chassis joints (drive wheels)

Same convention as FiveAges W2 / Ai2 Bot2 / Quanta X1 / Zerith H1:

- **整机 / 运控 URDF**（`robot.xacro`、`ros2_control/robot.xacro`）默认 **`chassis_joints_movable:=false`**：`left_wheel_joint` / `right_wheel_joint` 为 **`fixed`**，不进 `ros2_control`。OCS2 planning 由 `robot_common_launch` 注入 `chassis_joints_movable:=false`（与 W2 / Taku / DexForce 相同）。
- **部件预览** `component.launch.py` `type:=athena2` / `type:=chassis` 默认轮子 **可动**；静态预览可加 `chassis_joints_movable:=false`。
- 差速导航再设 `chassis_joints_movable:=true`（轮速接口 + `diff_drive_controller`）。

## 4. Navigation

* Gazebo Simulation
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch diff_drive.launch.py robot:=airbot_mmk2 world:=warehouse chassis_joints_movable:=true
  ```
* SLAM Toolbox
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch navigation_slam.launch.py
  ```

## 5. Layout

| Path | Role |
|------|------|
| `xacro/robot.xacro` | Visualization kinematics (`chassis_joints_movable`, `isaac`) |
| `xacro/component.xacro` | Athena2-only (`component.launch.py` `type:=athena2`；`xacro_isaac:=true` 导入 Isaac) |
| `xacro/components/athena2.xacro` | Athena2 chassis (`base_link` + wheels + chassis camera / lidar) |
| `xacro/ros2_control/robot.xacro` | Hardware plugins + joint interfaces |
| `config/ros2_control/ros2_controllers.yaml` | Controller manager |
| `config/rviz/fullbody.rviz` / `splitbody.rviz` | RViz (Fixed Frame `world` / `base_link`), auto-picked by `full_body` / `split_body` launch |
| `config/ocs2/task.info` | Dual-arm OCS2 model (demo / split arms) |
| `config/ocs2/fixed_base_tcp.info` | Full-body WBC (body + arms + head); Pinocchio 4 order body\|head\|L\|R |
| `config/ocs2/target_manager.yaml` | Marker / VR frames (`base_link`, `head_camera` D435i) |
| `config/ocs2/mobile_demo.info` | Official OCS2 mobile-manipulator demo model |
