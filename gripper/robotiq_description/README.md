# Robotiq Gripper Description

## Build

```bash
cd ~/ros2_ws
colcon build --packages-up-to robotiq_description --symlink-install
```

## Visualize the Gripper

* Robotiq 85 Gripper
    ```bash
    source ~/ros2_ws/install/setup.bash
    ros2 launch robot_visualize_config manipulator.launch.py robot:=robotiq
    ```
    
    <img src="../.images/robotiq85.png" width="300" height="300" style="object-fit: cover; object-position: center;"> <img src="../.images/robotiq85_collision.png" width="300" height="300" style="object-fit: cover; object-position: center;">