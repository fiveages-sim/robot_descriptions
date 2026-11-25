# LimX Dynamics TRON2B_DACH Description

逐际动力 TRON2B_DACH 固定基座双臂描述包，包含底座、躯干、头部和双侧可动夹爪。整机模型由 `xacro/robot.xacro` 生成。

![TRON2B_DACH 整机渲染](../../.images/tron2b_dach.png)

## Build

在已加载 ROS 2 Jazzy 的工作空间中构建。以下以 `~/ros2_ws` 为例。

```bash
cd ~/ros2_ws
colcon build --packages-up-to tron2b_dach_description --symlink-install
source install/setup.bash
```

## Visualize

```bash
ros2 launch robot_common_launch manipulator.launch.py robot:=tron2b_dach
```

### Component

用 [`component.xacro`](xacro/component.xacro) 单独展开部件：`type:=body|head|arm|gripper`，手臂和夹爪用 `name:=left|right` 与 `direction:=±1`。组件默认 `isaac:=true`（不显示 `sensor_models` 相机网格）；要看外形时传 `xacro_isaac:=false`。

```bash
xacro "$(ros2 pkg prefix --share tron2b_dach_description)/xacro/component.xacro" type:=arm name:=right direction:=-1
ros2 launch robot_common_launch component.launch.py robot:=tron2b_dach type:=head xacro_isaac:=false
```

臂/爪宏对齐 Taku/G1：`name` + `direction:=±1`，内部 `prefix="${name}_"`，关节为 `${prefix}proximal_pitch_Joint` 等；`direction` 镜像 Y、惯量交叉项与网格。相机光学系为 `head_camera`（D455）与 `body_camera`（D435）。

## Control / OCS2

先加载包含 `ocs2_arm_controller` / `ocs2_wbc_controller` 的工作空间，再加载本描述包。

### 分体控制（split_body）

双臂走 `ocs2_arm_controller`（[`task.info`](config/ocs2/task.info)），头部两关节走 `head_joint_controller`，夹爪走 adaptive gripper。

```bash
ros2 launch ocs2_arm_controller split_body.launch.py robot:=tron2b_dach
# 或 demo（同样走臂 MPC）
ros2 launch ocs2_arm_controller demo.launch.py robot:=tron2b_dach
```

### 全身控制（full_body）

`ocs2_wbc_controller` 规划双臂 + 头（[`fixed_base_tcp.info`](config/ocs2/fixed_base_tcp.info)）。无腰/升降；默认 `HM_DUAL_BODY_FREE` + `HEAD_GAZE`，`head_camera` 随双手中点注视。默认 RViz 为 [`config/rviz/fullbody.rviz`](config/rviz/fullbody.rviz)（Fixed Frame=`world`，含 WBC 面板与碰撞模型）。

```bash
ros2 launch ocs2_arm_controller full_body.launch.py robot:=tron2b_dach
```

双臂经 identity `arm_base` 挂到 `base_link`，头仍挂 `base_link`，Pinocchio 规划顺序：`[left×7 | right×7 | head×2]`，`headInputStart=14`。规划 URDF 由 launch 注入 `eef_fixed_joints:=true` 冻结夹爪关节。

### Isaac Sim

Isaac 资源导入用 `xacro_isaac:=true`（藏 `sensor_models` 的 `head_camera` / `body_camera` 网格），与运行时 `hardware:=isaac` 无关：

```bash
ros2 launch robot_common_launch manipulator.launch.py robot:=tron2b_dach xacro_isaac:=true
```

在 FaSim-Isaac 根目录运行 `./run.sh`，选择 PhysX，并打开 `robots/manipulators/LimX/TRON2/TRON2B_DACH/env/empty.usda`。点 **Play** 后：

```bash
ros2 launch ocs2_arm_controller split_body.launch.py robot:=tron2b_dach hardware:=isaac
# 或
ros2 launch ocs2_arm_controller full_body.launch.py robot:=tron2b_dach hardware:=isaac
```

### 双臂、夹爪与头部

- **双臂**：末端 `left_ee_link` / `right_ee_link`。启动后 `HOLD`，点 `HOME` 回预设姿态。
- **夹爪**：`/left_gripper_controller/target_percent`、`/right_gripper_controller/target_percent`（`0` 闭合，`1` 全开）。驱动关节 `left_gripper_joint` / `right_gripper_joint`。
- **分体头部**：`head_joint_controller` 控制 `head_yaw_Joint`、`head_pitch_Joint`。
- **全身头部**：OCS2 `HEAD_GAZE` 驱动相机随动；ATM `enable_head_control: false`。

## Model and Configuration

| 文件 | 用途 |
| --- | --- |
| [`xacro/robot.xacro`](xacro/robot.xacro) | 整机组装 |
| [`xacro/components/`](xacro/components/) | 躯干 / 头 / 臂 / 爪（臂爪用 `name` + `direction` → `prefix`） |
| [`config/ros2_control/ros2_controllers.yaml`](config/ros2_control/ros2_controllers.yaml) | 分体 / 全身控制器 |
| [`config/ocs2/task.info`](config/ocs2/task.info) | 分体双臂 MPC |
| [`config/ocs2/fixed_base_tcp.info`](config/ocs2/fixed_base_tcp.info) | 全身 WBC + HEAD_GAZE |
| [`config/ocs2/target_manager.yaml`](config/ocs2/target_manager.yaml) | ATM |
| [`config/rviz/demo_ocs2.rviz`](config/rviz/demo_ocs2.rviz) | demo / 分体 RViz |
| [`config/rviz/fullbody.rviz`](config/rviz/fullbody.rviz) | 全身 WBC RViz |

## 来源与验证

上游版权署名为 © 2024–2026 LimX Dynamics Inc.，许可证为 [Apache-2.0](LICENSE)。

模型来自逐际动力 [TRON2 官方描述仓库](https://github.com/limxdynamics/tron2-robot-description/tree/d81d2a83a3c718bc68deca4e8804fdc984dc34f7) 的 `tron2b/DACH_TRON2B`。
