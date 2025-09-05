# Camera Models

* Compile
```bash
cd ~/ros2_ws
colcon build --packages-up-to camera_models --symlink-install
```

# Quadruped & Humanoid
* Visualize the robot
```bash
source ~/ros2_ws/install/setup.bash
ros2 launch robot_visualize_config visualize.launch.py
```