# Galbot One Description

This package contains the description files for Galbot humanoid. The origin models could be found at [RoboHanger_code](https://github.com/chen01yx/RoboHanger_code)

![galbot_one.png](../../.images/galbot_one.png)

## Build

```bash
cd ~/ros2_ws
colcon build --packages-up-to galbot_one_description --symlink-install
```

## Visualize the robot

### Full Robot

* Without End Effector:
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch humanoid.launch.py robot:=galbot_one type:=none 
  ```
* With Hitbot Gripper
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch humanoid.launch.py robot:=galbot_one collider:=simple
```

### Component

* Wheel
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch component.launch.py robot:=galbot_one type:=wheel
  ```

* Chassis
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch component.launch.py robot:=galbot_one type:=chassis
  ```
  
* Body
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch component.launch.py robot:=galbot_one type:=body
  ```

* Arms module 
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch component.launch.py robot:=galbot_one type:=arm
  ```

* Gripper Hitbot
  ```bash
  source ~/ros2_ws/install/setup.bash
  ros2 launch robot_common_launch gripper.launch.py gripper:=galbot_one
  ```

## Full-body ROS2 Control Demo


Run with gripper_hitbot:

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch ocs2_arm_controller full_body.launch.py \
  robot:=galbot_one 
```

https://github.com/user-attachments/assets/2948099b-ac18-473c-8201-79c42028e2c4

* Isaac Sim
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch ocs2_arm_controller full_body.launch.py \
  robot:=galbot_one hardware:=isaac
```

## Navigation (Isaac Sim / 底盘点云)

单路底盘雷达点云：`/chassis_lidar/point_cloud`。导航控制坐标系为 **`omni_chassis_base_link`**（见 `config/nav2/nav2_params_isaac_gt.yaml`）。请保证 `/odom` 的 `child_frame_id` 与该 link 一致，且 TF 树中存在 `map`→`odom`→`omni_chassis_base_link`。

代价地图中车体为 **半径 0.3 m 圆的 16 边形近似**（满足 MPPI `consider_footprint` 对多边形的要求）。

**仿真时间必须统一**：Isaac / ROS2 bridge 需发布 **`/clock`**；点云、`tf`、`nav_msgs/Odometry` 的 **header.stamp** 须与 `/clock` 一致（不要用主机 wall time）。若出现 `Transform data too old (map to odom)` 或 collision_monitor 报点云与节点时间差很大，优先检查上述项；launch 里 `map→world` 静态 TF 已与 `use_sim_time` 对齐。

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_common_launch navigation_isaac_gt.launch.py robot:=galbot_one
```
