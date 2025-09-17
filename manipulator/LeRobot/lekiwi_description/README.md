# XLeRobot Description
This package contains the description files for Lekiwi Mobile Manipulator. The origin models could be found at [Lekiwi](https://github.com/SIGRobotics-UIUC/LeKiwi)

## 1. Build
```bash
cd ~/ros2_ws
colcon build --packages-up-to lekiwi_description --symlink-install
```

## 2. Visualize the robot

* Lekiwi with SO100 Arm
    ```bash
    source ~/ros2_ws/install/setup.bash
    ros2 launch robot_common_launch manipulator.launch.py robot:=lekiwi
    ```
  ![lekiwi_100](../../.images/lekiwi_100.png)

* Lekiwi with SO101 Arm
    ```bash
    source ~/ros2_ws/install/setup.bash
    ros2 launch robot_common_launch manipulator.launch.py robot:=lekiwi  type:=so101
    ```
  ![lekiwi_101](../../.images/lekiwi_101.png)

## 3. OCS2 Demo
* With SO101 Arm
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch manipulator_ocs2.launch.py robot_name:=lekiwi
  ```

  ![lekiwi_ocs2](../../.images/lekiwi_ocs2.gif)
