# RobotEra Xbot-L Description

This package contains the description files for RobotEra Xbot-L humanoid. The origin models could be found at [humanoid_gym](https://github.com/roboterax/humanoid-gym). Both wrists reuse the shared [`xhand1_description`](../../../common/dexhands/xhand1_description) (XHand1).

- Default topology: **upper body + waist** (`variant:=upper`) — no legs
- Full body with legs: `variant:=full` (or any value other than `upper`)
- Root: `floating_base` → `base_link` (ROS Z-up hip); waist DOFs lift `torso_base_link`
- Default EEF: **XHand1** (`type:=xhand1`, alias `type:=xhand`; per-side `left_type` / `right_type`)
- Control: `ocs2_wbc_controller` with `config/ocs2/fixed_base_tcp.info` (waist×2 + dual 7-DoF arms + neck×2 = 18 DOF)
- Default mode: **自由** (`HM_DUAL_BODY_FREE`, fixed base auto-locks) + **注视** (`HEAD_GAZE`)
- Colliders: default `collider:=simple` (torso/waist boxes + arm cylinders for OCS2 `selfCollision`); `collider:=convex` restores visual GLBs — do not enable `selfCollision` with that
- Hands (W2-style): sim → finger joints in the main `ros2_control` system; `hardware:=real` + `left_ee_drive_type:=usb` → dedicated `xhand1_*_system` RS485

## 1. Build
```bash
cd ~/ros2_ws
colcon build --packages-up-to robotera_xbotl_description --symlink-install
```

## 2. Visualize the robot

### 2.1 Upper body + waist (default)
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch visualize.launch.py robot:=robotera_xbotl
ros2 launch robot_common_launch visualize.launch.py robot:=robotera_xbotl variant:=upper
ros2 launch robot_common_launch visualize.launch.py robot:=robotera_xbotl collider:=simple
```

![Xbot-L](../.images/robotera_xbotl.png)

### 2.2 Full body
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch visualize.launch.py robot:=robotera_xbotl variant:=full
```

### 2.3 Component
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch component.launch.py robot:=robotera_xbotl type:=upper
ros2 launch robot_common_launch component.launch.py robot:=robotera_xbotl type:=left
ros2 launch robot_common_launch component.launch.py robot:=robotera_xbotl type:=right
ros2 launch robot_common_launch component.launch.py robot:=robotera_xbotl type:=left_hand
ros2 launch robot_common_launch component.launch.py robot:=robotera_xbotl type:=right_hand
ros2 launch robot_common_launch component.launch.py robot:=robotera_xbotl type:=left_leg
ros2 launch robot_common_launch component.launch.py robot:=robotera_xbotl type:=right_leg
```

## 3. Control (mock)

Uses `xacro/ros2_control/robot.xacro` (default `variant:=upper`) with `hardware:=mock_components` (also `isaac` / `isaac_sim` / `gz`).
FaSim Isaac `ROS=fiveages` 走进程内 `IsaacSimSystem`（`hardware:=isaac_sim` + ArtRoot `isaac_prim_path`）。

### 3.1 Upper-body WBC
Waist×2 + dual 7-DoF arms + neck×2 in one `ocs2_wbc_controller`. Default mode: `HM_DUAL_BODY_FREE` + `HEAD_GAZE`. Fingers are frozen in the planning URDF via `eef_fixed_joints:=true`.
OCS2 model: `config/ocs2/fixed_base_tcp.info`.
`selfCollision` (G1d-style, `activate true`): `torso_base_link` ↔ `elbow_pitch` / `wrist_roll` only; `minimumDistance 0.01`, `activationDistance 0.03`. Proximal shoulder links omitted to avoid hang false positives. Requires `collider:=simple`.

`full_body.launch.py` auto-loads `config/rviz/fullbody.rviz` (OCS2 FSM / Joint / Gripper panels + `TargetErrorDisplay` HUD for MPC timing and EE tracking error).

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch ocs2_arm_controller full_body.launch.py robot:=robotera_xbotl
ros2 launch ocs2_arm_controller full_body.launch.py robot:=robotera_xbotl hardware:=isaac
# Isaac 进程内 CM（与 FaSim ROS=fiveages / emit_control 一致）:
ros2 launch ocs2_arm_controller full_body.launch.py robot:=robotera_xbotl hardware:=isaac_sim isaac_prim_path:=/World/XbotL/XbotL_Upper/base_link
```

## 4. Package layout

| Path | Role |
|------|------|
| `xacro/robot.xacro` | Full / upper topology (`variant`, `collider`) |
| `xacro/component.xacro` | Component preview (`type:=upper/left/right/...`) |
| `xacro/ros2_control/` | Hardware interfaces for waist + arms + neck |
| `config/ros2_control/ros2_controllers.yaml` | `ocs2_wbc_controller` joint order |
| `config/ocs2/fixed_base_tcp.info` | Fixed-base WBC + G1d-style `selfCollision` |
| `config/ocs2/target_manager.yaml` | Interactive markers / VR |
| `config/rviz/fullbody.rviz` | RViz (Fixed Frame `world`) + TargetErrorDisplay HUD |
