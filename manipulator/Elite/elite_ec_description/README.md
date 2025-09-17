# Elite EC series Description

This package contains the description files for Elite EC Series Manipulator. The origin models could be found
at [Elite ROS](https://github.com/Elite-Robots/ROS).

## 1. Build

```bash
cd ~/ros2_ws
colcon build --packages-up-to elite_ec_description --symlink-install
```

## 2. Visualize the robot

* EC66
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch manipulator.launch.py robot:=elite_ec
  ```
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch manipulator.launch.py robot:=elite_ec collider:=simple
  ```

  ![ec66](../../.images/elite_ec66.png)

## 3. OCS2 Demo

### 3.1 Official OCS2 Mobile Manipulator Demo

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch manipulator_ocs2.launch.py robot_name:=elite_ec
```

### 3.2 OCS2 Arm Controller Demo

* Gazebo
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch ocs2_arm_controller demo.launch.py hardware:=gz robot:=elite_ec
  ```
* Isaac Sim
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch ocs2_arm_controller demo.launch.py hardware:=isaac robot:=elite_ec
  ```
* Real Robot
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch ocs2_arm_controller demo.launch.py hardware:=real type:=empty
  ```