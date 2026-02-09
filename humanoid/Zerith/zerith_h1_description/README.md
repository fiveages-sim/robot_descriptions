# Zerith H1 Description

This package contains the URDF and configuration files for the Zerith H1 humanoid. The origin models could be found at [Zerith_Model](https://github.com/inFpZero/Zerith_Model).

## Build

```bash
cd ~/ros2_ws
colcon build --packages-up-to zerith_h1_description --symlink-install
```

## Visualize the robot

To visualize and check the configuration of the robot in rviz, simply launch:

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch humanoid.launch.py robot:=zerith_h1
```