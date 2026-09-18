# AgileX Mobile Aloha Description

This package contains the description files for AgileX's Mobile Aloha2 manipulator. The origin models can be found
at [mobile aloha sim](https://github.com/agilexrobotics/mobile_aloha_sim/tree/v2.0.0)

> **Cobot Magic V1**（原 Mobile Aloha V1）已拆到独立包
> [`cobot_magic_v1_description`](../cobot_magic_v1_description/README.md)：
> `ros2 launch robot_common_launch manipulator.launch.py robot:=cobot_magic_v1`
>
> **Split Aloha**（Ranger Mini + 升降）已拆到独立包
> [`split_aloha_description`](../split_aloha_description/README.md)：
> `ros2 launch robot_common_launch manipulator.launch.py robot:=split_aloha`

本包仅保留 **Aloha V2**（Tracer 底盘 + 固定躯干 + 双 Piper）。

## 1. Build

```bash
cd ~/ros2_ws
colcon build --packages-up-to agilex_aloha_description --symlink-install
```

## 2. Visualize the robot

### 2.1 Full Robot

* Aloha V2 (Tracer V1 Base，默认)
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch manipulator.launch.py robot:=agilex_aloha
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
* Tracer
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch component.launch.py robot:=agilex_aloha
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
