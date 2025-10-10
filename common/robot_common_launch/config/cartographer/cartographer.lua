include "map_builder.lua"
include "trajectory_builder.lua"

options = {
  map_builder = MAP_BUILDER,
  trajectory_builder = TRAJECTORY_BUILDER,
  map_frame = "map",
  tracking_frame = "base_footprint",
  published_frame = "odom",
  odom_frame = "odom",
  provide_odom_frame = false,
  publish_frame_projected_to_2d = true,
  use_odometry = true,
  use_nav_sat = false,
  use_landmarks = false,
  num_laser_scans = 1,
  num_multi_echo_laser_scans = 0,
  num_subdivisions_per_laser_scan = 1,
  num_point_clouds = 0,
  lookup_transform_timeout_sec = 0.2,
  submap_publish_period_sec = 0.3,
  pose_publish_period_sec = 5e-3,
  trajectory_publish_period_sec = 30e-3,
  rangefinder_sampling_ratio = 1.,
  odometry_sampling_ratio = 0.5,
  fixed_frame_pose_sampling_ratio = 0.9,
  imu_sampling_ratio = 1.,
  landmarks_sampling_ratio = 1.,
}

MAP_BUILDER.use_trajectory_builder_2d = true

TRAJECTORY_BUILDER_2D.min_range = 0.12
TRAJECTORY_BUILDER_2D.max_range = 10.0
TRAJECTORY_BUILDER_2D.missing_data_ray_length = 3.
TRAJECTORY_BUILDER_2D.use_imu_data = false
TRAJECTORY_BUILDER_2D.use_online_correlative_scan_matching = true 
TRAJECTORY_BUILDER_2D.motion_filter.max_angle_radians = math.rad(0.1)


POSE_GRAPH.optimize_every_n_nodes = 40 -- 每90个节点进行一次优化，这也是启动回环检测的触发条件
POSE_GRAPH.constraint_builder.sampling_ratio = 0.3 -- 用于回环检测的节点的采样比率
POSE_GRAPH.constraint_builder.min_score = 0.65 -- 用于接受约束的最小分数
POSE_GRAPH.constraint_builder.global_localization_min_score = 0.7 -- 用于全局定位的最小分数
POSE_GRAPH.constraint_builder.loop_closure_translation_weight = 1.1e4 -- 回环闭合的平移权重
POSE_GRAPH.constraint_builder.loop_closure_rotation_weight = 1e5 -- 回环闭合的旋转权重
POSE_GRAPH.matcher_translation_weight = 5e2 -- 匹配的平移权重
POSE_GRAPH.matcher_rotation_weight = 1.6e3 -- 匹配的旋转权重
POSE_GRAPH.optimization_problem.huber_scale = 1e2 -- Huber损失函数的比例
POSE_GRAPH.optimization_problem.acceleration_weight = 1e3 -- 优化问题的加速度权重
POSE_GRAPH.optimization_problem.rotation_weight = 3e5 -- 优化问题的旋转权重
POSE_GRAPH.optimization_problem.local_slam_pose_translation_weight = 1e5 -- 本地SLAM姿态的平移权重
POSE_GRAPH.optimization_problem.local_slam_pose_rotation_weight = 1e5 -- 本地SLAM姿态的旋转权重
POSE_GRAPH.optimization_problem.odometry_translation_weight = 1e5 -- 里程计的平移权重
POSE_GRAPH.optimization_problem.odometry_rotation_weight = 1e5 -- 里程计的旋转权重
POSE_GRAPH.optimization_problem.fixed_frame_pose_translation_weight = 1e1 -- 固定帧姿态的平移权重
POSE_GRAPH.optimization_problem.fixed_frame_pose_rotation_weight = 1e2 -- 固定帧姿态的旋转权重
POSE_GRAPH.optimization_problem.log_solver_summary = false -- 是否记录求解器摘要

return options