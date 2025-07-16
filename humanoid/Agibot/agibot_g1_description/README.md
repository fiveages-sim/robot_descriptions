# Agibot G1 Description

This package contains the description files for Agibot Genie G1 humanoid. The origin models could be found at [GenieSim](https://huggingface.co/datasets/agibot-world/GenieSimAssets).

## 1. Build
```bash
cd ~/ros2_ws
colcon build --packages-up-to agibot_g1_description --symlink-install
```

## 2. Visualize the robot

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_visualize_config manipulator.launch.py robot:=agibot_g1
```
    
![G1](../../.images/agibot_g1.png)