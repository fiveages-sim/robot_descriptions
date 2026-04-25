# AUBO i16 使用说明

这个包提供 AUBO i16 的模型、`ros2_control` 配置、OCS2 任务文件，以及常用启动示例。

## 1. 支持的末端配置

- 不带夹爪：`type` 留空
- 气动夹爪：`type:=AG2F90-C`
- 软爪版本：`type:=AG2F90-C-Soft`

当前 `type` 会同时影响：

- 机器人模型与 TCP 定义
- `ros2_control` 控制器配置选择
- 是否自动生成 `gripper_controller`

## 2. 编译

```bash
# 在工作区根目录编译 AUBO 相关包
cd ~/ros2_ws
source /opt/ros/jazzy/setup.bash
colcon build --packages-select aubo_i16_description aubo_ros2_control robot_common_launch ocs2_arm_controller --symlink-install
source install/setup.bash
```

## 3. 常用启动命令

### 3.1 仅查看模型

```bash
# 仅看 AUBO i16 基础模型，不启动控制器
ros2 launch aubo_i16_description display.launch.py
```

### 3.2 仿真测试：mock_components

推荐先用 `mock_components` 做联调。这个模式不需要真机，也不需要 AUBO 控制柜在线。

```bash
# 无夹爪，带 RViz
ros2 launch ocs2_arm_controller demo.launch.py \
  robot:=aubo_i16 \
  hardware:=mock_components
```

```bash
# 带 AG2F90-C 夹爪，带 RViz
ros2 launch ocs2_arm_controller demo.launch.py \
  robot:=aubo_i16 \
  type:=AG2F90-C \
  hardware:=mock_components
```

```bash
# 带 AG2F90-C-Soft 软爪，带 RViz
ros2 launch ocs2_arm_controller demo.launch.py \
  robot:=aubo_i16 \
  type:=AG2F90-C-Soft \
  hardware:=mock_components
```

```bash
# 只起控制链路，不开 RViz，适合做启动检查
ros2 launch ocs2_arm_controller demo.launch.py \
  robot:=aubo_i16 \
  type:=AG2F90-C \
  hardware:=mock_components \
  launch_mode:=control_only
```

### 3.3 真机启动

真机模式下，`robot_ip` 和 `ft_topic` 会透传到 `ros2_control` 硬件插件。

```bash
# 真机，无夹爪
ros2 launch ocs2_arm_controller demo.launch.py \
  robot:=aubo_i16 \
  hardware:=real \
  robot_ip:=192.168.1.107 \
  ft_topic:=/ft_sensor_wrench \
  launch_mode:=control_only
```

```bash
# 真机，带 AG2F90-C 夹爪
ros2 launch ocs2_arm_controller demo.launch.py \
  robot:=aubo_i16 \
  type:=AG2F90-C \
  hardware:=real \
  robot_ip:=192.168.1.107 \
  ft_topic:=/ft_sensor_wrench \
  launch_mode:=control_only
```

```bash
# 真机，带 AG2F90-C-Soft 软爪
ros2 launch ocs2_arm_controller demo.launch.py \
  robot:=aubo_i16 \
  type:=AG2F90-C-Soft \
  hardware:=real \
  robot_ip:=192.168.1.107 \
  ft_topic:=/ft_sensor_wrench \
  launch_mode:=control_only
```

### 3.4 远端只看 RViz

如果机器人侧已经起好了控制器，另一台机器只想连过来看 RViz：

```bash
# 只启动 RViz 和面板，不在本机重复启动控制器
ros2 launch ocs2_arm_controller demo.launch.py \
  robot:=aubo_i16 \
  type:=AG2F90-C \
  launch_mode:=rviz_only
```

## 4. BlueDot 力传感器节点

如果真机使用外部 BlueDot 六维力传感器，可以先单独启动传感器节点，再让 AUBO 硬件插件订阅 `ft_topic`。

```bash
# 发布到 /ft_sensor_wrench，供 AUBO 硬件接口读取
ros2 run aubo_ros2_control bluedot_force_sensor_node --ros-args \
  -p sensor_ip:=192.168.0.20 \
  -p sensor_port:=49152 \
  -p publish_topic:=/ft_sensor_wrench \
  -p frame_id:=ft_sensor \
  -p poll_period_ms:=10
```

如果你改了话题名，记得在真机 launch 里同步改 `ft_topic:=...`。

## 5. 常用参数说明

### `demo.launch.py`

- `robot:=aubo_i16`
  AUBO 机器人名称，保持这个值即可。
- `type:=AG2F90-C`
  指定末端夹爪类型；留空表示不挂夹爪。
- `hardware:=mock_components`
  推荐用于仿真测试。
- `hardware:=real`
  真机模式，启用 `aubo_ros2_control/AuboHardware`。
- `launch_mode:=full`
  默认模式，启动控制链路和 RViz。
- `launch_mode:=control_only`
  只启控制，不开 RViz。
- `launch_mode:=rviz_only`
  只启 RViz，不起控制器。
- `robot_ip:=192.168.1.107`
  仅 `hardware:=real` 时生效。
- `ft_topic:=/ft_sensor_wrench`
  仅 `hardware:=real` 时生效。

## 6. 说明

- 当前主推的联调方式是 `hardware:=mock_components`。
- 真机模式下，AUBO 默认通过 `follow_mode` 连续下发关节目标，更适合 OCS2 控制器。
- 如果你只是做模型检查，优先使用 `display.launch.py`。
- 如果你要看控制链路、夹爪控制面板和 OCS2 目标交互，优先使用 `ocs2_arm_controller demo.launch.py`。
