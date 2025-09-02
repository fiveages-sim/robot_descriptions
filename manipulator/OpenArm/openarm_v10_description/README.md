# OpenArm v1.0 Description

This package contains the description files for OpenArm single and bimanual manipulator. I got the origin XACRO files from
the [OpenArm XACRO](https://github.com/enactic/openarm_description).

## 1. Build

```bash
cd ~/ros2_ws
colcon build --packages-up-to openarm_v10_description --symlink-install
```

## 2. Visualize the robot

* OpenArm Bimanual
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_visualize_config manipulator.launch.py robot:=openarm_v10 type:=bimanual
  ```

  ![Bimanual](../../.images/openarm_bimanual.png)

* OpenArm Single
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_visualize_config manipulator.launch.py robot:=openarm_v10 type:=single
  ```

  ![Single](../../.images/openarm_single.png)


## 3. OCS2 Demo

### 3.1 Official OCS2 Mobile Manipulator Demo

* OpenArm Bimanual
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_visualize_config manipulator_ocs2.launch.py robot_name:=openarm_v10 type:=bimanual
  ```

* OpenArm Single
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_visualize_config manipulator_ocs2.launch.py robot_name:=openarm_v10 type:=single
  ```


### 3.2 OCS2 Arm Controller Demo
* OpenArm Bimanual
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch ocs2_arm_controller demo.launch.py robot:=openarm_v10 type:=bimanual
  ```
* OpenArm Single
  ```bash
  source ~/ros2_ws/install/setup.bash
    ros2 launch ocs2_arm_controller demo.launch.py robot:=openarm_v10 hardware:=gz type:=single
  ```
