# RobotEra L7 Description

This package contains the description files for the RobotEra L7 humanoid. Both wrists reuse the shared [`xhand1_description`](../../../common/dexhands/xhand1_description) (XHand1).

- Default topology: **upper body + waist** (`variant:=upper`) — no legs
- Full body with legs: `variant:=full` (or any value other than `upper`)
- Default EEF: **XHand1** (`type:=xhand1`, alias `type:=xhand`; per-side `left_type` / `right_type`)
- Colliders: `collider:=simple` (default, existing primitives and some meshes) or `collider:=convex` (visual GLB meshes)
- Control: `ocs2_wbc_controller` with `config/ocs2/fixed_base_tcp.info` (waist×3 + dual 7-DoF arms = 17 DOF)
- Default mode: `HM_DUAL_RELATIVE_FIXED_BASE` + `HEAD_DISABLE`

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
# Without hands:
ros2 launch robot_common_launch visualize.launch.py robot:=robotera_l7 type:=none
```

`type` selects the EEF for both sides. A non-empty `left_type` or `right_type` overrides the corresponding side; for example, `left_type:=none` removes only the left hand. An empty side value falls back to `type`, which defaults to `xhand1`.

### 2.2 Full body
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch visualize.launch.py robot:=robotera_l7 variant:=full
ros2 launch robot_common_launch visualize.launch.py robot:=robotera_l7 variant:=full type:=none
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

For component preview, `type` selects the component rather than the EEF. The `upper`, `left`, and `right` previews include their corresponding XHand1 hands.

## 3. Control (mock)

Uses `xacro/ros2_control/robot.xacro` (default `variant:=upper`) with `hardware:=mock_components` (also `isaac` / `gz`).

### 3.1 Upper-body WBC

Waist×3 + dual 7-DoF arms in one `ocs2_wbc_controller`. The planning URDF freezes fingers via `eef_fixed_joints:=true`; the control URDF retains movable finger joints and interfaces in mock and Isaac modes. OCS2 model: `config/ocs2/fixed_base_tcp.info` (17 DOF, `HM_DUAL_RELATIVE_FIXED_BASE`). Separate hand control depends on the loaded controller configuration.

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch ocs2_arm_controller full_body.launch.py robot:=robotera_l7
ros2 launch ocs2_arm_controller full_body.launch.py robot:=robotera_l7 hardware:=isaac
ros2 launch ocs2_arm_controller full_body.launch.py robot:=robotera_l7 collider:=convex
```

`type:=none` removes the hands from both control and planning URDFs. The current WBC configuration refers to `left_hand_hand_ee_link` and `right_hand_hand_ee_link`, so it must be updated to use frames present in the no-hand model before controlling without hands.

For real hand hardware, use `hardware:=real` with `left_ee_drive_type:=usb` / `right_ee_drive_type:=usb` and the corresponding USB ports. Selecting a hand in the URDF alone does not enable its hardware connection.

## 4. Package layout

| Path | Role |
|------|------|
| `xacro/robot.xacro` | Full / upper topology (`variant`) and EEF selection |
| `xacro/component.xacro` | Component preview (`type:=upper/left/right/left_leg/right_leg`) |
| `xacro/ros2_control/` | Hardware selection and interfaces for waist, arms, and hands |
| `config/ros2_control/ros2_controllers.yaml` | `ocs2_wbc_controller` joint order |
| `config/ocs2/fixed_base_tcp.info` | Fixed-base WBC (17 DOF) |
| `config/ocs2/target_manager.yaml` | Interactive markers / VR |
