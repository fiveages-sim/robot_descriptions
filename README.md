# Robot Descriptions

This repository contains the URDF files for humanoid and manipulator robots, all organized as ROS2 packages. Most of them have been repainted in Blender for better visualization. ☺️

## Quick Start

```bash
# Clone the repository
git clone https://github.com/fiveages-sim/robot_descriptions

# Navigate to the repository directory
cd robot_descriptions

# Initialize and update all submodules
git submodule init
git submodule update
```

Or clone the repository with all submodules in one command:

```bash
git clone --recursive https://github.com/fiveages-sim/robot_descriptions
```

> **Note**: This repository uses git submodules. Make sure to initialize them to access all robot descriptions and components. See the [Submodules](#submodules) section below for details about more robots.

## Wheel Humanoid Robots

| Brand    | Model                                                | Repaint | Images                                                                                                                                                                                                                        |
|----------|------------------------------------------------------|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DexForce | [W1](humanoid/DexForce/dexfoce_w1_description/)      | Yes     | <img src="humanoid/.images/dexforce_w1.png" width="180" style="object-fit: cover; object-position: center;"> <img src="humanoid/.images/dexforce_w1_pro.png" width="180" style="object-fit: cover; object-position: center;"> |
| Agibot   | [G1](humanoid/Agibot/agibot_g1_description)          | No      | <img src="humanoid/Agibot/.images/agibot_g1.png" width="180"> <img src="humanoid/Agibot/.images/agibot_g1_omnipicker.png" width="180">                                                                                        |
| Airbot   | [MMK2](humanoid/Airbot/airbot_mmk2_description)      | Yes     | <img src="humanoid/.images/airbot_mmk2.png" width="200">                                                                                                                                                                      |
| Astribot | [S1](humanoid/Astribot/astribot_s1_description)      | Yes     | <img src="humanoid/.images/astribot_s1_revo2.png" width="200"><img src="humanoid/.images/astribot_s1.png" width="200">                                                                                                        |
| Galaxea  | [R1](humanoid/Galaxea/galaxea_r1_description)        | Yes     | <img src="humanoid/.images/galaxea_r1_down.png" width="180">     <img src="humanoid/.images/galaxea_r1.png" width="160">                                                                                                      |
| Galaxea  | [R1 Pro](humanoid/Galaxea/galaxea_r1pro_description) | Yes     | <img src="humanoid/.images/galaxea_r1_pro.png" width="200">                                                                                                                                                                   |
| Realman  | [AIDAL](humanoid/Realman/aidal_description)          | Yes     | <img src="humanoid/.images/realman_aidal.png" width="200">                                                                                                                                                                    |
| Zerith   | [H1](humanoid/Zerith/zerith_h1_description)          | Yes     | <img src="humanoid/.images/zerith_h1.png" width="200">                                                                                                                                                                        |

## Mobile Manipulators

| Brand          | Model                                                       | Repaint | Images                                                                                                                                                                                                                                                  |
|----------------|-------------------------------------------------------------|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Galaxea        | [R1 Lite](manipulator/Galaxea/galaxea_r1lite_description)   | Yes     | <img src="manipulator/.images/galaxea_r1lite_x.png" width="200" style="object-fit: cover; object-position: center;">     <img src="manipulator/.images/galaxea_r1lite_y.png" width="200" style="object-fit: cover; object-position: center;">           |
| AgileX         | [AgileX Aloha](manipulator/AgileX/agilex_aloha_description) | Yes     | <img src="manipulator/.images/agilex_aloha_v1.png" width="220"> <img src="manipulator/.images/agilex_split_aloha.png" width="180">   <img src="manipulator/.images/agilex_aloha2.png" width="260">                                                      |
| SIGRobotics    | [Lekiwi](manipulator/LeRobot/lekiwi_description)            | Yes     | <img src="manipulator/.images/lekiwi_100.png" width="200" height="150" style="object-fit: cover; object-position: center;"> <img src="manipulator/.images/lekiwi_101.png" width="200" height="150" style="object-fit: cover; object-position: center;"> |

## Manipulators

| Brand          | Model                                                       | Repaint | Images                                                                                                                                                                                                                                                                                                                                                                                |
|----------------|-------------------------------------------------------------|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TheRobotStudio | [SO-ARM](manipulator/LeRobot/so_arm_description)            | Yes     | <img src="manipulator/.images/so100.png" width="200" height="150" style="object-fit: cover; object-position: center;"> <img src="manipulator/.images/so101.png" width="200" height="150" style="object-fit: cover; object-position: center;">                                                                                                                                         |
| AgileX         | [Piper](manipulator/AgileX/piper_description)               | Yes     | <img src="manipulator/.images/agilex_piper.png" width="200" height="120" style="object-fit: cover; object-position: center;"> <img src="manipulator/.images/agilex_piper_master.png" width="200" height="120" style="object-fit: cover; object-position: center;">                                                                                                                    |
| Galaxea        | [A1/A1X/A1Y](manipulator/Galaxea/galaxea_a1_description)    | Yes     | <img src="manipulator/.images/galaxea_a1.png" width="200" height="120" style="object-fit: cover; object-position: center;"> <img src="manipulator/.images/galaxea_a1x.png" width="200" height="120" style="object-fit: cover; object-position: center;"> <img src="manipulator/.images/galaxea_a1y.png" width="200" height="120" style="object-fit: cover; object-position: center;"> |
| Airbots        | [Play](manipulator/Airbot/airbot_play_description)          | Yes     | <img src="manipulator/.images/airbot_play.png" width="200">                                                                                                                                                                                                                                                                                                                           |
| Realman        | [RM65](manipulator/Realman/rm65_description)                | Yes     | <img src="manipulator/.images/realman_rm65.png" width="200">                                                                                                                                                                                                                                                                                                                          |
| Elite          | [EC Series](manipulator/Elite/elite_ec_description)         | Yes     | <img src="manipulator/.images/elite_ec66.png" width="200">                                                                                                                                                                                                                                                                                                                            |
| OpenArm        | [OpenArm](manipulator/OpenArm/openarm_description)          | Yes     | <img src="manipulator/.images/openarm_single.png" width="200" style="object-fit: cover; object-position: center;">     <img src="manipulator/.images/openarm_bimanual.png" width="200" style="object-fit: cover; object-position: center;">                                                                                                                                           |

## Leg Humanoid Robots

| Brand    | Model                                                | Repaint | Images                                                                                                                                                                                                                  |
|----------|------------------------------------------------------|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Unitree  | [G1](humanoid/Unitree/unitree_g1_description)        | Yes     | <img src="humanoid/.images/unitree_g1.png" width="160">                                                                                                                                                                 |
| Agibot   | [A2](humanoid/Agibot/agibot_a2_description)          | Yes     | <img src="humanoid/Agibot/.images/agibot_a2.png" width="220">                                                                                                                                                                 |
| Booster  | [T1](humanoid/Booster/t1_description/)               | Yes     | <img src="humanoid/.images/booster_t1.png" width="120" style="object-fit: cover; object-position: center;">                                                                                                             |
| EngineAI | [SA01](humanoid/EngineAI/sa01_description/)          | Yes     | <img src="humanoid/.images/engineai_sa01.png" width="130" style="object-fit: cover; object-position: center;">                                                                                                          |
| EngineAI | [PM01](humanoid/EngineAI/pm01_description/)          | Yes     | <img src="humanoid/.images/engineai_pm01.png" width="200" style="object-fit: cover; object-position: center;">                                                                                                          |
| RobotEra | [xbot](humanoid/RobotEra/xbot_description)           | Yes     | <img src="humanoid/.images/robotera_xbot.png" width="140">                                                                                                                                                              |

## Submodules

This repository uses git submodules to manage shared components and specific robot descriptions independently:

| Name | Path | Repository | Description |
|------|------|------------|-------------|
| Common Components | `common` | [robot-descriptions-common](https://github.com/fiveages-sim/robot-descriptions-common) | Shared grippers, dexterous hands, camera models, and launch utilities |
| Quadruped Robots | `quadruped` | [robot-descriptions-quadruped](https://github.com/fiveages-sim/robot-descriptions-quadruped) | Quadruped robot descriptions including Unitree, Deep Robotics, MagicLab, and ZsiBot |
| Dobot CR5 | `manipulator/Dobot` | [robot-descriptions-dobot](https://github.com/fiveages-sim/robot-descriptions-dobot) | 6-DOF collaborative robot arm with real hardware integration |
| Tianji M6 | `manipulator/Tianji` | [robot-descriptions-tianji](https://github.com/fiveages-sim/robot-descriptions-tianji) | M6-CCS and M6-SRS manipulator arms |
| Rokae AR5 | `manipulator/Rokae` | [robot-descriptions-rokae](https://github.com/fiveages-sim/robot-descriptions-rokae) | 6-DOF industrial robot arm |
| ARX Robots | `manipulator/ARX` | [robot-descriptions-arx](https://github.com/fiveages-sim/robot-descriptions-arx) | ARX robot descriptions including LIFT, X7S humanoids and X5/R5 manipulators |

### Using Submodules

**Initialize all submodules:**
```bash
git submodule update --init --recursive
```

**Initialize a specific submodule:**
```bash
# For common components
git submodule update --init common

# For quadruped robots
git submodule update --init quadruped

# For Dobot robot
git submodule update --init manipulator/Dobot

# For Tianji robot
git submodule update --init manipulator/Tianji

# For Rokae robot
git submodule update --init manipulator/Rokae

# For ARX robots
git submodule update --init manipulator/ARX
```

**Update submodules to latest version:**
```bash
git submodule update --remote
```

See the individual submodule repositories for detailed documentation and usage instructions.

## Related Repos

| Repository | Description |
|------------|-------------|
| [arms_ros2_control](https://github.com/fiveages-sim/arms_ros2_control) | ROS2 controllers and hardware interfaces that use robot configurations from this repository |
| [robot_usds](https://github.com/fiveages-sim/robot_usds) | Isaac Sim USD models built from the URDF models in this repository for simulation |
