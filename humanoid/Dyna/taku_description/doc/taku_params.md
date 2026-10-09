# Taku / DVT1 推断参数（不是 Dyna 官方规格）

这些数字是从公开网格、`dvt1_kin.json` 和公开参考机器人 URDF **推断**的，用来填一份能加载的 URDF。Dyna 没有发布关节限位、质量或惯量。记录轨迹只是真实限位的下界。

运动学树直接来自 `dvt1_kin.json`：根 `base_footprint` → `base_link`（原公开 kin 根名 `agv_base`，已对齐其他机器人），48 个关节（29 转动、15 固定、4 个夹爪平移）另加 `base_footprint_joint`，连杆相应多一个 `base_footprint`。零位身高 1.365 m，足迹约 0.78 × 0.60 m。

网格：限位扫描用 damping GLB（与 ego-replay GLB 是同一套 715,276 面网格）。`head_yaw_link` / `head_pitch_link` 只在较粗的 body GLB 里有网格。扫描方法：只动一个关节、其余为 0，在子树和**非父**连杆之间做表面点最近距离。父连杆在铰链处本来就贴在一起，不拿来当限位。距离掉到约 5 mm 以下视为干涉。然后把自由区间收到仍包住 `joint_ranges.csv` 观测范围的整数角度。

## 驱动关节限位

角度为度。观测范围是四段记录的并集（dryer 12 Hz + 三段 ego 15 Hz），单位 rad 见 CSV。轮关节在数据里被卷到 ±π，所以 min/max 没有意义。

| 关节 | 提议 lower | 提议 upper | 观测（下界） | 依据 |
|---|---|---|---|---|
| 四个 `*_rotate_joint` | continuous | continuous | 数据绕满 ±180° | 转轴穿过轮胎，±180° 无干涉。不做限位。 |
| 四个 `*_steering_joint` | continuous | continuous | 数据绕满 ±180° | 非父连杆间隙在 ±180° 始终约 190 mm。外壳没有打到的硬限位。Galaxea R1 转向是 ±90°，但和这套网格、这段轨迹不符，没有借用。 |
| `folding_low_joint` | −70° (−1.2217 rad) | +90° (+1.5708 rad) | −30.0° … +12.1° | −80° 时下折叠臂距后轮约 5 mm，−100° 约 1 mm；+80° 仍有 36 mm，+100° 前轮约 1 mm。取 −70° / +90°。 |
| `folding_high_joint` | 0° | +150° (+2.6180 rad) | +2.7° … +56.9° | −20° 时上臂已碰到 `base_link`（约 4 mm），0° 间隙 34 mm。正向扫到 +160° 仍 >118 mm，没有见到上止挡，+150° 只是落在已扫过的自由区间里的整数，不是测到的硬限位。 |
| `waist_pitch_joint` | −90° | +80° | −26.1° … +5.8° | −120°…+60° 对非父连杆都 >60 mm；+90° 才靠近 `folding_lower_joint_link`（约 20 mm），还没撞上。−90°/+80° 是包住观测、且明显落在自由区里的整数，不是硬止挡。 |
| `waist_yaw_joint` | −45° | +45° | −26.0° … +40.3° | ±40° 对 `folding_to_waist_link` 还有 10–13 mm，±70° 约 2 mm，躯干壳贴上下折叠臂。 |
| `head_yaw_joint` | −90° | +90° | −45.1° … +47.1° | 实机校准后保持 ±90°。`effort`/`velocity` 填 0，表示没有参考额定值。 |
| `head_pitch_joint` | −20° | +20° | +0.7° … +30.1° | 实机校准限位 ±20°（旧推断 0…+45°）。 |
| `head_roll_joint` | −15° | +15° | −4.0° … +2.3° | 实机校准限位 ±15°（旧推断 ±30°）。 |
| `*_shoulder_pitch_joint` | −150° | +90° | 右 −122°…+27°；左 −128°…+42° | −150°…+140° 单关节扫描没有非父干涉。没有外观止挡。整数区间只包住观测并留在已扫自由区里。力矩/速度借 OpenArm v1 joint1：40 N·m，16.75 rad/s。 |
| `*_shoulder_roll_joint` | −105° | 0° | 左旧零位 −11.8°…+66.8°；右 −89.5°…+12.7° | Bot2：左右同一套限位。旧左 −15°…+90°，+90° bake 后 −105°…0°；右臂镜像只在 shoulder 安装（y 与 rpy z=π），臂内 origin/limit 与左相同。 |
| `*_shoulder_yaw_joint` | −180° | +180° | 左旧 −49°…+47°；右 −45°…+65° | Bot2：左右同一套。+90° bake 进 origin；±180° 包住旧 ±90° 换算后的并集。力矩/速度用 OpenArm joint3：27 N·m，5.45 rad/s。 |
| `*_elbow_joint` | −135° | +20° | 右 −127°…−15°；左 −123°…−22° | −150° 时小臂碰到 `shoulder_roll_link`（约 5 mm），−110° 仍有 46 mm。+40° 仍自由。−135°/+20° 包住观测。OpenArm 肘是 0…+140°，零位定义不同，只借了力矩/速度（27 N·m，5.45 rad/s），没有借角度。 |
| `*_wrist_yaw_joint` | −90° | +90° | 右 −80°…+75°；左 −47°…+80° | 单关节 ±90° 没有局部止挡（最近的是远处的底盘，约 34 mm）。借 OpenArm joint5：7 N·m，20.94 rad/s。 |
| `*_wrist_pitch_joint` | −90° | +90° | 右 −42°…+52°；左 −26°…+47° | −80°…+120° 无干涉。OpenArm joint6 的 ±45° **包不住** 右腕 +52°，所以没有借它的角度。力矩/速度仍用 OpenArm joint6：7 N·m，20.94 rad/s。 |
| `*_wrist_roll_joint` | −90° | +90° | 右 −58°…+68°；左 −80°…+24° | −70° 时离 `wrist_yaw_link` 约 7 mm，可能是腕壳；+70° 时手在零位姿态下会靠近腰，那是整臂构型干涉，不是腕关节自己的挡块。±90° 包住观测。力矩/速度用 OpenArm joint7。 |
| `*_gripper_joint` | 0 | +0.0345 m | 页面给定，不是轨迹 | 标准命名（`left_gripper_joint` / `right_gripper_joint`）。驱动后指（gripperb），轴 +Y；0 合拢，+0.0345 张开。查看器 `rear = +0.0345 * grip`，`grip∈[0,1]`。力矩/速度暂借 Galaxea R1 夹爪 100 N、0.25 m/s。 |
| `*_gripper_mimic_joint` | −0.0345 m | 0 | 同上 | 前指（grippera）mimic：`q_front = -q_gripper`。两指张开量最大 0.069 m。 |

`effort` / `velocity` 凡是写了非零值，都是参考机器人 URDF 里的数，不是 Taku 的额定值。头三个关节没有可借的头，URDF 里写成 0。

## 质量与惯量

缩放：`m' = m (L'/L)^3`，对角惯量 `I' = I (m'/m) (L'/L)^2`，惯性积置 0。质心用网格顶点均值，不是体积质心。AABB 体积只用来检查缩放后的质量有没有超过「实心铝 2700 kg/m³ × 包围盒」，超过就标未知。

### 已填写

| 连杆 | 质量 kg | Ixx, Iyy, Izz (kg·m²) | 参考 |
|---|---|---|---|
| `base_link` | 13.60 | 0.226, 0.404, 0.515 | Agilex Ranger Mini `base_link` 10 kg（`split_aloha_description/xacro/components/ranger_mini.xacro`，本仓库 `feature/agilex`）。轮距比 k=1.108。Ranger 这 10 kg 本身像简化壳，不是整车。 |
| `*_wheel_steering` ×4 | 1.89 | 0.0184, 0.0184, 0.0303 | Ranger `*_steering_wheel_link` 1 kg，轴距 0.12 → 0.1484 m，k=1.237。 |
| `*_wheel_rotate` ×4 | 1.13 | 0.00078, 0.00078, 0.00124 | Ranger `*_wheel_link` 8 kg、半径 0.12 m → Taku 网格半径 0.0625 m，k=0.521。 |
| `folding_lower_joint_link` | 8.14 | 0.197, 0.193, 0.0146 | Galaxea R1 `torso_link1` 5.72 kg，关节间距 0.40 m → 0.450 m。文件 `userguide-galaxea/URDF` 的 `R1/urdf/r1_v2_1_0.urdf`。 |
| `folding_to_waist_link` | 11.81 | 0.198, 0.209, 0.0141 | R1 `torso_link2` 3.50 kg，间距 0.30 m → 0.450 m，k=1.50。 |
| `*_shoulder_pitch_link` | 2.32 | 0.00511, 0.00415, 0.00331 | OpenArm v1 `link1` 1.142 kg，L 0.067 → 0.085 m。文件 `enactic/openarm_description` `.../v1.0/urdf/example/v1.urdf`。 |
| `*_shoulder_roll_link` | 1.41 | 0.00539, 0.00565, 0.00349 | OpenArm `link2` 0.278 kg，L 0.073 → 0.125 m。 |
| `*_shoulder_yaw_link` | 0.56 | 0.00146, 0.00144, 0.00022 | OpenArm `link3` 1.074 kg，L 0.157 → 0.126 m。 |
| `*_elbow_link` | 0.68 | 0.00070, 0.00057, 0.00038 | OpenArm `link4` 0.635 kg，L 0.101 → 0.103 m。 |
| `*_wrist_yaw_link` | 1.09 | 0.00109, 0.00115, 0.00083 | OpenArm `link5` 0.616 kg，L 0.126 → 0.1525 m。 |
| `*_wrist_pitch_link` | 0.21 | 3.6e-5, 4.0e-5, 4.0e-5 | OpenArm `link6` 0.475 kg，L 0.0375 → 0.0285 m。连杆很短，惯量会被缩得很小。 |
| `*_wrist_roll_link` | 2.16 | 0.00826, 0.00642, 0.00442 | OpenArm `link7` 0.466 kg，L 0.1025 → 0.171 m（到夹爪原点）。 |

左右臂用同一套数。

### 未填（没有可信类比，不猜）

- `torso_body_link`：R1 `torso_link4` 是 7.4 kg 的小法兰（惯量约 0.0015），不是这块胸壳。
- `torso_waist_pitch_link`：按 R1 `torso_link3`（3.4 kg，间距 0.10 m）缩到 0.172 m 会得到约 17 kg，超过该连杆包围盒的实心铝质量（约 16 kg），缩放失效。
- `head_yaw_link`、`head_pitch_link`、`head_roll_link`：R1 的 `zed_link` 是相机，不是头。
- `*_grippera_link`、`*_gripperb_link`：OpenArm 指 0.036 kg 小很多，按长度硬缩会超过夹爪包围盒的实心铝质量。
- 16 个固定坐标系（相机、激光、IMU、指尖、EE 目标、`torso_tracking_frame`）：无质量。

## 参考文件

- Agilex 底盘：`fiveages-sim/robot_descriptions` 分支 `feature/agilex`，`manipulator/AgileX/split_aloha_description/xacro/components/ranger_mini.xacro`
- OpenArm v1：https://github.com/enactic/openarm_description `assets/robot/openarm_v1.0/urdf/example/v1.urdf`
- Galaxea R1：https://github.com/userguide-galaxea/URDF `R1/urdf/r1_v2_1_0.urdf`

## 不要把这些当 Dyna 的真值

单关节、其余关节为 0 的扫描会漏掉「别的关节摆开之后才出现的」干涉，也会把「手臂在零位时手已经靠近腰」误看成腕关节限位（腕 roll 的正向已按这个原因放宽）。整数角度是人为收到的。质量和惯量是别的机器人按长度比缩放的，密度、电机和配重都没有。

## Lidars (sensor_models)

| Frame (link / joint) | Sensor | Pose in `base_link` (xyz, rpy) | sensor_models mesh | Visual offset in lidar frame |
|---|---|---|---|---|
| `lidar_front_left` / `lidar_front_left_frame` | RoboSense Airy | `0.292236 0.227959 0.301378`, `-0.616837 -0.603562 -1.94305` | `meshes/robosense/airy.glb` | `0 0 0.042` |
| `lidar_front_right` / `lidar_front_right_frame` | RoboSense Airy | `0.292236 -0.227959 0.301378`, `0.613474 -0.606997 1.94896` | `meshes/robosense/airy.glb` | `0 0 0.042` |
| `lidar_back` / `lidar_back_frame` | Livox MID-360 | `-0.3275 0 0.24995`, `0 0 1.5708` | `meshes/livox/mid360.glb` | `0 0 0.0683` |

Frame poses are unchanged from `dvt1_kin.json`. The front-lidar z axes point forward, outward and up, `[0.707, ±0.221, 0.672]` in `base_link`. The rear-lidar z axis points straight up.

The base GLB already contains the sensor domes. Within 9 cm of each frame, the base mesh has an axisymmetric dome centred on the frame z axis, with an xy axis offset of 1.3 mm or less. Dome tops are at z = 0.0629 m (front) and 0.0618 m (back) in the lidar frames.

Each sensor mesh was fitted to its dome by a 1-mm grid search along z, followed by a ±6 mm xy search. Front: Airy at dz = 0.042, median surface error 0.4 mm, p90 1.5 mm. Back: the kin-frame fit that matched the baked dome was dz = 0.029. That buried the real MID-360 flange in the solid rear skin (the skin is 42 mm above the kin frame; the other robots in this repo only sit ~10 mm under their deck because they have a pocket). The visual is now `0 0 0.0683`, which puts the mesh bottom (z = -0.02615) on the rear skin. xy correction is 0 for all three.

Dyna's lidar frames therefore sit at the sensor mounting face, not at the sensor_models mesh origin. The frames are kept, and only the visual is offset. Yaw about the sensor axis cannot be checked, because only the rotationally symmetric dome is visible.

sensor_models ships meshes only, no xacro macros. Every other robot in this repo inlines `<link><visual><mesh filename="file://$(find sensor_models)/meshes/...glb"/></visual></link>` plus a fixed joint. Taku follows the same pattern.


## Layout notes (arm / chassis / Dynaclaw)

- Arms follow Ai2 Bot2 / M6 CCS: one `TakuArm` macro and one mesh set under `meshes/arm/*.glb` with **no** left/right mesh `scale`. Roll/yaw +90° are baked into the same joint origins; limits and inertias are identical. `direction` only flips the shoulder_pitch mount (`y` and right `rpy z=π`).
- Swerve modules keep distinct link/joint names, but all four share `meshes/wheel_steering.glb` and `meshes/wheel_rotate.glb` (per-corner GLBs matched within ~0.2 mm).
- Dynaclaw keeps one jaw mesh, `meshes/dynaclaw/grippera_link.glb`, shared by both sides (left≈right within ~0.22 mm). `gripperb_link` uses that mesh with `rpy="0 0 pi"` (180° about z; 1 mm voxel IoU ≈ 0.998). Actuated joint is `left_/right_gripper_joint` ([0, 0.0345]); opposite jaw is `*_gripper_mimic_joint` with `multiplier="-1"`. No separate gripper base link in `dvt1_kin.json`. Standalone entry: `xacro/dynaclaw.xacro`.
- OCS2 `config/ocs2/fixed_base_tcp.info` follows FiveAges W2 / Bot2 fixed-base TCP with head in the MPC (21 DoF: body 4 + left 7 + right 7 + head 3). `config/ocs2/task.info` is the 14-DoF dual-arm file for `ocs2_arm_controller` (`topology:=dual`). `bodyFrame` is `torso_tracking_frame` (identity dummy on `torso_body_link`, ROS X-forward Z-up; zero-pose x≈−0.21 m, so `bodyRelative` uses `[−0.35, −0.05]` not Bot2 `[0, 0.25]`). `headMode` defaults to `HEAD_GAZE`; camera frame `head_camera_mid_optical_frame` (midpoint of left/right optical centers); `headMidpointGaze.muUpright` keeps camera +X world-horizontal via `head_roll` only (`uprightDeadbandDeg 2.0`, inactive inside the band). Default `collider:=simple`: folding PCA-OBB cylinders (trimmed), waist AABB box, torso Z-cylinder `r=0.100` `L=0.300`, arm cylinders (wrist_roll split), Dynaclaw jaw boxes; `selfCollision` pairs torso/arm_base ↔ elbow / wrist_yaw / wrist_roll.
