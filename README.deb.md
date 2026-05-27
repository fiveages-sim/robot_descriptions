# Debian 包使用说明

本文档说明 4 个相关 deb 包的依赖关系、安装顺序，以及当前的安装方式。

## 包列表（ROS 2 规范命名）

| 新包名 | 旧包名（`Provides` 兼容） |
|--------|---------------------------|
| `ros-jazzy-ocs2` | `ocs2-ros2-jazzy-mobile-manipulator`、`ros-jazzy-ocs2-ros2-mobile-manipulator` |
| `ros-jazzy-robot-descriptions-common` | `robot-descriptions-jazzy-common` |
| `ros-jazzy-arms-ros2-control` | `arms-ros2-control-jazzy` |
| `ros-jazzy-robot-descriptions-robots` | `robot-descriptions-jazzy-robots` |

另有完整硬件栈包：`ros-jazzy-arms-ros2-control-full`（含 gripper / marvin / modbus / juxie）。

`ros-jazzy-ocs2` 包含 OCS2 核心库及 **全部 basic examples**（ballbot、cartpole、double_integrator、legged_robot、mobile_manipulator、quadrotor），运行时依赖含 `xterm`（示例 launch 常用独立终端）。

当前示例按版本 `0.1.3` 编写，对应的 deb 文件名格式分别为：

- `ros-jazzy-ocs2_<version>_<arch>.deb`
- `ros-jazzy-robot-descriptions-common_<version>_<arch>.deb`
- `ros-jazzy-arms-ros2-control_<version>_<arch>.deb`
- `ros-jazzy-robot-descriptions-robots_<version>_<arch>.deb`

## 依赖关系

这 4 个包之间的运行时依赖关系如下：

1. `ros-jazzy-ocs2`
   依赖：`ros-jazzy-ros-base`、`xterm`
2. `ros-jazzy-robot-descriptions-common`
   只依赖系统 ROS：`ros-jazzy-ros-base`
3. `ros-jazzy-arms-ros2-control`
   依赖：
   `ros-jazzy-ros-base`、`ros-jazzy-ocs2`、`ros-jazzy-robot-descriptions-common`
4. `ros-jazzy-robot-descriptions-robots`
   依赖：
   `ros-jazzy-ros-base`、`ros-jazzy-robot-descriptions-common`、`ros-jazzy-arms-ros2-control`

因此整体依赖链可以理解为：

`ros-jazzy-ocs2` + `ros-jazzy-robot-descriptions-common` → `ros-jazzy-arms-ros2-control` → `ros-jazzy-robot-descriptions-robots`

注意：`ros-jazzy-robot-descriptions-robots` 没有在 deb 控制文件里直接声明依赖 `ros-jazzy-ocs2`，但它会通过 `ros-jazzy-arms-ros2-control` 间接依赖它。

## 安装路径

现在这几个 deb 都安装到统一前缀：

- `/opt/ros/jazzy`

为了避免和系统包 `ros-jazzy-ros-workspace` 的公共文件冲突，打包时会剥离前缀根目录下的公共文件，例如：

- `setup.bash`
- `local_setup.bash`
- `_local_setup_util.py`

也就是说，这些 deb 会把各自的包内容安装到 `/opt/ros/jazzy` 下，但不会覆盖 ROS 自带的前缀级公共脚本。

## 推荐安装顺序

如果要把 4 个包全部安装完整，推荐顺序如下：

1. 安装系统 ROS Jazzy 基础环境
2. 安装 `ros-jazzy-ocs2`
3. 安装 `ros-jazzy-robot-descriptions-common`
4. 安装 `ros-jazzy-arms-ros2-control`（或 `ros-jazzy-arms-ros2-control-full`）
5. 安装 `ros-jazzy-robot-descriptions-robots`

例如可直接从 release 下载并安装（文件名以实际 release 为准）：

```bash
wget https://github.com/YangLuo-Bionics/ocs2_ros2/releases/download/v0.1.3/ros-jazzy-ocs2_0.1.3_amd64.deb
wget https://github.com/fiveages-sim/robot-descriptions-common/releases/download/v0.1.3/ros-jazzy-robot-descriptions-common_0.1.3_amd64.deb
wget https://github.com/fiveages-sim/arms_ros2_control/releases/download/v0.3.0/ros-jazzy-arms-ros2-control_0.3.0_amd64.deb
wget https://github.com/YangLuo-Bionics/robot_descriptions/releases/download/v0.2.0/ros-jazzy-robot-descriptions-robots_0.2.0_amd64.deb

sudo dpkg -i ros-jazzy-ocs2_0.1.3_amd64.deb
sudo dpkg -i ros-jazzy-robot-descriptions-common_0.1.3_amd64.deb
sudo dpkg -i ros-jazzy-arms-ros2-control_0.3.0_amd64.deb
sudo dpkg -i ros-jazzy-robot-descriptions-robots_0.2.0_amd64.deb
```

若 release 仍提供旧文件名，CI 下载逻辑会回退匹配；新 tag 起请使用 `ros-jazzy-ocs2_*.deb`。

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

## Workflow 中依赖包的获取策略

对于需要下载其他 deb 作为依赖的 workflow，目前采用以下策略：

- 优先从上游仓库的最新 release 获取
- 如果上游仓库没有 release，再回退到当前 fork 仓库的 release
- 如果手动指定了某个依赖 tag，则优先在上游仓库查找该 tag，找不到再回退到当前 fork 仓库
- 下载时同时匹配新、旧 deb 文件名（`ros-jazzy-ocs2` 与历史命名）

`ros-jazzy-robot-descriptions-common` 在独立仓库 [**fiveages-sim/robot-descriptions-common**](https://github.com/fiveages-sim/robot-descriptions-common) 打 `v*` tag 时由该仓 CI 构建（workflow 位于本 monorepo 的 `common/.github/workflows/build-common-deb.yml`，仅在该子模块仓生效）。

`ros-jazzy-robot-descriptions-robots` 在本 monorepo（`robot_descriptions`）通过 **Build Robots Deb** 手动触发（`workflow_dispatch`）。打完 common tag、发布好 arms 后，再在 Actions 里运行该 workflow，并填入 `v0.1.3` 等 tag 与依赖 release tag。

Fork 仓库若子模块为私有，须在 **Settings → Secrets → Actions** 中配置 `SUBMODULES_TOKEN`（对 `fiveages-sim/*` 相关子模块有读权限的 PAT），与上游仓库互不相通。

## 备注

- 这几个 deb 仍然依赖 ROS 官方 apt 源中的系统包。
- 如果想查看某个 deb 安装了哪些文件，可以执行 `dpkg -L <package-name>`。
- **不要**在 `robot_descriptions` monorepo 打 tag 期望产出 common deb；common 的 CI/CD 只在 `robot-descriptions-common` 子模块仓库中运行。
