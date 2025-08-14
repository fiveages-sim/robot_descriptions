# ARX X5/R5 Description

This package contains the description files for ARX X5/R5 Manipulator. The origin models could be found
at [ARX_Models](https://github.com/ARXroboticsX/ARX_Model)

## 1. Build

```bash
cd ~/ros2_ws
colcon build --packages-up-to arx5_description --symlink-install
```

## 2. Visualize the robot

To visualize and check the configuration of the robot in rviz, simply launch:

* ARX X5
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_visualize_config manipulator.launch.py robot:=arx5
  ```

  ![arx x5](../../.images/arx_x5.png)

* ARX R5
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_visualize_config manipulator.launch.py robot:=arx5 type:="r5"
  ```

  ![arx r5](../../.images/arx_r5.png)

## 3. OCS2 Demo

### 3.1 Official OCS2 Mobile Manipulator Demo

* ARX X5
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_visualize_config manipulator_ocs2.launch.py robot_name:=arx5
  ```
* ARX R5
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_visualize_config manipulator_ocs2.launch.py robot_name:=arx5 type:=r5
  ```

### 3.2 OCS2 Arm Controller Demo

* ARX X5
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch ocs2_arm_controller demo.launch.py robot:=arx5
  ```

* ARX R5
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch ocs2_arm_controller demo.launch.py robot:=arx5 type:=r5 hardware:=gz
  ```