# Unitree AlienGo Description

This repository contains the urdf model of Aliengo. The origin models could be found at [Unitree ROS](https://github.com/unitreerobotics/unitree_ros).
 
![Aliengo](../../.images/unitree_aliengo.png)

## Build

```bash
cd ~/ros2_ws
colcon build --packages-up-to aliengo_description  --symlink-install
```

## Visualize the robot

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch visualize.launch.py robot:=aliengo
```

## Launch ROS2 Control

Tested environment:

* Ubuntu 24.04
  * ROS2 Jazzy

### Mujoco Simulator

* Unitree Guide Controller
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch unitree_guide_controller mujoco.launch.py pkg_description:=aliengo_description
  ```
* OCS2 Quadruped Controller
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch ocs2_quadruped_controller mujoco.launch.py pkg_description:=aliengo_description
  ```

### Gazebo Classic 11 (ROS2 Humble)

* Unitree Guide Controller
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch unitree_guide_controller gazebo_classic.launch.py pkg_description:=aliengo_description height:=0.535
  ```

### Gazebo Harmonic (ROS2 Jazzy)

* Unitree Guide Controller
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch unitree_guide_controller gazebo.launch.py pkg_description:=aliengo_description height:=0.535
  ```