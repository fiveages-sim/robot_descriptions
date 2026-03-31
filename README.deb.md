# Debian 包使用说明

本文档说明 deb 包的依赖关系、安装顺序，以及当前的安装方式。

## 包列表（核心 4 个 + 可选 1 个）

**整条描述 + 控制栈**一般只需要下面 4 个包（与 `robot-descriptions-jazzy-robots` 的 `Depends` 一致）：

- `ocs2-ros2-jazzy-mobile-manipulator`
- `robot-descriptions-jazzy-common`
- `arms-ros2-control-jazzy`
- `robot-descriptions-jazzy-robots`

**第 5 个（可选）** — 仅在使用依赖 `gripper_hardware_common` 的**硬件接口**（如部分 Modbus / Dobot / Marvin 等独立打的 hardware deb）时才需要，与「打 / 安装 robots 描述包」不是同一条必选依赖链：

- `arms-gripper-hardware-common-jazzy`
  - 对应源码：`arms_ros2_control` 里的 `libraries/gripper_hardware_common`，单独成 deb 是为了给多块硬件复用、且与主 `arms-ros2-control-jazzy` 解耦。

**和「夹爪」相关的常见误解**：部分机型的 `package.xml` 会对 **`adaptive_gripper_controller`** 有 `exec_depend`，该控制器已在 **`arms-ros2-control-jazzy`** 里提供，**不要求**再装 `arms-gripper-hardware-common-jazzy` 才能安装或编译 robots 描述包。`arms-gripper-hardware-common-jazzy` 提供的是**硬件侧共用库**，不是 `adaptive_gripper_controller` 本身。

**GitHub Release 上只有 gripper-common deb、没有主 bundle 时**：例如同一 tag `v1.1.0` 下只上传了 `arms_gripper_hardware_common_jazzy_*.deb`，**不能**代替 `arms-ros2-control-jazzy_*.deb`。打 **Build Robots Deb** 的 CI 会解压主 bundle 到 `/opt/ros/jazzy` 再编译，缺少主 bundle 就会失败——这是 **asset 不齐**，不是「robots 又多了一个 gripper 硬依赖」。请对该 tag 再跑 **`release-arms-ros2-control-deb`**（或手动上传 `arms-ros2-control-jazzy_*.deb`）到同一 release。

当前示例按版本 `0.1.3` 编写，对应的 deb 文件名格式分别为：

- `ocs2-ros2-jazzy-mobile-manipulator_<version>_amd64.deb`
- `robot-descriptions-jazzy-common_<version>_amd64.deb`
- `arms-ros2-control-jazzy_<version>_amd64.deb`
- `robot-descriptions-jazzy-robots_<version>_amd64.deb`
- （可选）`arms_gripper_hardware_common_jazzy_<version>_amd64.deb`

## 依赖关系

**核心 4 包**之间的运行时依赖关系如下：

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

**`arms-gripper-hardware-common-jazzy`**：通常只被**独立发布的 hardware** deb 声明依赖（主 arms 包有意不包含 `gripper_hardware_common`）。装齐核心 4 包即可满足 robots 描述包与主控制栈；若要装某款 hardware deb，再按其 `Depends` 安装本包。

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
2. 安装 `ocs2-ros2-jazzy-mobile-manipulator`
3. 安装 `robot-descriptions-jazzy-common`
4. 安装 `arms-ros2-control-jazzy`
5. 安装 `robot-descriptions-jazzy-robots`

若还要使用声明依赖 `arms-gripper-hardware-common-jazzy` 的硬件 deb，在该硬件 deb 之前安装第 5 包即可（版本需与 release 说明一致）。

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

## CI（Build Robots Deb）

拉取依赖 deb 时：**优先上游 release**，否则回退 fork；若填写了依赖 tag，同样先上游再回退。

**Build Robots Deb** 为 **手动触发**。建议打完 `common`、release 上已有 **主 arms bundle**（`arms-ros2-control-jazzy_*.deb`）后再跑。同一 tag 上若先上传了 gripper-common、后上传主 bundle，workflow 会对 arms **做多次重试**；仍失败可在 release 齐备后 **Re-run**。

子模块由 **`.github/workflows/build-robots-deb.yml`** 决定初始化与 rsync 范围（例如 W1/W2、**humanoid/Ubtech**、Tianji、quadruped 等默认不进了 deb）。**Ubtech** 仍可在主仓库 **`.gitmodules`** 里保留：本地需要时可 `git submodule update --init humanoid/Ubtech`，但 **Build Robots Deb** 不会克隆该路径也不会把它打进 robots deb。若某路径为**私有仓**导致匿名克隆报 `could not read Username for 'https://github.com'`，在仓库 **Settings → Secrets → Actions** 配置可读的 **`SUBMODULES_TOKEN`**；Fork **不继承** upstream secret。当前无 token 时 **Rokae** 子模块会被跳过，deb 不含对应描述包；要把 Tianji 等纳入打包需在 workflow 里改 init/rsync 并配 token。

## 备注

- 这几个 deb 仍然依赖 ROS 官方 apt 源中的系统包。
- 如果想查看某个 deb 安装了哪些文件，可以执行 `dpkg -L <package-name>`。
