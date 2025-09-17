# Zsibot ZSL-1 Description

This repository contains the urdf model of ZSL-1. The origin models could be found at [Zsibot Model](https://github.com/zsibot/zsibot_model).

![ZSL1](../../.images/zsl1.png)

## Build

```bash
cd ~/ros2_ws
colcon build --packages-up-to zsl1_description --symlink-install
```

## Visualize the robot

To visualize and check the configuration of the robot in rviz, simply launch:

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch visualize.launch.py robot:=zsl1
```

### Gazebo Harmonic

* Unitree Guide Controller
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch unitree_guide_controller gazebo.launch.py pkg_description:=magicdog_description
  ```