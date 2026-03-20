# Ai2 Bot2 Description

This package contains the URDF and configuration files for the Ai2 Bot2 humanoid. 

## 1. Build

```bash
cd ~/ros2_ws
colcon build --packages-up-to ai2_bot2_description --symlink-install
```

## 2. Visualize the robot
### 2.1 Full Robot
* Ai2 Bot2 (Basic visualization)
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch manipulator.launch.py robot:=ai2_bot2
```
* With Inspire EG2 Gripper
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch manipulator.launch.py robot:=ai2_bot2 type:=inspire
```

![Ai2 Bot2](../../.images/ai2_bot2.png)

### 2.2 Component
* Base
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch component.launch.py robot:=ai2_bot2
  ```
* Arms
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch component.launch.py robot:=ai2_bot2 type:=arms
  ```
* Left arm
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch component.launch.py robot:=ai2_bot2 type:=left_arm
  ```
* Chassis
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch component.launch.py robot:=ai2_bot2 type:=chassis
  ```
* Body
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch component.launch.py robot:=ai2_bot2 type:=body
  ```
  
## 3. OCS2 Demo

### 3.1 Full Body Control


```bash
source ~/ros2_ws/install/setup.bash
ros2 launch ocs2_arm_controller full_body.launch.py robot:=ai2_bot2
```

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch ocs2_arm_controller full_body.launch.py robot:=ai2_bot2 type:=inspire
```

### 3.2 Split Body Control


```bash
source ~/ros2_ws/install/setup.bash
ros2 launch ocs2_arm_controller split_body.launch.py robot:=ai2_bot2
```

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch ocs2_arm_controller split_body.launch.py robot:=ai2_bot2 type:=inspire
```

### 3.3 Isaac Sim

* Empty Hand
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch ocs2_arm_controller demo.launch.py robot:=ai2_bot2 hardware:=isaac
```
* With Inspire EG2 Gripper
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch ocs2_arm_controller demo.launch.py robot:=ai2_bot2 type:=inspire hardware:=isaac
```

https://github.com/user-attachments/assets/ba05a717-cc46-4093-aa56-1ad4ea8a5264


