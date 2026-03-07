# AgileX Nero Description

This package contains the URDF and related files for the AgileX Nero robot manipulator. The origin models can be found
at [agx_arm_sim](https://github.com/agilexrobotics/agx_arm_sim/tree/master/robot_description).

## 1. Build

```bash
cd ~/ros2_ws
colcon build --packages-up-to nero_description --symlink-install
```

## 2. Visualize the robot

* Launch left Nero Arm with v1 stand
    ```bash
    source ~/ros2_ws/install/setup.bash
    ros2 launch robot_common_launch manipulator.launch.py robot:=nero type:="v1" direction:=left
    ```
* Launch left Nero Arm with revo2 hand
    ```bash
    source ~/ros2_ws/install/setup.bash
    ros2 launch robot_common_launch manipulator.launch.py robot:=nero type:="hand" direction:=left
    ```
* Launch right Nero Arm with v1 stand
    ```bash
    source ~/ros2_ws/install/setup.bash
    ros2 launch robot_common_launch manipulator.launch.py robot:=nero type:="v1" direction:=right
    ```
* Launch right Nero Arm with revo2 hand
    ```bash
    source ~/ros2_ws/install/setup.bash
    ros2 launch robot_common_launch manipulator.launch.py robot:=nero type:="hand" direction:=right
    ```

## 3. OCS2 Demo

### 3.1 Official OCS2 Mobile Manipulator Demo

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch manipulator_ocs2.launch.py robot_name:=nero
```

### 3.2 OCS2 Arm Controller Demo
* Gazebo
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch ocs2_arm_controller demo.launch.py robot:=nero hardware:=gz world:=warehouse
  ```

* Isaac Sim
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch ocs2_arm_controller demo.launch.py robot:=nero hardware:=isaac
  ```
