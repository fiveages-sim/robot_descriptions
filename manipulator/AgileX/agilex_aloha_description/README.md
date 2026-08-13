# AgileX Mobile Aloha Description

This package contains the description files for AgileX's Mobile Aloha2 manipulator. The origin models can be found
at [mobile aloha sim](https://github.com/agilexrobotics/mobile_aloha_sim/tree/v2.0.0)

## 1. Build

```bash
cd ~/ros2_ws
colcon build --packages-up-to agilex_aloha_description --symlink-install
```

## 2. Visualize the robot
> **Cobot Magic V1**（原 Mobile Aloha V1）已拆到独立包
> [`cobot_magic_v1_description`](../cobot_magic_v1_description/README.md)：
> `ros2 launch robot_common_launch manipulator.launch.py robot:=cobot_magic_v1`

### 2.1 Full Robot
* Aloha Split
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch manipulator.launch.py robot:=agilex_aloha
  ```
  
  ![split](../../.images/agilex_split_aloha.png)

* Aloha V2 (Tracer V1 Base)
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch manipulator.launch.py robot:=agilex_aloha type:="v2"
  ```

  ![aloha2](../../.images/agilex_aloha2.png)
* Aloha V2 (Tracer V2 Base)
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch manipulator.launch.py robot:=agilex_aloha type:="v2-1"
```

* Aloha V2 (Tracer V2 Base with Master Arm)
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch manipulator.launch.py robot:=agilex_aloha type:="v2-master"
```

### 2.2 Component
* Ranger Mini
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch component.launch.py robot:=agilex_aloha
  ```
* Tracer
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch component.launch.py robot:=agilex_aloha type:=tracer
  ```
* Tracer V2
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch component.launch.py robot:=agilex_aloha type:=tracer_v2
  ```
* V2 Body
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch component.launch.py robot:=agilex_aloha type:=body_v2
  ```
* Split Body
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch component.launch.py robot:=agilex_aloha type:=body_split
  ```

## 3. OCS2 Demo

### 3.1 Official OCS2 Mobile Manipulator Demo

* Split Aloha
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch manipulator_ocs2.launch.py robot_name:=agilex_aloha dual_arm:=true
  ```

### 3.2 OCS2 Arm Controller Demo

* Split Aloha
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch ocs2_arm_controller demo.launch.py robot:=agilex_aloha
  ```
    ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch ocs2_arm_controller demo.launch.py robot:=agilex_aloha hardware:=gz world:=warehouse
  ```