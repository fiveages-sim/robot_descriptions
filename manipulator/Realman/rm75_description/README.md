# Realman RM 65&75 Description

This package contains the description files for Realman RM65 manipulator. The origin models could be found at [RM_Models](https://github.com/RealManRobot/rm_models).

## 1. Build
```bash
cd ~/ros2_ws
colcon build --packages-up-to rm75_description --symlink-install
```

## 2. Visualize the robot

### 2.1 RM75 Series
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch manipulator.launch.py robot:=rm75
```
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch manipulator.launch.py robot:=rm75 type:=none
```
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch manipulator.launch.py robot:=rm75 type:=fb
```
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch manipulator.launch.py robot:=rm75 type:=fb_camera
```
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch manipulator.launch.py robot:=rm75 type:=aidal
```

### 2.2. RM65 Series
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch manipulator.launch.py robot:=rm75 type:=65
```
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch manipulator.launch.py robot:=rm75 type:=65_fb
```

### 2.3 RM75 FB75 Camera Component
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch component.launch.py robot:=rm75 type:=fb75_camera
```

![RM65](../../.images/realman_rm65.png)

## 3. OCS2 Demo
### 3.1 Official OCS2 Mobile Manipulator Demo
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch manipulator_ocs2.launch.py robot_name:=rm75
```

### 3.2 OCS2 Arm Controller Demo
#### RM75
* Mock Components
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch ocs2_arm_controller demo.launch.py robot:=rm75
  ```
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch ocs2_arm_controller demo.launch.py robot:=rm75 type:=aidal
  ```
* Gazebo
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch ocs2_arm_controller demo.launch.py robot:=rm75 type:=EG2-4C2 hardware:=gz
  ```
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch ocs2_arm_controller demo.launch.py hardware:=gz robot:=rm65 type:=EG2-4C2 hardware:=gz world:=dart
  ```
* Isaac
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch ocs2_arm_controller demo.launch.py robot:=rm75 type:=aidal hardware:=isaac
  ```

#### RM65
* Mock Components
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch ocs2_arm_controller demo.launch.py robot:=rm75 type:=65
  ```