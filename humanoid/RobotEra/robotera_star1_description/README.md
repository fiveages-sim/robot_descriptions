# RobotEra STAR1 Description

This package contains the description files for RobotEra STAR1 humanoid (upstream internal code L3). Both wrists reuse the shared [`xhand1_description`](../../../common/dexhands/xhand1_description) (XHand1).

- Root: **pelvis** (`base_link`); waist chain goes up to `torso_base_link` (chest); arms/neck on torso
- Default topology: **upper body + waist** (`variant:=upper`) — no legs
- Full body with legs: `variant:=full` (or any value other than `upper`)
- Default EEF: **XHand1** (`type:=xhand1`, alias `type:=xhand`; per-side `left_type` / `right_type`)
- Colliders: `collider:=simple` (default, box/cylinder for OCS2 selfCollision) or `collider:=convex`
- Control: `ocs2_wbc_controller` with `config/ocs2/fixed_base_tcp.info` (waist×3 + dual 7-DoF arms + neck×2 = 19 DOF)
- Default mode: **自由** (`HM_DUAL_BODY_FREE`, fixed base auto-locks) + **注视** (`HEAD_GAZE`)

## 1. Build
```bash
cd ~/ros2_ws
colcon build --packages-up-to robotera_star1_description --symlink-install
```

## 2. Visualize the robot

### 2.1 Upper body + waist (default)
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch visualize.launch.py robot:=robotera_star1
ros2 launch robot_common_launch visualize.launch.py robot:=robotera_star1 variant:=upper
```

### 2.2 Full body
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch visualize.launch.py robot:=robotera_star1 variant:=full
```

### 2.3 Component
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch component.launch.py robot:=robotera_star1 type:=upper
ros2 launch robot_common_launch component.launch.py robot:=robotera_star1 type:=left
ros2 launch robot_common_launch component.launch.py robot:=robotera_star1 type:=right
ros2 launch robot_common_launch component.launch.py robot:=robotera_star1 type:=left_leg
ros2 launch robot_common_launch component.launch.py robot:=robotera_star1 type:=right_leg
ros2 launch robot_common_launch component.launch.py robot:=robotera_star1 type:=lower
```

Isaac / FaSim import: `isaac:=true` strips the D455 visual (keeps empty `realsense_link`); `type:=none` omits hands (EE payload). Lower component uses a stub pelvis `base_link` + both legs for Assembler.

## 3. Control (mock)

Uses `xacro/ros2_control/robot.xacro` (default `variant:=upper`) with `hardware:=mock_components` (also `isaac` / `isaac_sim` / `gz`).
FaSim Isaac `ROS=fiveages` 走进程内 `IsaacSimSystem`（`hardware:=isaac_sim` + ArtRoot `isaac_prim_path`）。

### 3.1 Upper-body WBC
Waist×3 + dual 7-DoF arms + neck×2 in one `ocs2_wbc_controller`. Default mode: `HM_DUAL_BODY_FREE` + `HEAD_GAZE`. Fingers frozen via `eef_fixed_joints:=true`. Use `collider:=simple` (default) so selfCollision pairs are boxes/cylinders.
OCS2 model: `config/ocs2/fixed_base_tcp.info` (19 DOF). Hand controllers come from `xhand1` `control_compose` (`type:=xhand1`).

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch ocs2_arm_controller full_body.launch.py robot:=robotera_star1
ros2 launch ocs2_arm_controller full_body.launch.py robot:=robotera_star1 hardware:=isaac
# Isaac 进程内 CM（与 FaSim ROS=fiveages / emit_control 一致）:
ros2 launch ocs2_arm_controller full_body.launch.py robot:=robotera_star1 hardware:=isaac_sim isaac_prim_path:=/World/Star1/Star1_Upper/base_link
```

`full_body.launch.py` auto-loads `config/rviz/fullbody.rviz` (OCS2 FSM / Joint / Gripper panels + `TargetErrorDisplay` HUD for MPC timing and EE tracking error).

## 4. Package layout

| Path | Role |
|------|------|
| `xacro/robot.xacro` | Full / upper topology (`variant`) |
| `xacro/component.xacro` | Component preview (`type:=upper/lower/left/right/...`)；`isaac:=true` / `eef:=none` 用于 Isaac 导入 |
| `xacro/ros2_control/` | Hardware interfaces for waist + arms + hands |
| `config/ros2_control/ros2_controllers.yaml` | `ocs2_wbc_controller` joint order + XHand1 |
| `config/ocs2/fixed_base_tcp.info` | Fixed-base WBC (19 DOF + HEAD_GAZE, selfCollision) |
| `config/ocs2/target_manager.yaml` | Interactive markers / VR |
| `config/rviz/fullbody.rviz` | RViz (Fixed Frame `world`) + TargetErrorDisplay HUD |
