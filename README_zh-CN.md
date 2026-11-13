# Robot Descriptions

[English](README.md) | [中文](README_zh-CN.md)

本仓库收录人形与机械臂的 URDF，均以 ROS2 包组织。多数模型已在 Blender 中重绘以便可视化。☺️

## 快速开始

```bash
# 克隆仓库
git clone https://github.com/fiveages-sim/robot_descriptions

# 进入仓库目录
cd robot_descriptions

# 初始化并更新所有子模块
git submodule init
git submodule update
```

也可一次克隆含子模块：

```bash
git clone --recursive https://github.com/fiveages-sim/robot_descriptions
```

> **说明**：本仓库使用 git 子模块。请先初始化子模块以获取全部机器人描述与公共组件。更多机器人见下方 [子模块](#子模块)。

## 轮式人形

| 品牌          | 型号                                                 | 重绘 | 图片                                                                                                                                                                                                                        |
|---------------|------------------------------------------------------|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DexForce      | [W1](humanoid/DexForce/dexfoce_w1_description/)      | 是   | <img src="humanoid/.images/dexforce_w1.png" width="180" style="object-fit: cover; object-position: center;"> <img src="humanoid/.images/dexforce_w1_pro.png" width="180" style="object-fit: cover; object-position: center;"> |
| 智元 Agibot   | [G1](humanoid/Agibot/agibot_g1_description)          | 否   | <img src="humanoid/Agibot/.images/agibot_g1.png" width="180"> <img src="humanoid/Agibot/.images/agibot_g1_omnipicker.png" width="180">                                                                                        |
| Airbot        | [MMK2](humanoid/Airbot/airbot_mmk2_description)      | 是   | <img src="humanoid/.images/airbot_mmk2.png" width="200">                                                                                                                                                                      |
| 星尘 Astribot | [S1](humanoid/Astribot/astribot_s1_description)      | 是   | <img src="humanoid/.images/astribot_s1_revo2.png" width="200"><img src="humanoid/.images/astribot_s1.png" width="200">                                                                                                        |
| 星海图 Galaxea| [R1](humanoid/Galaxea/galaxea_r1_description)        | 是   | <img src="humanoid/.images/galaxea_r1.png" width="200">                                                                                                                                                                       |
| 星海图 Galaxea| [R1 Pro](humanoid/Galaxea/galaxea_r1pro_description) | 是   | <img src="humanoid/.images/galaxea_r1_pro.png" width="200">                                                                                                                                                                   |
| 睿尔曼 Realman| [AIDAL](humanoid/Realman/aidal_description)          | 是   | <img src="humanoid/.images/realman_aidal.png" width="200">                                                                                                                                                                    |
| 睿尔曼 Realman| [RS-01](humanoid/Realman/rs01_description)           | 是   | <img src="humanoid/.images/realman_rs01.png" width="200">                                                                                                                                                                     |
| 零次方 Zerith | [H1](humanoid/Zerith/zerith_h1_description)          | 是   | <img src="humanoid/.images/zerith_h1.png" width="200">                                                                                                                                                                        |
| Unitree       | [G1-D](humanoid/Unitree/unitree_g1d_description)     | 否   |                                                                                                                                                                                                                               |
| Unitree       | [R1-D](humanoid/Unitree/unitree_r1d_description)     | 否   |                                                                                                                                                                                                                               |
| 智平方 Ai2    | [Bot2](humanoid/Ai2Robotics/ai2_bot2_description)    | 是   | <img src="humanoid/.images/ai2_bot2.png" width="200">                                                                                                                                                                         |
| 智平方 XSquare| [Quanta X1](humanoid/X2Robot/quanta_x1_description)  | 是   | <img src="humanoid/.images/x2robot_quanta_x1.png" width="200">                                                                                                                                                                |
| 千寻 Spirit AI| [MOZ 1](humanoid/SpiritAI/moz1_description)          | 是   | <img src="humanoid/.images/spiritai_moz1.png" width="200">                                                                                                                                                                    |
| 珞石 Rokae    | [INEX](humanoid/Rokae/rokae_inex_description/)       | 是   | <img src="humanoid/.images/rokae_inex.png" width="200"> |

## 移动操作臂

| 品牌           | 型号                                                        | 重绘 | 图片                                                                                                                                                                                                                                                  |
|----------------|-------------------------------------------------------------|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 星海图 Galaxea | [R1 Lite](manipulator/Galaxea/galaxea_r1lite_description)   | 是   | <img src="manipulator/.images/galaxea_r1lite_x.png" width="200" style="object-fit: cover; object-position: center;">     <img src="manipulator/.images/galaxea_r1lite_y.png" width="200" style="object-fit: cover; object-position: center;">           |
| 松灵 AgileX    | [Cobot Magic V1](manipulator/AgileX/cobot_magic_v1_description) | 是 | <img src="manipulator/.images/agilex_aloha_v1.png" width="220"> <img src="manipulator/.images/agilex_aloha_v1_x5.png" width="220">                                                                                                                  |
| 松灵 AgileX    | [Split Aloha](manipulator/AgileX/split_aloha_description)   | 是   | <img src="manipulator/.images/agilex_split_aloha.png" width="180">                                                                                                                  |
| 松灵 AgileX    | [Cobot Magic V2](manipulator/AgileX/cobot_magic_v2_description) | 是 | <img src="manipulator/.images/cobot_magic_v2.png" width="260">                                                                                                                  |
| SIGRobotics    | [Lekiwi](manipulator/LeRobot/lekiwi_description)            | 是   | <img src="manipulator/.images/lekiwi_100.png" width="200" height="150" style="object-fit: cover; object-position: center;"> <img src="manipulator/.images/lekiwi_101.png" width="200" height="150" style="object-fit: cover; object-position: center;"> |

## 机械臂

| 品牌           | 型号                                                     | 重绘 | 图片                                                                                                                                                                                                                                                                                                                                                                                |
|----------------|----------------------------------------------------------|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TheRobotStudio | [SO-ARM](manipulator/LeRobot/so_arm_description)         | 是   | <img src="manipulator/.images/so100.png" width="200" height="150" style="object-fit: cover; object-position: center;"> <img src="manipulator/.images/so101.png" width="200" height="150" style="object-fit: cover; object-position: center;">                                                                                                                                         |
| 松灵 AgileX    | [Piper](manipulator/AgileX/piper_description)            | 是   | <img src="manipulator/.images/agilex_piper.png" width="200" height="120" style="object-fit: cover; object-position: center;">                                                                                                                    |
| 松灵 AgileX    | [Nero](manipulator/AgileX/nero_description)              | 否   |                                                                                                                                                                                                                                                    |
| 松灵 AgileX    | [Open Nero](manipulator/AgileX/open_nero_description)    | 是   | <img src="manipulator/.images/open_nero.png" width="260">                                                                                                                          |
| 星海图 Galaxea | [A1/A1X/A1Y](manipulator/Galaxea/galaxea_a1_description) | 是   | <img src="manipulator/.images/galaxea_a1.png" width="200" height="120" style="object-fit: cover; object-position: center;"> <img src="manipulator/.images/galaxea_a1x.png" width="200" height="120" style="object-fit: cover; object-position: center;"> <img src="manipulator/.images/galaxea_a1y.png" width="200" height="120" style="object-fit: cover; object-position: center;"> |
| Airbots        | [Play](manipulator/Airbot/airbot_play_description)       | 是   | <img src="manipulator/.images/airbot_play.png" width="200">                                                                                                                                                                                                                                                                                                                           |
| 睿尔曼 Realman | [RM65&75](manipulator/Realman/rm75_description)          | 是   | <img src="manipulator/.images/realman_rm65.png" width="200">                                                                                                                                                                                                                                                                                                                          |
| 艾利特 Elite   | [EC Series](manipulator/Elite/elite_ec_description)      | 是   | <img src="manipulator/.images/elite_ec66.png" width="200">                                                                                                                                                                                                                                                                                                                            |
| OpenArm        | [OpenArm](manipulator/OpenArm/openarm_description)       | 是   | <img src="manipulator/.images/openarm_single.png" width="200" style="object-fit: cover; object-position: center;">     <img src="manipulator/.images/openarm_bimanual.png" width="200" style="object-fit: cover; object-position: center;">                                                                                                                                           |

## 足式人形

| 品牌              | 型号                                                   | 重绘 | 图片                                                                                                                                                                                                                  |
|-------------------|--------------------------------------------------------|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Unitree           | [G1](humanoid/Unitree/unitree_g1_description)          | 是   | <img src="humanoid/.images/unitree_g1.png" width="160">                                                                                                                                                                 |
| 智元 Agibot       | [A2](humanoid/Agibot/agibot_a2_description)            | 是   | <img src="humanoid/Agibot/.images/agibot_a2.png" width="220">                                                                                                                                                                 |
| Booster           | [T1](humanoid/Booster/t1_description/)                 | 是   | <img src="humanoid/.images/booster_t1.png" width="120" style="object-fit: cover; object-position: center;">                                                                                                             |
| EngineAI          | [SA01](humanoid/EngineAI/sa01_description/)            | 是   | <img src="humanoid/.images/engineai_sa01.png" width="130" style="object-fit: cover; object-position: center;">                                                                                                          |
| EngineAI          | [PM01](humanoid/EngineAI/pm01_description/)            | 是   | <img src="humanoid/.images/engineai_pm01.png" width="200" style="object-fit: cover; object-position: center;">                                                                                                          |
| 星动纪元 RobotEra | [Xbot-L](humanoid/RobotEra/robotera_xbotl_description) | 是   | <img src="humanoid/RobotEra/.images/robotera_xbotl.png" width="200">                                                                                                                                                    |
| 星动纪元 RobotEra | [STAR1](humanoid/RobotEra/robotera_star1_description)  | 是   | <img src="humanoid/RobotEra/.images/robotera_star1.png" width="200">                                                                                                                                                    |
| 星动纪元 RobotEra | [L7](humanoid/RobotEra/robotera_l7_description)        | 否   |                                                                                                                                                                                                                         |

## 子模块

本仓库用 git 子模块独立管理公共组件与部分机器人描述：

| 名称 | 路径 | 仓库 | 说明 |
|------|------|------|------|
| 公共组件 | `common` | [robot-descriptions-common](https://github.com/fiveages-sim/robot-descriptions-common) | 共享夹爪、灵巧手、相机模型与 launch 工具 |
| 四足机器人 | `quadruped` | [robot-descriptions-quadruped](https://github.com/fiveages-sim/robot-descriptions-quadruped) | 四足描述（Unitree、Deep Robotics、MagicLab、ZsiBot 等） |
| 越疆 Dobot CR5 | `manipulator/Dobot` | [robot-descriptions-dobot](https://github.com/fiveages-sim/robot-descriptions-dobot) | 6 自由度协作臂与真机集成 |
| 天机 Tianji | `manipulator/Tianji` | [robot-descriptions-tianji](https://github.com/fiveages-sim/robot-descriptions-tianji) | M6-CCS、M6-SRS、M20S-CCS、Marvin Pro 等 |
| 珞石 Rokae | `manipulator/Rokae` | [robot-descriptions-rokae](https://github.com/fiveages-sim/robot-descriptions-rokae) | AR5-SRS、AR5-CCS；轮式人形 INEX 在 `humanoid/Rokae` |
| 法奥 Fairino ART7 | `manipulator/Fairino` | [robot-descriptions-fairino](https://github.com/fiveages-sim/robot-descriptions-fairino) | ART7 双臂 |
| 方舟无限 ARX | `manipulator/ARX` | [robot-descriptions-arx](https://github.com/fiveages-sim/robot-descriptions-arx) | LIFT、X7S 人形与 X5/R5 机械臂 |
| 银河通用 Galbot | `humanoid/Galbot` | [robot-descriptions-galbot](https://github.com/fiveages-sim/robot-descriptions-galbot) | Zero、One、Charlie、Foxtrot、Golf、S1；见 [README](humanoid/Galbot/README.md) |
| 天机 Gento | `humanoid/Gento` | [robot-descriptions-gento](https://github.com/fiveages-sim/robot-descriptions-gento) | Skye、Luna；灵猴 S2 v2 + 天机 M6-CCS / M6S Lite |
| Unitree | `humanoid/Unitree` | [robot-descriptions-unitree](https://github.com/fiveages-sim/robot-descriptions-unitree) | G1（足式）、G1-D、R1-D；共享臂/头/手宏 |
| 智元 G2 | `humanoid/Agibot/agibot_g2_description` | [agibot-g2-description](https://github.com/fiveages-sim/agibot-g2-description) | G2 描述（私有子模块） |
| 高擎 Panthera HT | `manipulator/HighTorque/panthera_ht_description` | [panthera_ht_description](https://github.com/fiveages-sim/panthera_ht_description) | Panthera HT 机械臂 |

### 使用子模块

**初始化全部子模块：**
```bash
git submodule update --init --recursive
```

**初始化指定子模块：**
```bash
git submodule update --init common
git submodule update --init quadruped
git submodule update --init manipulator/Dobot
git submodule update --init manipulator/Tianji
git submodule update --init manipulator/Rokae
git submodule update --init manipulator/Fairino
git submodule update --init manipulator/ARX
git submodule update --init humanoid/Galbot
git submodule update --init humanoid/Unitree
git submodule update --init humanoid/Agibot/agibot_g2_description
git submodule update --init manipulator/HighTorque/panthera_ht_description
```

**更新子模块到最新：**
```bash
git submodule update --remote
```

各子模块仓库内有更详细的使用说明。

## 相关仓库

| 仓库 | 说明 |
|------|------|
| [arms_ros2_control](https://github.com/fiveages-sim/arms_ros2_control) | 使用本仓库配置的 ROS2 控制器与硬件接口 |
| [robot_usds](https://github.com/fiveages-sim/robot_usds) | 由本仓库 URDF 生成的 Isaac Sim USD 模型 |
