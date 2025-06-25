# Dobot CR5 Description

This package contains the description files for Dobot CR5 Manipulator.

## 1. Build
```bash
cd ~/ros2_ws
colcon build --packages-up-to cr5_description --symlink-install
```

## 2. Visualize the robot

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_visualize_config manipulator.launch.py robot:=cr5
```

![cr5](../../.images/dobot_cr5.png)

## 3. OCS2 Demo
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch cr5_description ocs2.launch.py
```