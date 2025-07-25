# ARX Lift Description

This package contains the description files for ARX Lift. The origin models could be found
at [ARX_Models](https://github.com/ARXroboticsX/ARX_Model)

## 1. Build

```bash
cd ~/ros2_ws
colcon build --packages-up-to lift_description --symlink-install
```

## 2. Visualize the robot

* Lift with X5 Arm
    ```bash
    source ~/ros2_ws/install/setup.bash
    ros2 launch robot_visualize_config manipulator.launch.py robot:=lift
    ```
  ![arx lift x5](../../.images/arx_lift2.png)

* Lift with R5 Arm
    ```bash
    source ~/ros2_ws/install/setup.bash
    ros2 launch robot_visualize_config manipulator.launch.py robot:=lift type:="r5"
    ```

  ![arx lift](../../.images/arx_lift.png)

## 3. OCS2 Demo

* Lift with X5 Arm
    ```bash
    source ~/ros2_ws/install/setup.bash
    ros2 launch robot_visualize_config manipulator_ocs2.launch.py robot_name:=lift
    ```
* Lift with R5 Arm
   ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_visualize_config manipulator_ocs2.launch.py robot_name:=lift type:=r5
    ```