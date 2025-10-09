# Agibot G1 Description

This package contains the description files for Agibot Genie G1 humanoid. The origin models could be found at [GenieSim](https://huggingface.co/datasets/agibot-world/GenieSimAssets).

## 1. Build
```bash
cd ~/ros2_ws
colcon build --packages-up-to agibot_g1_description --symlink-install
```

## 2. Visualize the robot

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch manipulator.launch.py robot:=agibot_g1
```
    
![G1](../../.images/agibot_g1.png)

## 3. OCS2 Demo

### 3.1 Official OCS2 Mobile Manipulator Demo

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch manipulator_ocs2.launch.py robot_name:=agibot_g1
```

[Screencast from 2025-09-05 11-16-59.webm](https://github.com/user-attachments/assets/efc29041-42ae-4062-95d0-0024767ddca1)


### 3.2 OCS2 Arm Controller Demo

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch ocs2_arm_controller demo.launch.py robot:=agibot_g1
```

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch ocs2_arm_controller demo.launch.py robot:=agibot_g1 hardware:=gz world:=warehouse
```

### 4. Navigation
* Gazebo Simulation
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch diff_drive.launch.py robot:=agibot_g1 world:=warehouse
  ```
* SLAM Toolbox
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch navigation_slam.launch.py
  ```