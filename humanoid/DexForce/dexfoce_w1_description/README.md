# Dexforce W1 Humanoid

This package contains the description files for DexForce W1 humanoid. The origin models could be found at [EmbodiChain](https://github.com/DexForce/EmbodiChain).

## 产品型号说明

- **拟人机械臂 ANTHROPOMORPHIC**
  - 模拟人体手臂关节结构设计
  - 适用于需要人机交互的场景
    ![revo1](../../.images/dexforce_w1.png)
- **工业机械臂 INDUSTRIAL**
  - 专业工业级设计
  - 适用于工业自动化生产场景
    ![pro](../../.images/dexforce_w1_pro.png)
## Build

```bash
cd ~/ros2_ws
colcon build --packages-up-to dexforce_w1_description --symlink-install
```

## Visualize the robot

To visualize and check the configuration of the robot in rviz, simply launch:

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch humanoid.launch.py robot:=dexforce_w1
```

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch humanoid.launch.py robot:=dexforce_w1 type:=pro
```

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch humanoid.launch.py robot:=dexforce_w1 type:=pro_pgc140
```

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch humanoid.launch.py robot:=dexforce_w1 type:=revo1
```

## 3. ROS2 Control Demos

### 3.1 Mock Component

* Full Body Control
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch ocs2_arm_controller demo.launch.py robot:=dexforce_w1
  ```
* Full Body Control
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch ocs2_arm_controller demo.launch.py robot:=dexforce_w1 type:=pro
  ```
* Full Body Control
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch ocs2_arm_controller demo.launch.py robot:=dexforce_w1 type:=pro_pgc140
  ```
* Full Body Control
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch ocs2_arm_controller demo.launch.py robot:=dexforce_w1 type:=revo1
  ```