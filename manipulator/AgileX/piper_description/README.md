# AgileX Piper Description

This package contains the URDF and related files for the AgileX Piper robot manipulator. The origin models can be found
at [mobile aloha sim](https://github.com/agilexrobotics/mobile_aloha_sim/tree/v2.0.0)

## 1. Build

```bash
cd ~/ros2_ws
colcon build --packages-up-to piper_description --symlink-install
```

## 2. Visualize the robot

* Launch Slave Arm with camera
    ```bash
    source ~/ros2_ws/install/setup.bash
    ros2 launch robot_visualize_config manipulator.launch.py
    ```
  ![piper](../../.images/agilex_piper.png)
* Launch Master Arm
    ```bash
    source ~/ros2_ws/install/setup.bash
    ros2 launch robot_visualize_config manipulator.launch.py type:="master"
    ```
  ![piper master](../../.images/agilex_piper_master.png)

## 3. OCS2 Demo

### 3.1 Official OCS2 Mobile Manipulator Demo

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_visualize_config manipulator_ocs2.launch.py robot_name:=piper
```

### 3.2 OCS2 Arm Controller Demo

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch ocs2_arm_controller demo.launch.py robot:=piper hardware:=gz
```