# RobotEra L7 Description

This package contains the description files for RobotEra L7 humanoid. The origin models could be found at [humanoid-lab](https://github.com/roboterax/humanoid-lab). Both wrists reuse the shared [`xhand1_description`](../../../common/dexhands/xhand1_description) (XHand1).

- Default topology: **upper body + waist** (`variant:=upper`) — no legs
- Full body with legs: `variant:=full` (or any value other than `upper`)
- Control: `ocs2_wbc_controller` with `config/ocs2/fixed_base_tcp.info` (waist×3 + dual 7-DoF arms = 17 DOF)

## 1. Build
```bash
cd ~/ros2_ws
colcon build --packages-up-to robotera_l7_description --symlink-install
```

## 2. Visualize the robot

### 2.1 Upper body + waist (default)
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch visualize.launch.py robot:=robotera_l7
ros2 launch robot_common_launch visualize.launch.py robot:=robotera_l7 variant:=upper
```

### 2.2 Full body
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch visualize.launch.py robot:=robotera_l7 variant:=full
```

### 2.3 Component
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch component.launch.py robot:=robotera_l7 type:=upper
ros2 launch robot_common_launch component.launch.py robot:=robotera_l7 type:=left
ros2 launch robot_common_launch component.launch.py robot:=robotera_l7 type:=right
ros2 launch robot_common_launch component.launch.py robot:=robotera_l7 type:=left_leg
ros2 launch robot_common_launch component.launch.py robot:=robotera_l7 type:=right_leg
```

## 3. Control (mock)

Uses `xacro/ros2_control/robot.xacro` (default `variant:=upper`) with `hardware:=mock_components` (also `isaac` / `gz`).

### 3.1 Upper-body WBC
Waist×3 + dual 7-DoF arms in one `ocs2_wbc_controller`. Neck joints are fixed in the URDF (`HEAD_DISABLE`). Fingers are frozen in the planning URDF via `eef_fixed_joints:=true`.
OCS2 model: `config/ocs2/fixed_base_tcp.info` (mode `HM_DUAL_RELATIVE_FIXED_BASE`).

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch ocs2_arm_controller full_body.launch.py robot:=robotera_l7
ros2 launch ocs2_arm_controller full_body.launch.py robot:=robotera_l7 hardware:=isaac
```

## 4. Package layout

| Path | Role |
|------|------|
| `xacro/robot.xacro` | Full / upper topology (`variant`) |
| `xacro/component.xacro` | Component preview (`type:=upper/left/right/...`) |
| `xacro/ros2_control/` | Hardware interfaces for waist + arms |
| `config/ros2_control/ros2_controllers.yaml` | `ocs2_wbc_controller` joint order |
| `config/ocs2/fixed_base_tcp.info` | Fixed-base WBC (17 DOF) |
| `config/ocs2/target_manager.yaml` | Interactive markers / VR |
