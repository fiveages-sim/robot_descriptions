# Agibot A2 Description

This package contains the description files for Agibot A2 humanoid. The origin models could be found at [GMR](https://github.com/YanjieZe/GMR).

## 1. Build
```bash
cd ~/ros2_ws
colcon build --packages-up-to agibot_a2_description --symlink-install
```

## 2. Visualize the robot
### 2.1 Full Robot
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch manipulator.launch.py robot:=agibot_a2
  ```
  ![A2](../.images/agibot_a2.png)
### 2.2 Component
* Base
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch component.launch.py
  ```
* Left Arm
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch component.launch.py robot:=agibot_a2 type:=left
  ```
* Right Arm
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch component.launch.py robot:=agibot_a2 type:=right
  ```
* Left Hand
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch component.launch.py robot:=agibot_a2 type:=left_hand
  ```
* Right Hand
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch component.launch.py robot:=agibot_a2 type:=right_hand
  ```
* Left Leg
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch component.launch.py robot:=agibot_a2 type:=left_leg
  ```
* Right Leg
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch component.launch.py robot:=agibot_a2 type:=right_leg
  ```
