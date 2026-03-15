# AgileX Nero Description

This package contains the URDF and related files for the AgileX Nero robot manipulator. The origin models can be found
at [agx_arm_sim](https://github.com/agilexrobotics/agx_arm_sim/tree/master/robot_description).

## 1. Build

```bash
cd ~/ros2_ws
colcon build --packages-up-to nero_description --symlink-install
```

## 2. Visualize the robot

### 2.1 Basic Arm Configuration
* Single Arm
    ```bash
    source ~/ros2_ws/install/setup.bash
    ros2 launch robot_common_launch manipulator.launch.py robot:=nero type:="arm_only" direction:=left
    ```
* Dual Arm
    ```bash
    source ~/ros2_ws/install/setup.bash
    ros2 launch robot_common_launch manipulator.launch.py robot:=nero type:="dual"
    ```
  
### 2.2 Full Nero Arm
* Dual Arm with revo2
    ```bash
    source ~/ros2_ws/install/setup.bash
    ros2 launch robot_common_launch manipulator.launch.py robot:=nero type:="dual_brainco" 
    ```
* Dual Arm with ChangingTek AG2F90
    ```bash
    source ~/ros2_ws/install/setup.bash
    ros2 launch robot_common_launch manipulator.launch.py robot:=nero type:="dual_ag2f90" 
    ```
* Dual Arm with Jodell RG75
    ```bash
    source ~/ros2_ws/install/setup.bash
    ros2 launch robot_common_launch manipulator.launch.py robot:=nero type:="dual_rg75" 
    ```

## 3. OCS2 Demo

### 3.1 Official OCS2 Mobile Manipulator Demo

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch manipulator_ocs2.launch.py robot_name:=nero 
```

### 3.2 OCS2 Arm Controller Demo
* Mock Hardware
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch ocs2_arm_controller demo.launch.py robot:=nero type:=left
  ```
* Gazebo
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch ocs2_arm_controller demo.launch.py robot:=nero hardware:=gz world:=warehouse
  ```

* Isaac Sim
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch ocs2_arm_controller demo.launch.py robot:=nero hardware:=isaac type:=arm_only
  ```
