# Booster T1 Description

This package contains the URDF and configuration files for the Booster T1 humanoid. The origin models could be found at [booster_gym](https://github.com/BoosterRobotics/booster_gym).

![T1](../../.images/booster_t1.png)

## Build

```bash
cd ~/ros2_ws
colcon build --packages-up-to t1_description --symlink-install
```

## Visualize the robot

To visualize and check the configuration of the robot in rviz, simply launch:

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch visualize.launch.py robot:=t1
```