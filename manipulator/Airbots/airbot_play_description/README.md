# Airbot Play Description

This package contains the description files for Discover Robotics's Airbot Play manipulator. I got the origin URDF files from the [DISCOVERSE](https://github.com/TATP-233/DISCOVERSE).

## 1. Build
```bash
cd ~/ros2_ws
colcon build --packages-up-to airbot_play_description --symlink-install
```

## 2. Visualize the robot

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_visualize_config manipulator.launch.py robot:=airbot_play
```

![airbot play](../../.images/airbot_play.png)

## 3. OCS2 Demo
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_visualize_config manipulator_ocs2.launch.py robot_name:=airbot_play
```
