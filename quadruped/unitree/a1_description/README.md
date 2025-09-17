# Unitree A1 Description

This repository contains the urdf model of A1. The origin models could be found at [Unitree ROS](https://github.com/unitreerobotics/unitree_ros).

![A1](../../.images/unitree_a1.png)

## Build

```bash
cd ~/ros2_ws
colcon build --packages-up-to a1_description --symlink-install
```

## Visualize the robot

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch visualize.launch.py robot:=a1
```

## Launch ROS2 Control

* Ubuntu 24.04
    * ROS2 Jazzy

### Mujoco Simulator

* Unitree Guide Controller
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch unitree_guide_controller mujoco.launch.py pkg_description:=a1_description
  ```
* OCS2 Quadruped Controller
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch ocs2_quadruped_controller mujoco.launch.py pkg_description:=a1_description
  ```
* RL Quadruped Controller
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch rl_quadruped_controller mujoco.launch.py pkg_description:=a1_description
  ```

### Gazebo Classic 11 (ROS2 Humble)

* Unitree Guide Controller
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch unitree_guide_controller gazebo_classic.launch.py pkg_description:=a1_description height:=0.43
  ```

### Gazebo Harmonic (ROS2 Jazzy)

* Unitree Guide Controller
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch unitree_guide_controller gazebo.launch.py pkg_description:=a1_description height:=0.43
  ```
* OCS2 Quadruped Controller
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch ocs2_quadruped_controller gazebo.launch.py pkg_description:=a1_description  height:=0.43
  ```
* RL Quadruped Controller
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch rl_quadruped_controller gazebo.launch.py pkg_description:=a1_description height:=0.43
  ```