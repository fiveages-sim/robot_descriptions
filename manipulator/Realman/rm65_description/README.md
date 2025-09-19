# Realman RM65 Description

This package contains the description files for Realman RM65 manipulator. The origin models could be found at [RM_Models](https://github.com/RealManRobot/rm_models).

## 1. Build
```bash
cd ~/ros2_ws
colcon build --packages-up-to rm65_description --symlink-install
```

## 2. Visualize the robot

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch manipulator.launch.py robot:=rm65
```

![RM65](../../.images/realman_rm65.png)

## 3. OCS2 Demo
### 3.1 Official OCS2 Mobile Manipulator Demo
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch manipulator_ocs2.launch.py robot_name:=rm65
```

### 3.2 OCS2 Arm Controller Demo
* Mock Components
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch ocs2_arm_controller demo.launch.py robot:=rm65 type:=EG2-4C2
  ```
* Gazebo
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch ocs2_arm_controller demo.launch.py robot:=rm65 type:=EG2-4C2 hardware:=gz
  ```
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch ocs2_arm_controller demo.launch.py hardware:=gz robot:=rm65 type:=EG2-4C2 hardware:=gz world:=dart
  ```