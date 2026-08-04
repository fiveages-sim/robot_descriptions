# Galaxea R1 Description

This package contains the description files for Galaxea R1 Humanoid Robot. The origin models could be found
at [Galaxea URDF](https://github.com/userguide-galaxea/URDF).

## 1. Build

```bash
cd ~/ros2_ws
colcon build --packages-up-to galaxea_r1_description --symlink-install
```

## 2. Visualize the robot
### 2.1 Full Robot
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch manipulator.launch.py robot:=galaxea_r1
```

![Galaxea R1](../../.images/galaxea_r1.png)

### 2.2 Components
* Chassis
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch component.launch.py robot:=galaxea_r1 type:=chassis
  ```

* Torso
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch component.launch.py robot:=galaxea_r1 type:=torso
  ```

## 3. OCS2 Demo

### 3.1 Official OCS2 Mobile Manipulator Demo

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch manipulator_ocs2.launch.py robot_name:=galaxea_r1
```

### 3.2 OCS2 Arm Controller Demo

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch ocs2_arm_controller full_body.launch.py robot:=galaxea_r1
```

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch ocs2_arm_controller demo.launch.py robot:=galaxea_r1 hardware:=gz
```

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch ocs2_arm_controller full_body.launch.py robot:=galaxea_r1 hardware:=isaac
```