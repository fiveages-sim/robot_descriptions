# 通用机器人 OCS2 Launch 系统

[这个文件夹](../common/robot_visualize_config)包含了一个通用的机器人 OCS2 launch 系统，允许你通过传入机器人名称来自动配置所有相关路径。ROS2版本的OCS2控制框架可以在这里找到：[OCS2 ROS2](https://github.com/legubiao/ocs2_ros2)

## 🚀 功能特点

- **自动路径补全**: 根据机器人名称自动生成 URDF、配置和库文件路径
- **极简配置**: 只需指定机器人名称，所有其他配置全部自动处理
- **自动可视化**: RViz 自动启动，无需额外配置
- **错误处理**: 提供友好的错误信息和警告
- **多机器人支持**: 支持任何符合命名规范的机器人

## 📋 使用方法

### 基本用法

启动 Dobot CR5 机器人的 OCS2 控制器：
```bash
ros2 launch robot_visualize_config manipulator_ocs2.launch.py robot_name:=cr5
```

启动 ARX X5 机器人的 OCS2 控制器：
```bash
ros2 launch robot_visualize_config manipulator_ocs2.launch.py robot_name:=x5
```

### 调试模式

启用调试模式获得详细日志：
```bash
ros2 launch robot_visualize_config manipulator_ocs2.launch.py robot_name:=cr5 debug:=true
```

## 🎯 参数说明

| 参数名 | 默认值 | 描述                      |
|--------|--------|-------------------------|
| `robot_name` | `cr5` | 机器人名称 (例如: cr5, x5, r5) |
| `debug` | `false` | 是否启用调试模式                |

**注意**: RViz 会自动启动，无需额外配置。

## 📁 自动路径生成规则

系统会根据 `robot_name` 参数自动生成以下路径：

### URDF 文件路径
```
{robot_name}_description/urdf/{robot_name}.urdf
```
例如：`cr5_description/urdf/cr5.urdf`

### 任务配置文件路径
```
{robot_name}_description/config/ocs2/task.info
```
例如：`cr5_description/config/ocs2/task.info`

### 库文件夹路径
```
ocs2_mobile_manipulator/auto_generated/{robot_name}
```
例如：`ocs2_mobile_manipulator/auto_generated/cr5`

## 🔧 支持的机器人

只要机器人包遵循以下命名规范，就可以使用这个 launch 系统：

1. 机器人描述包名称：`{robot_name}_description`
2. URDF 文件位置：`{robot_name}_description/urdf/{robot_name}.urdf`
3. OCS2 配置文件位置：`{robot_name}_description/config/ocs2/task.info`

### 当前支持的机器人示例：
- `cr5` (Dobot CR5)
- `x5` (ARX X5)
- `r5` (ARX R5)
- `piper` (AgileX Piper)
- 其他符合命名规范的机器人...

## 🐛 故障排除

### 常见问题

**问题**: 找不到机器人描述包
```
❌ Error: Could not find cr5_description package
```
**解决方案**: 确保机器人描述包已正确安装并且包名遵循 `{robot_name}_description` 格式。

**问题**: 找不到配置文件
**解决方案**: 检查机器人描述包中是否存在 `config/ocs2/task.info` 文件。

### 检查包是否存在
```bash
# 检查机器人描述包
ros2 pkg list | grep cr5_description

# 检查 OCS2 包
ros2 pkg list | grep ocs2_mobile_manipulator
```