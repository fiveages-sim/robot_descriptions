# Galaxea A1 Description

This package contains the description files for Galaxea A1, A1X and A1Y manipulator. I got the origin URDF files from
the [Galaxea URDF](https://github.com/userguide-galaxea/URDF).

## 1. Build

```bash
cd ~/ros2_ws
colcon build --packages-up-to galaxea_a1_description --symlink-install
```

## 2. Visualize the robot

* A1
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_visualize_config manipulator.launch.py robot:=galaxea_a1
  ```

  ![A1X](../../.images/galaxea_a1.png)

* A1 X
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_visualize_config manipulator.launch.py robot:=galaxea_a1 type:=x
  ```

  ![A1X](../../.images/galaxea_a1x.png)

* A1 Y
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_visualize_config manipulator.launch.py robot:=galaxea_a1 type:=y
  ```

  ![A1Y](../../.images/galaxea_a1y.png)

## 3. OCS2 Demo

### 3.1 Official OCS2 Mobile Manipulator Demo

* A1
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_visualize_config manipulator_ocs2.launch.py robot_name:=galaxea_a1
  ```

* A1 X
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_visualize_config manipulator_ocs2.launch.py robot_name:=galaxea_a1 type:=x
  ```

* A1 Y
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_visualize_config manipulator_ocs2.launch.py robot_name:=galaxea_a1 type:=y
  ```

### 3.2 OCS2 Arm Controller Demo
* A1
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch ocs2_arm_controller demo.launch.py robot:=galaxea_a1
  ```
* A1 X
  ```bash
  source ~/ros2_ws/install/setup.bash
    ros2 launch ocs2_arm_controller demo.launch.py robot:=galaxea_a1 hardware:=gz type:=x
  ```

* A1 Y
  ```bash
  source ~/ros2_ws/install/setup.bash
    ros2 launch ocs2_arm_controller demo.launch.py robot:=galaxea_a1 hardware:=gz type:=y
  ```