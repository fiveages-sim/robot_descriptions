# AgileX Piper Description

Piper / Piper H / Piper L / Piper X。臂宏停在 `tcp`，夹爪与可选 Revo1 / Revo2 由 `eefs.xacro` 挂载（对齐 AR5 CCS 的 `arms` / `type`）。

原始外观模型：[mobile aloha sim](https://github.com/agilexrobotics/mobile_aloha_sim/tree/v2.0.0)；H/L/X 运动学来自 [agx_arm_urdf](https://github.com/agilexrobotics/agx_arm_urdf)。

## 1. Build

```bash
cd ~/ros2_ws
colcon build --packages-up-to piper_description --symlink-install
```

## 2. Visualize

默认：标准 Piper + 作业夹爪 + 腕部相机 TF。夹爪统一为法兰 / `gripper_base` / pad（H/L/X 相同）。

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch manipulator.launch.py robot:=piper
```

![piper](../../.images/agilex_piper.png)

| 场景 | 参数 |
|------|------|
| Piper H / L / X | `arms:=h` / `l` / `x` |
| 裸腕 | `type:=none` |
| Revo1 | `type:=revo1`（默认关相机） |
| Revo2 | `type:=revo2`（默认关相机） |
| 关相机 | `xacro_camera:=false` |
| Dabai 支架 + Orbbec 相机 | `xacro_camera:=dabai` |
| 仅夹爪 | `ros2 launch robot_common_launch gripper.launch.py gripper:=piper` |

```bash
ros2 launch robot_common_launch manipulator.launch.py robot:=piper arms:=h
ros2 launch robot_common_launch manipulator.launch.py robot:=piper type:=revo1
ros2 launch robot_common_launch manipulator.launch.py robot:=piper type:=revo2
ros2 launch robot_common_launch manipulator.launch.py robot:=piper xacro_camera:=dabai
```

### 2.1 Component

`component.xacro` 只出单件（相机 TF / Dabai 支架 + 相机，或止于 `tcp` 的裸臂），不含夹爪 / Revo1 / Revo2。

| 部件 | 命令 |
|------|------|
| 腕部相机 TF（默认） | `ros2 launch robot_common_launch component.launch.py robot:=piper` |
| Dabai 支架 + Orbbec 相机 | `type:=dabai` |
| 标准 Piper 裸臂 | `type:=piper_ee` |
| Piper H / L / X 裸臂 | `type:=h_ee` / `l_ee` / `x_ee` |

```bash
ros2 launch robot_common_launch component.launch.py robot:=piper
ros2 launch robot_common_launch component.launch.py robot:=piper type:=dabai
ros2 launch robot_common_launch component.launch.py robot:=piper type:=piper_ee
ros2 launch robot_common_launch component.launch.py robot:=piper type:=h_ee
ros2 launch robot_common_launch component.launch.py robot:=piper type:=l_ee
ros2 launch robot_common_launch component.launch.py robot:=piper type:=x_ee
```

## 3. OCS2 Demo

### 3.1 Official OCS2 Mobile Manipulator Demo

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch manipulator_ocs2.launch.py robot_name:=piper
```

### 3.2 OCS2 Arm Controller Demo

* Gazebo
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch ocs2_arm_controller demo.launch.py robot:=piper hardware:=gz world:=warehouse
  ```

* Isaac Sim
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch ocs2_arm_controller demo.launch.py robot:=piper hardware:=isaac
  ```
