# Galaxea A1X/Y Description

This package contains the description files for Galaxea A1X and A1Y manipulator. I got the origin URDF files from the [Galaxea URDF](https://github.com/userguide-galaxea/URDF).

## 1. Build
```bash
cd ~/ros2_ws
colcon build --packages-up-to a1xy_description --symlink-install
```

## 2. Visualize the robot

* A1 X
    ```bash
    source ~/ros2_ws/install/setup.bash
    ros2 launch robot_visualize_config manipulator.launch.py robot:=a1xy
    ```
    
    ![A1X](../../.images/galaxea_a1x.png)

* A1 Y
    ```bash
    source ~/ros2_ws/install/setup.bash
    ros2 launch robot_visualize_config manipulator.launch.py robot:=a1xy arm_type:=y
    ```

  ![A1X](../../.images/galaxea_a1y.png)

## 3. OCS2 Demo
* A1 X
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_visualize_config manipulator_ocs2.launch.py robot_name:=a1xy
  ```

* A1 Y
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_visualize_config manipulator_ocs2.launch.py robot_name:=a1xy type:=y
  ```