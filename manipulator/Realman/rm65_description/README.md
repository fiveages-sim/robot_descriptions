# Realman RM65 Description

This package contains the description files for Realman RM65 manipulator. The origin models could be found at [RM_Models](https://github.com/RealManRobot/rm_models).

## 1. Build
```bash
cd ~/ros2_ws
colcon build --packages-up-to rm65_description --symlink-install
```

## 2. Visualize the robot

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_visualize_config manipulator.launch.py robot:=rm65
```

![RM65](../../.images/realman_rm65.png)

## 3. OCS2 Demo
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_visualize_config manipulator_ocs2.launch.py robot_name:=rm65
```