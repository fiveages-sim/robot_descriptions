# EngineAI PM01 Description

This package contains the URDF and configuration files for the EngineAI PM01 humanoid. The origin models could be found at [engineai_ros2_workspace](https://github.com/engineai-robotics/engineai_ros2_workspace).

![PM01](../../.images/engineai_pm01.png)

## Build

```bash
cd ~/ros2_ws
colcon build --packages-up-to pm01_description --symlink-install
```

## Visualize the robot

To visualize and check the configuration of the robot in rviz, simply launch:

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch visualize.launch.py robot:=pm01
```