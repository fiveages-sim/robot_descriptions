# AgileX Nero Description

7-DOF Nero 臂，宏停在 `tcp`。平行夹爪底座和手指复用 `piper_description`；7 轴法兰为本包 mesh。

## 1. Build

```bash
cd ~/ros2_ws
colcon build --packages-up-to nero_description --symlink-install
```

## 2. Visualize

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch manipulator.launch.py robot:=nero
```

默认 `collider:=simple`（连杆圆柱 / box）。看原网格碰撞：`collider:=convex`。

| 场景 | 参数 |
|------|------|
| 裸腕 | `type:=none` |
| Revo2 | `type:=revo2`（默认左手；右手 `direction:=-1` 或 `name:=right`） |
| 仅夹爪 | `ros2 launch robot_common_launch gripper.launch.py gripper:=nero` |

### 2.1 Component

止于 `tcp` 的 Nero 裸臂（不含夹爪 / Revo2）：

```bash
ros2 launch robot_common_launch component.launch.py robot:=nero
ros2 launch robot_common_launch component.launch.py robot:=nero type:=ee
```

## 3. OCS2 Demo

规划 URDF 默认 `collider:=simple`，并打开 `selfCollision`（`base_link` 对 `link3/5/7/gripper_base`）。

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch manipulator_ocs2.launch.py robot_name:=nero
ros2 launch ocs2_arm_controller demo.launch.py robot:=nero hardware:=gz
```
