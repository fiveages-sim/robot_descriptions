# XLeRobot Description

This package contains the description files for XLeRobot Project. The origin models could be found at [XLeRobot](https://github.com/Vector-Wangel/XLeRobot)

## 1. Build
```bash
cd ~/ros2_ws
colcon build --packages-up-to xlerobot_description --symlink-install
```

## 2. Visualize the robot

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_visualize_config manipulator.launch.py robot:=xlerobot
```