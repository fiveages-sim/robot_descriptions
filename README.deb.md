# Debian 包使用说明

本文档说明 4 个相关 deb 包的依赖关系、安装顺序，以及当前的安装方式。

## 包列表

- `ocs2-ros2-jazzy-mobile-manipulator`
- `robot-descriptions-jazzy-common`
- `arms-ros2-control-jazzy`
- `robot-descriptions-jazzy-robots`

当前示例按版本 `0.1.3` 编写，对应的 deb 文件名格式分别为：

- `ocs2-ros2-jazzy-mobile-manipulator_<version>_amd64.deb`
- `robot-descriptions-jazzy-common_<version>_amd64.deb`
- `arms-ros2-control-jazzy_<version>_amd64.deb`
- `robot-descriptions-jazzy-robots_<version>_amd64.deb`

## 依赖关系

这 4 个包之间的运行时依赖关系如下：

1. `ocs2-ros2-jazzy-mobile-manipulator`
   只依赖系统 ROS：`ros-jazzy-ros-base`
2. `robot-descriptions-jazzy-common`
   只依赖系统 ROS：`ros-jazzy-ros-base`
3. `arms-ros2-control-jazzy`
   依赖：
   `ros-jazzy-ros-base`、`ocs2-ros2-jazzy-mobile-manipulator`、`robot-descriptions-jazzy-common`
4. `robot-descriptions-jazzy-robots`
   依赖：
   `ros-jazzy-ros-base`、`robot-descriptions-jazzy-common`、`arms-ros2-control-jazzy`

因此整体依赖链可以理解为：

`ocs2-ros2-jazzy-mobile-manipulator` + `robot-descriptions-jazzy-common` -> `arms-ros2-control-jazzy` -> `robot-descriptions-jazzy-robots`

注意：`robot-descriptions-jazzy-robots` 没有在 deb 控制文件里直接声明依赖 `ocs2-ros2-jazzy-mobile-manipulator`，但它会通过 `arms-ros2-control-jazzy` 间接依赖它。

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
2. 安装 `ocs2-ros2-jazzy-mobile-manipulator`
3. 安装 `robot-descriptions-jazzy-common`
4. 安装 `arms-ros2-control-jazzy`
5. 安装 `robot-descriptions-jazzy-robots`

例如可直接从 `YangLuo-Bionics` 的 release 下载并安装：

```bash
wget https://github.com/YangLuo-Bionics/ocs2_ros2/releases/download/v0.1.3/ocs2-ros2-jazzy-mobile-manipulator_0.1.3_amd64.deb
wget https://github.com/YangLuo-Bionics/robot_descriptions/releases/download/v0.1.3/robot-descriptions-jazzy-common_0.1.3_amd64.deb
wget https://github.com/YangLuo-Bionics/arms_ros2_control/releases/download/v0.3.0/arms-ros2-control-jazzy_0.3.0_amd64.deb
wget https://github.com/YangLuo-Bionics/robot_descriptions/releases/download/v0.2.0/robot-descriptions-jazzy-robots_0.2.0_amd64.deb

sudo dpkg -i ocs2-ros2-jazzy-mobile-manipulator_0.1.3_amd64.deb
sudo dpkg -i robot-descriptions-jazzy-common_0.1.3_amd64.deb
sudo dpkg -i arms-ros2-control-jazzy_0.3.0_amd64.deb
sudo dpkg -i robot-descriptions-jazzy-robots_0.2.0_amd64.deb
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

## Workflow 中依赖包的获取策略

对于需要下载其他 deb 作为依赖的 workflow，目前采用以下策略：

- 优先从上游仓库的最新 release 获取
- 如果上游仓库没有 release，再回退到当前 fork 仓库的 release
- 如果手动指定了某个依赖 tag，则优先在上游仓库查找该 tag，找不到再回退到当前 fork 仓库

`robot-descriptions-jazzy-robots` 的 CI 仅支持 **手动触发**（`workflow_dispatch`），避免与 `common` 打同一 `v*` tag 时两条 workflow 一起跑。打完 `common`、发布好 `arms` 后，再在 Actions 里单独运行 **Build Robots Deb**，并填入 `v0.1.3` 等 tag 与依赖 release tag。

Fork 仓库若子模块为私有，须在 **Settings → Secrets → Actions** 中配置 `SUBMODULES_TOKEN`（对 `fiveages-sim/*` 相关子模块有读权限的 PAT），与上游仓库互不相通。

## 备注

- 这几个 deb 仍然依赖 ROS 官方 apt 源中的系统包。
- 如果想查看某个 deb 安装了哪些文件，可以执行 `dpkg -L <package-name>`。
