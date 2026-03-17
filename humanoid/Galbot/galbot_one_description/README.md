# Galbot One Description

This package contains URDF/Xacro/config files for Galbot One, aligned with the workspace conventions used by `robot_common_launch` and `ocs2_arm_controller`.

## Build

```bash
cd ~/ros2_ws
colcon build --packages-up-to galbot_one_description --symlink-install
```

## Visualize

### Full Robot

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch humanoid.launch.py robot:=galbot_one type:=type1
```

Switch to gripper2:

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch humanoid.launch.py robot:=galbot_one type:=type2
```

### Component

* Base
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch component.launch.py robot:=galbot_one type:=base
  ```

* Chassis
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch component.launch.py robot:=galbot_one type:=chassis
  ```

* Body
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch component.launch.py robot:=galbot_one type:=body
  ```

* Arms module
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch component.launch.py robot:=galbot_one type:=arm
  ```

## Full-body OCS2 Demo

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch ocs2_arm_controller full_body.launch.py \
  robot:=galbot_one \
  type:=type1 \
  rviz_config:=/home/angel/ros2_ws/src/robot-descriptions/humanoid/Galbot/galbot_one_description/config/rviz/fullbody.rviz
```

Run with gripper2:

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch ocs2_arm_controller full_body.launch.py \
  robot:=galbot_one \
  type:=type2 \
  rviz_config:=/home/angel/ros2_ws/src/robot-descriptions/humanoid/Galbot/galbot_one_description/config/rviz/fullbody.rviz
```
