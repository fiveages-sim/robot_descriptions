# Rokae Humanoids

珞石轮式人形描述包。机械臂本体仍在 [`manipulator/Rokae`](../../manipulator/Rokae/)（`ar5_ccs_description`）。

| 整机 | 包 | 说明 |
|------|-----|------|
| INEX | [`rokae_inex_description`](rokae_inex_description/) | 底盘 + 4-DOF 腰 + 2-DOF 头 + 双 AR5 CCS V2 |

```bash
ros2 launch robot_common_launch humanoid.launch.py robot:=rokae_inex collider:=simple
ros2 launch robot_common_launch component.launch.py robot:=rokae_inex type:=chassis
ros2 launch ocs2_arm_controller full_body.launch.py robot:=rokae_inex
```
