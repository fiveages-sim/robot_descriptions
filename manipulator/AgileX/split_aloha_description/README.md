# Split Aloha Description

AgileX **Split Aloha**：Ranger Mini 全向底盘 + 升降躯干 + 双臂（`arms:=piper|h|l|x`）+ 夹爪或 BrainCo Revo1/Revo2（`type:=gripper|revo1|revo2|none`）。
有 `lifting_joint`（棱柱升降），全身 WBC 把升降与双臂一起规划；双臂 `demo` 用同包 `topology:=dual`。

| 模式 | Launch | OCS2 | 控制对象 |
|------|--------|------|----------|
| Full body | `full_body.launch.py` | `task.info`（`ocs2_wheel_humanoid` type 4） | 全向底盘 (vx, vy, omega) + 升降 + 双臂 |
| Demo | `demo.launch.py` | `task_arm.info` + `topology:=dual`（根 `arm_base`） | 仅双臂 |

Demo 规划：`robot.xacro` 在 `topology:=dual` 时只生成 `arm_base` + 双臂（不含底盘 / 升降）。`arm_base` 与 `lifting_link` 重合。

全身 WBC 状态：`[base x,y,yaw | lifting | left×6 | right×6]`。H/L/X 与标准 Piper 一样都是 6 轴、`tcp`、`left_/right_joint1–6`，OCS2 `task.info` / `task_arm.info` 不用改。默认腰部模式 `HM_DUAL_BODY_FREE`（单关节升降，不锁腰）。HOME 关节参考约束默认开启（升降 + 双臂全部纳入）。未做 `collider:=simple` 前不要开 `selfCollision`。

## 1. Build

```bash
cd ~/ros2_ws
colcon build --packages-up-to split_aloha_description --symlink-install
```

## 2. Visualize

默认：标准双 Piper + 作业夹爪 + 腕部相机 TF。

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch manipulator.launch.py robot:=split_aloha
```

![split](../../.images/agilex_split_aloha.png)

| 场景 | 参数 |
|------|------|
| Piper H / L / X | `arms:=h` / `l` / `x` |
| 裸腕 | `type:=none` |
| Revo1 | `type:=revo1`（默认关相机） |
| Revo2 | `type:=revo2`（默认关相机） |

```bash
ros2 launch robot_common_launch manipulator.launch.py robot:=split_aloha arms:=h
ros2 launch robot_common_launch manipulator.launch.py robot:=split_aloha type:=revo2
ros2 launch robot_common_launch manipulator.launch.py robot:=split_aloha arms:=x type:=revo1
```

### 2.1 Component

`component.xacro` 的 `type:=ranger_mini|body` 只出单件，与整机 EEF `type` 不是同一入口。Isaac 资源导入用 `xacro_isaac:=true`（藏 `sensor_models` 相机/雷达网格），与 `hardware:=isaac` 无关。

* Ranger Mini 底盘
  ```bash
  ros2 launch robot_common_launch component.launch.py robot:=split_aloha
  ```
* 升降躯干
  ```bash
  ros2 launch robot_common_launch component.launch.py robot:=split_aloha type:=body
  ros2 launch robot_common_launch component.launch.py robot:=split_aloha type:=body xacro_isaac:=true
  ```

## 3. OCS2

RMW=zenoh 时先：`ros2 run rmw_zenoh_cpp rmw_zenohd`。

### 3.1 Full body

RViz Fixed Frame = `world`（不要用 `base_link`）。

```bash
ros2 launch ocs2_arm_controller full_body.launch.py robot:=split_aloha
ros2 launch ocs2_arm_controller full_body.launch.py robot:=split_aloha hardware:=isaac
ros2 launch ocs2_arm_controller full_body.launch.py robot:=split_aloha type:=revo2 hardware:=isaac arms:=x
```

### 3.2 Demo（双臂）

RViz Fixed Frame = `arm_base`。

```bash
ros2 launch ocs2_arm_controller demo.launch.py robot:=split_aloha
ros2 launch ocs2_arm_controller demo.launch.py robot:=split_aloha hardware:=isaac
ros2 launch ocs2_arm_controller demo.launch.py robot:=split_aloha hardware:=gz world:=warehouse
ros2 launch ocs2_arm_controller demo.launch.py robot:=split_aloha arms:=h type:=revo1
```

配置见 `config/ocs2/task.info`、`task_arm.info` 与 `config/ros2_control/common.yaml`。Revo 手部控制器见 `brainco_description/config/ros2_control`（`type:=revo1` / `revo2` 由 EEF compose 合成）。
