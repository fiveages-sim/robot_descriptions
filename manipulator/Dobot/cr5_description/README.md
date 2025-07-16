# Dobot CR5 Description

This package contains the description files for Dobot CR5 Manipulator. The origin models could be found at [DOBOT_6Axis_ROS2_V4](https://github.com/Dobot-Arm/DOBOT_6Axis_ROS2_V4).

## 1. Build
```bash
cd ~/ros2_ws
colcon build --packages-up-to cr5_description --symlink-install
```

## 2. Visualize the robot

* Without gripper
    ```bash
    source ~/ros2_ws/install/setup.bash
    ros2 launch robot_visualize_config manipulator.launch.py robot:=cr5
    ```
    ![cr5](../../.images/dobot_cr5.png)

* With Robotiq 85 Gripper
    ```bash
    source ~/ros2_ws/install/setup.bash
    ros2 launch robot_visualize_config manipulator.launch.py robot:=cr5 arm_type:="robotiq85"
    ```
  ![cr5 robotiq85](../../.images/dobot_cr5_robotiq85.png)

## 3. OCS2 Demo
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_visualize_config manipulator_ocs2.launch.py robot_name:=cr5
```

![cr5 ocs2](../../.images/dobot_cr5_ocs2.gif)