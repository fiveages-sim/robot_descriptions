# UR5e Description

FaSim 侧的 UR5e 描述包装包。运动学、网格和限位来自 ROS 2 官方 `ur_description`（`ur_type:=ur5e`），本包只补齐与现有机械臂对齐的夹爪、ros2_control 和 OCS2 臂运控配置。

关节名使用官方名称：`shoulder_pan_joint`、`shoulder_lift_joint`、`elbow_joint`、`wrist_1_joint`、`wrist_2_joint`、`wrist_3_joint`。夹爪挂在官方 `tool0` 上（法兰处的全零工具系，Z 朝外）；OCS2 规划 URDF 也会在 `tool0` 上挂载夹爪（`kinematic_only`）并生成 `eef`。不要把夹爪以单位姿直接贴到 ROS-Industrial 的 `flange`，那会和腕部差 90°。

OCS2 info（`config/ocs2/`）：

| 文件 | `eeFrame` | 用途 |
| --- | --- | --- |
| `task.info`（默认） | `eef`（夹爪尖 / gripper_base+0.15 m） | 通用 demo |
| `flange.info` | `flange`（ROS-Industrial 法兰系） | 法兰坐标系跟踪；FaSim Isaac `fiveages_acepro2` / `fiveages_action6` 通过 `ROS2ControlLaunch.inputs:infoFile=flange` 选用 |

`collider:=convex`（默认）使用官方 mesh 碰撞；OCS2 规划会注入 `collider:=simple`，臂用圆柱简化碰撞、Robotiq 用包络盒/圆柱，才能开启 `selfCollision`。

`ocs2_arm_controller` 的 `demo.launch.py` 默认 `robot` 是 `cr5`，启动 UR5e 时必须显式传入 `robot:=ur5e`。

## 1. 依赖

在 Ubuntu 24 / ROS 2 Jazzy 环境中先安装官方描述包：

```bash
sudo apt install ros-jazzy-ur-description
```

工作空间里还需要已有的 `robot_common_launch`、`robotiq_gripper_description` 和 `ocs2_arm_controller`。

## 2. 构建

```bash
cd ~/ros2_ws
colcon build --packages-up-to ur5e_description --symlink-install
source install/setup.bash
```

## 3. 可视化

无夹爪：

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch manipulator.launch.py robot:=ur5e
```

带 Robotiq 2F-85：

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch manipulator.launch.py robot:=ur5e type:=robotiq85
```

## 4. OCS2 Demo

### 4.1 Official OCS2 Mobile Manipulator Demo

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch manipulator_ocs2.launch.py robot_name:=ur5e
```

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch manipulator_ocs2.launch.py robot_name:=ur5e type:=robotiq85
```

### 4.2 OCS2 Arm Controller Demo

Mock hardware：

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch ocs2_arm_controller demo.launch.py robot:=ur5e
```

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch ocs2_arm_controller demo.launch.py robot:=ur5e type:=robotiq85
```

Gazebo：

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch ocs2_arm_controller demo.launch.py robot:=ur5e type:=robotiq85 hardware:=gz
```

Isaac Sim（`isaac` 为 TopicBased 驱动，`isaac_sim` 为进程内驱动）：

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch ocs2_arm_controller demo.launch.py robot:=ur5e type:=robotiq85 hardware:=isaac
```

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch ocs2_arm_controller demo.launch.py robot:=ur5e type:=robotiq85 hardware:=isaac_sim isaac_prim_path:=/World/UR5e/root_joint
```

`ocs2_arm_controller` 的 `home_1`（以及 `interfaces.xacro` 里对应的 `initial_value`）按官方 RoboAPI Home 设计：夹爪竖直、手指朝下，离台面约 30–50 cm。仿真默认把任务系原点放在 `base_link`（Z 朝上），因此用官网标定后的笛卡尔位姿 `[-0.13, -0.46, 0.49]` m、四元数 xyzw `[0, 1, 0, 0]`（tool0 的 Z 朝下、X 沿 −X）反解，再把 `shoulder_pan_joint` 减 90°，得到 `[-0.5580, -1.6481, 1.6395, -1.5622, -1.5708, -0.5580]` rad。运动学取官方 `ur_description` UR5e；控制点是法兰中心 / `tool0`（PolyScope TCP 平移为 0）。若实际台架的任务系原点不在底座，需要重新标定，不要沿用这组关节角。

`home_2` 是原先的 UR5e ready 姿 `[0, -π/2, 0, -π/2, 0, 0]`（大臂立起、肘部折叠）。Isaac Sim 里 UR5e 的 USD 默认关节仍是全 0，和 ROS Home 是两回事。
