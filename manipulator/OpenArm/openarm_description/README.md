# OpenArm v1.0 Description

This package contains the description files for OpenArm single and bimanual manipulator. I got the origin XACRO files
from
the [OpenArm XACRO](https://github.com/enactic/openarm_description).

Note: The /meshes/arm/v10/visual/link0.dae file may cause the model not shown due error of
`Not enough data for accessor`. You can change it to .stl file with same suffix name. Howere, the stl file will have
render issue in both rviz and gazebo. So does

## 1. Build

```bash
cd ~/ros2_ws
colcon build --packages-up-to openarm_description --symlink-install
```

## 2. Visualize the robot

* OpenArm Bimanual
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch manipulator.launch.py robot:=openarm
  ```

  ![Bimanual](../../.images/openarm_bimanual.png)

* Left arm only
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch manipulator.launch.py robot:=openarm type:=left
  ```
* Right arm only
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch manipulator.launch.py robot:=openarm type:=right
  ```

  ![Single](../../.images/openarm_single.png)

## 3. OCS2 Demo

### 3.1 Official OCS2 Mobile Manipulator Demo

* OpenArm Bimanual
  ```bash
  # Need to copy and replace task_bimanual.info content into task.info
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch manipulator_ocs2.launch.py robot_name:=openarm 
  ```
  [Screencast from 2025-09-05 18-23-31.webm](https://github.com/user-attachments/assets/a681d0cc-a2a0-4f05-a3d0-64778d28941a)

* OpenArm Single Left
  ```bash
  # Need to copy replace task_single.info content into task.info
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch manipulator_ocs2.launch.py robot_name:=openarm type:=left task_file:=single
  ```
  [Screencast from 2025-09-05 18-25-13.webm](https://github.com/user-attachments/assets/d2fb17a5-b1c2-403d-b398-8532435fc8e8)

### 3.2 OCS2 Arm Controller Demo

Note: need to check the .xacro file under ros2_control, make sure when ros2_control_hardware_type == isaac, the
joint_command is not joint_command's'!!!

#### 3.2.1 OpenArm Bimanual

* Mock Component
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch ocs2_arm_controller demo.launch.py robot:=openarm
  ```
* Gazebo Simulation
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch ocs2_arm_controller demo.launch.py robot:=openarm hardware:=gz world:=warehouse
  ```
  [Screencast from 2025-09-08 17-15-43.webm](https://github.com/user-attachments/assets/97720fe3-d873-4a01-b3a0-c7a084019f31)


#### 3.2.2 OpenArm Single

* Mock Component
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch ocs2_arm_controller demo.launch.py robot:=openarm type:=left
  ```
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch ocs2_arm_controller demo.launch.py robot:=openarm type:=right
  ```
* Gazebo Simulation
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch ocs2_arm_controller demo.launch.py robot:=openarm type:=left hardware:=gz
  ```
