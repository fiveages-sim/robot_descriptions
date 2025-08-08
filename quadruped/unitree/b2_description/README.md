# Unitree B2 Description

This repository contains the urdf model of b2. The origin models could be found at [Unitree ROS](https://github.com/unitreerobotics/unitree_ros).

![B2](../../.images/unitree_b2.png)

## Build

```bash
cd ~/ros2_ws
colcon build --packages-up-to b2_description --symlink-install
```

## Visualize the robot

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_visualize_config visualize.launch.py robot:=b2
```

## Launch ROS2 Control

### Mujoco Simulator

* Unitree Guide Controller
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch unitree_guide_controller mujoco.launch.py pkg_description:=b2_description
  ```
* OCS2 Quadruped Controller
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch ocs2_quadruped_controller mujoco.launch.py pkg_description:=b2_description
  ```

### Gazebo Classic 11 (ROS2 Humble)

* Unitree Guide Controller
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch unitree_guide_controller gazebo_classic.launch.py pkg_description:=b2_description height:=0.68
  ```

### Gazebo Harmonic (ROS2 Jazzy)

* Unitree Guide Controller
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch unitree_guide_controller gazebo.launch.py pkg_description:=b2_description height:=0.68
  ```
* OCS2 Quadruped Controller
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch ocs2_quadruped_controller gazebo.launch.py pkg_description:=b2_description height:=0.68
  ```