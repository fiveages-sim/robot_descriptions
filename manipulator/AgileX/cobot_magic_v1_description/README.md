# Cobot Magic V1 Description

AgileX **Cobot Magic V1**（原 Mobile Aloha V1）：Tracer 底盘 + 双臂（R5/X5）+ 固定相机架。
无腰 / 升降 / 头等身体自由度，因此没有分体控制：只有全身 WBC 与双臂 `demo`。

| 模式 | Launch | OCS2 | 控制对象 |
|------|--------|------|----------|
| Full body | `full_body.launch.py` | `task.info`（`ocs2_wheel_humanoid`） | 底盘 SE(2) + 双臂 |
| Demo | `demo.launch.py` | `task_arm.info` + `topology:=dual`（根 `arm_base`） | 仅双臂 |

Demo 规划：`robot.xacro` 在 `topology:=dual` 时只生成 `arm_base` + 双臂（不含底盘 / 相机架）。

全身 WBC 状态：`[base x,y,yaw | left×6 | right×6]`。

## 1. Build

```bash
cd ~/ros2_ws
colcon build --packages-up-to cobot_magic_v1_description --symlink-install
```

## 2. Visualize

```bash
source ~/ros2_ws/install/setup.bash
# 默认 R5（AgileX 涂装）
ros2 launch robot_common_launch manipulator.launch.py robot:=cobot_magic_v1
# X5 臂
ros2 launch robot_common_launch manipulator.launch.py robot:=cobot_magic_v1 type:=x5
```

![v1](../../.images/agilex_aloha_v1.png)
![v1 x5](../../.images/agilex_aloha_v1_x5.png)

### 2.1 Component

* Tracer 底盘
  ```bash
  ros2 launch robot_common_launch component.launch.py robot:=cobot_magic_v1
  ```
* 躯干 / 相机架
  ```bash
  ros2 launch robot_common_launch component.launch.py robot:=cobot_magic_v1 type:=body
  ```

## 3. OCS2

RMW=zenoh 时先：`ros2 run rmw_zenoh_cpp rmw_zenohd`。

### 3.1 Full body

RViz Fixed Frame = `world`（不要用 `base_link`）。

```bash
ros2 launch ocs2_arm_controller full_body.launch.py robot:=cobot_magic_v1
ros2 launch ocs2_arm_controller full_body.launch.py robot:=cobot_magic_v1 hardware:=isaac
ros2 launch ocs2_arm_controller full_body.launch.py robot:=cobot_magic_v1 type:=x5
```

### 3.2 Demo（双臂）

RViz Fixed Frame = `arm_base`。

```bash
ros2 launch ocs2_arm_controller demo.launch.py robot:=cobot_magic_v1
ros2 launch ocs2_arm_controller demo.launch.py robot:=cobot_magic_v1 hardware:=isaac
ros2 launch ocs2_arm_controller demo.launch.py robot:=cobot_magic_v1 type:=x5
```

配置见 `config/ocs2/task.info`、`task_arm.info` 与 `config/ros2_control/common.yaml`。
