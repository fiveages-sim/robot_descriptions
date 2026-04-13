# Debian 包使用说明

本文档说明 deb 包的依赖关系、安装顺序，以及当前的安装方式。

## Release 与源码仓库（对齐同一 tag，例如 `v1.1.0`）

核心 4 个 deb 分别在**各自源码仓库**的 GitHub **Releases** 上下载；**不要**指望在同一个仓库里找齐四个包。子模块拆出去的包在**子仓库**发版。

| deb 包（Jazzy） | 去哪个仓库的 Release 下载 |
|-----------------|----------------------------|
| `ros-jazzy-ocs2-ros2-mobile-manipulator` | [legubiao/ocs2_ros2](https://github.com/legubiao/ocs2_ros2) |
| `ros-jazzy-robot-descriptions-common` | [fiveages-sim/robot-descriptions-common](https://github.com/fiveages-sim/robot-descriptions-common)（主仓 `robot_descriptions` 的 **`common` 子模块**对应此仓库） |
| `ros-jazzy-arms-ros2-control` | [fiveages-sim/arms_ros2_control](https://github.com/fiveages-sim/arms_ros2_control) |
| `ros-jazzy-arms-ros2-control-pro`（可选，含全身 MPC / WBC 与私有依赖） | [fiveages-sim/ocs2-wbc-controller](https://github.com/fiveages-sim/ocs2-wbc-controller)（`arms_ros2_control` 的 **子模块**独立仓库；workflow 在该子仓 `.github/workflows/`，本地主仓路径为 `controller/ocs2_wbc_controller/.github/`） |
| `ros-jazzy-robot-descriptions-robots` | [fiveages-sim/robot_descriptions](https://github.com/fiveages-sim/robot_descriptions)（主聚合仓，仅 **robots** 这一条 deb 在此 release） |

**可选（与主 arms 同仓库、同 tag）**：`ros-jazzy-gripper-hardware-common_<version>_amd64.deb` 也在 [**fiveages-sim/arms_ros2_control**](https://github.com/fiveages-sim/arms_ros2_control) 的 **Releases** 里，与 `ros-jazzy-arms-ros2-control_*.deb` **同一 `v*`，作为另一条 asset**（由单独 workflow 上传，可能比主 bundle 早或晚几分钟）。需要装某款 **hardware** deb 且其 `Depends` 含 `gripper_hardware_common` 时再下；**不能**代替主 bundle `ros-jazzy-arms-ros2-control`。

同一套环境建议 **四个主包**的 release **同一 tag**（如 `v1.1.0`）；若装 gripper-common，**优先与主 arms 同 tag**。

## 包列表（核心 4 个 + 可选 1 个）

**整条描述 + 控制栈**一般只需要下面 4 个包（与 `ros-jazzy-robot-descriptions-robots` 的 `Depends` 一致）：

- `ros-jazzy-ocs2-ros2-mobile-manipulator`
- `ros-jazzy-robot-descriptions-common`
- `ros-jazzy-arms-ros2-control`
- `ros-jazzy-robot-descriptions-robots`

**第 5 个（可选）** — 仅在使用依赖 `gripper_hardware_common` 的**硬件接口**（如部分 Modbus / Dobot / Marvin 等独立打的 hardware deb）时才需要，与「打 / 安装 robots 描述包」不是同一条必选依赖链：

- 包名：`ros-jazzy-gripper-hardware-common`；release 上文件名一般为 **`ros-jazzy-gripper-hardware-common_<version>_amd64.deb`**（下划线）。
- **下载位置**：与主包 **`ros-jazzy-arms-ros2-control`** 相同 — [fiveages-sim/arms_ros2_control](https://github.com/fiveages-sim/arms_ros2_control) → **Releases** → 选与主 arms **同一 tag**（如 `v1.1.0`），在 assets 里单独找该 deb。
- 对应源码：`arms_ros2_control` 里的 `libraries/gripper_hardware_common`，单独成 deb 是为了给多块硬件复用、且与主 `ros-jazzy-arms-ros2-control` 解耦。

**和「夹爪」相关的常见误解（拆开两件事）**：

1. **`adaptive_gripper_controller`（软件侧控制器插件）**  
   这是 **ros2_control 里的一个控制器插件**，已经打在主包 **`ros-jazzy-arms-ros2-control`** 里。很多机型的 `package.xml` 里写的 `exec_depend` 指的是「运行时要能加载这个插件」，**只要装了主 arms deb 就满足**，和下面第 2 点**不是**同一个包。

2. **`ros-jazzy-gripper-hardware-common`（硬件侧共用库）**  
   这是给 **真实夹爪硬件驱动**（Modbus、部分 Dobot/Marvin 等 **hardware** 插件）链接用的 **C++ 共用库**。**装 / 编译 robots 描述包**一般**不需要**它；只有当你还要装**依赖 `gripper_hardware_common` 的独立 hardware deb** 时，才需要按硬件文档再装这个可选 deb。

一句话：**缺的是「仿真/主栈里用的夹爪控制器插件」→ 靠主 `ros-jazzy-arms-ros2-control`；缺的是「接真机硬件驱动要的库」→ 才考虑 `ros-jazzy-gripper-hardware-common`。**

**GitHub Release 上只有 gripper-common deb、没有主 bundle 时**：例如同一 tag `v1.1.0` 下只上传了 `ros-jazzy-gripper-hardware-common_*.deb`，**不能**代替 `ros-jazzy-arms-ros2-control_*.deb`。打 **Build Robots Deb** 的 CI 会解压主 bundle 到 `/opt/ros/jazzy` 再编译，缺少主 bundle 就会失败——这是 **asset 不齐**，不是「robots 又多了一个 gripper 硬依赖」。请对该 tag 再跑 **`release-arms-ros2-control-deb`**（或手动上传 `ros-jazzy-arms-ros2-control_*.deb`）到同一 release。

示例按 **`v1.1.0`** 对齐时，deb 文件名中的版本号一般为 `1.1.0`（与 tag 对应），格式如下：

- `ros-jazzy-ocs2-ros2-mobile-manipulator_<version>_amd64.deb`
- `ros-jazzy-robot-descriptions-common_<version>_amd64.deb`
- `ros-jazzy-arms-ros2-control_<version>_amd64.deb`
- `ros-jazzy-robot-descriptions-robots_<version>_amd64.deb`
- （可选）`ros-jazzy-gripper-hardware-common_<version>_amd64.deb` — **仍在 [arms_ros2_control](https://github.com/fiveages-sim/arms_ros2_control) 同一 release**，与主 bundle 分开发布

## 依赖关系

**核心 4 包**之间的运行时依赖关系如下：

1. `ros-jazzy-ocs2-ros2-mobile-manipulator`
   只依赖系统 ROS：`ros-jazzy-ros-base`
2. `ros-jazzy-robot-descriptions-common`
   只依赖系统 ROS：`ros-jazzy-ros-base`
3. `ros-jazzy-arms-ros2-control`
   依赖：
   `ros-jazzy-ros-base`、`ros-jazzy-ocs2-ros2-mobile-manipulator`、`ros-jazzy-robot-descriptions-common`
4. `ros-jazzy-robot-descriptions-robots`
   依赖：
   `ros-jazzy-ros-base`、`ros-jazzy-robot-descriptions-common`、`ros-jazzy-arms-ros2-control`

因此整体依赖链可以理解为：

`ros-jazzy-ocs2-ros2-mobile-manipulator` + `ros-jazzy-robot-descriptions-common` -> `ros-jazzy-arms-ros2-control` -> `ros-jazzy-robot-descriptions-robots`

注意：`ros-jazzy-robot-descriptions-robots` 没有在 deb 控制文件里直接声明依赖 `ros-jazzy-ocs2-ros2-mobile-manipulator`，但它会通过 `ros-jazzy-arms-ros2-control` 间接依赖它。

**`ros-jazzy-gripper-hardware-common`**：通常只被**独立发布的 hardware** deb 声明依赖（主 arms 包有意不包含 `gripper_hardware_common`）。装齐核心 4 包即可满足 robots 描述包与主控制栈；若要装某款 hardware deb，再按其 `Depends` 安装本包。

## 安装路径

现在这几个 deb 都安装到统一前缀：

- `/opt/ros/jazzy`

为了避免和系统包 `ros-jazzy-ros-workspace` 的公共文件冲突，打包时会剥离前缀根目录下的公共文件，例如：

- `setup.bash`
- `local_setup.bash`
- `_local_setup_util.py`

也就是说，这些 deb 会把各自的包内容安装到 `/opt/ros/jazzy` 下，但不会覆盖 ROS 自带的前缀级公共脚本。

## 推荐安装顺序

如果要把**核心 4 包**全部安装完整，推荐顺序如下：

1. 安装系统 ROS Jazzy 基础环境
2. 安装 `ros-jazzy-ocs2-ros2-mobile-manipulator`
3. 安装 `ros-jazzy-robot-descriptions-common`
4. 安装 `ros-jazzy-arms-ros2-control`
5. （可选）安装 `ros-jazzy-gripper-hardware-common` — 与主 arms **同 tag**、同 [arms_ros2_control](https://github.com/fiveages-sim/arms_ros2_control) release；要用依赖 `gripper_hardware_common` 的硬件 deb 时需要
6. 安装 `ros-jazzy-robot-descriptions-robots`

若还要使用声明依赖 `ros-jazzy-gripper-hardware-common` 的硬件 deb，在装该硬件 deb **之前**已装好 `ros-jazzy-gripper-hardware-common_*.deb`（与主 arms **同 tag**）。

例如 **`v1.1.0`**（分别从对应仓库的 **Releases** 下载）：

```bash
wget https://github.com/legubiao/ocs2_ros2/releases/download/v1.1.0/ros-jazzy-ocs2-ros2-mobile-manipulator_1.1.1_amd64.deb
wget https://github.com/fiveages-sim/robot-descriptions-common/releases/download/v1.1.0/ros-jazzy-robot-descriptions-common_1.1.0_amd64.deb
wget https://github.com/fiveages-sim/arms_ros2_control/releases/download/v1.1.0/ros-jazzy-arms-ros2-control_1.1.0_amd64.deb
wget https://github.com/fiveages-sim/robot_descriptions/releases/download/v1.1.0/ros-jazzy-robot-descriptions-robots_1.1.0_amd64.deb

sudo dpkg -i ros-jazzy-ocs2-ros2-mobile-manipulator_1.1.0_amd64.deb
sudo dpkg -i ros-jazzy-robot-descriptions-common_1.1.0_amd64.deb
sudo dpkg -i ros-jazzy-arms-ros2-control_1.1.0_amd64.deb
sudo dpkg -i ros-jazzy-robot-descriptions-robots_1.1.0_amd64.deb
```

若实际 release 上的 **文件名与版本号** 与上述不一致，以各仓库 release 页面列出的 asset 为准。

可选安装包 ros-jazzy-gripper-hardware-common
```
wget https://github.com/fiveages-sim/arms_ros2_control/releases/download/v1.1.0/ros-jazzy-gripper-hardware-common_1.1.0_amd64.deb

sudo dpkg -i ros-jazzy-gripper-hardware-common_1.1.0_amd64.deb
```

如果安装过程中提示缺少系统依赖，可执行：

```bash
sudo apt-get update
sudo apt-get install -f
```

## 使用方式

安装完成后，直接 source 系统 ROS 的环境即可：

```bash
source /opt/ros/jazzy/setup.bash
```

因为这些 deb 也安装在 `/opt/ros/jazzy` 下，所以不再需要像旧版 `/opt/fa/...` 方案那样额外 source 每个独立前缀。

## CI

- **OCS2 deb**：由 [legubiao/ocs2_ros2](https://github.com/legubiao/ocs2_ros2) 的 release workflow 发布（与 [上游 OCS2 ROS2](https://github.com/legubiao/ocs2_ros2) 同一套 release tag）。
- **`ros-jazzy-robot-descriptions-common`**：仅在子仓库 [fiveages-sim/robot-descriptions-common](https://github.com/fiveages-sim/robot-descriptions-common) 打 **`.github/workflows/build-common-deb.yml`**（`push` `v*` 或 **workflow_dispatch**）；**不要**在 [fiveages-sim/robot_descriptions](https://github.com/fiveages-sim/robot_descriptions) 主仓里找 common 的独立 deb（主仓通过子模块引用该仓库）。
- **`ros-jazzy-arms-ros2-control`** / **`ros-jazzy-gripper-hardware-common`**（可选）：均在 [fiveages-sim/arms_ros2_control](https://github.com/fiveages-sim/arms_ros2_control) **同一 release**；gripper-common 为单独 workflow 上传的第二条 asset，下载位置仍是该 tag 的 **Releases → Assets**。
- **WBC 扩展包 `ros-jazzy-arms-ros2-control-pro`（可选）**：在子仓库 [**ocs2-wbc-controller**](https://github.com/fiveages-sim/ocs2-wbc-controller) 自己的 **`.github/workflows/`** 里打 deb（workflow 已从 `arms_ros2_control` 主仓挪到该子模块仓库）。制品发布在 **ocs2-wbc-controller** 的 **Releases**；若 CI 里还要拉 [**lina_planning**](https://github.com/fiveages-sim/lina_planning) 等 **private** 依赖，应在 **跑该 workflow 的仓库**（即 **ocs2-wbc-controller**）配置 **`PRIVATE_SUBMODULES_TOKEN`**（或等价 PAT），让 `actions/checkout` 能递归拉 private 子模块；这与 **robot_descriptions** 主仓是否加 token **无必然关系**。
- **`ros-jazzy-robot-descriptions-robots`**：主仓库 **`.github/workflows/build-robots-deb.yml`**（`push` `v*` 或 **workflow_dispatch**）。CI 会从 **legubiao/ocs2_ros2**、**robot-descriptions-common**、**arms_ros2_control** 的 release **拉 deb** 解压到 `/opt/ros/jazzy` 再编译 robots；版本解析与 **fork 回退** 见 workflow 内 `PREFERRED_*` / `FALLBACK_*`。未填 `common_release_tag` 时优先与本次 robots **同名 tag** 对齐。若 workflow 需要 checkout **本仓内的 private 子模块**，仍需 **`SUBMODULES_TOKEN`**；无 token 时部分机型（如 **Rokae**）会被跳过。

## 备注

- 这几个 deb 仍然依赖 ROS 官方 apt 源中的系统包。
- 如果想查看某个 deb 安装了哪些文件，可以执行 `dpkg -L <package-name>`。
