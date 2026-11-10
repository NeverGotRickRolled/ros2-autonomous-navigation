# Project notes

## Scope

This repository is a fork of [SaxionMechatronics/smart_diffbot](https://github.com/SaxionMechatronics/smart_diffbot). It retains the upstream robot implementation and is used to reproduce and document its ROS 2 Humble + Gazebo Fortress navigation workflow.

## Reading the architecture

The upstream package layout separates concerns:

- `smart_diffbot_bringup`: world, robot spawn and top-level launch orchestration.
- `smart_diffbot_control`: controllers and robot control integration.
- `smart_diffbot_localization`: localization nodes and configuration.
- `smart_diffbot_navigation`: Nav2 launch and parameters.
- `smart_diffbot_clients`: example goal/action clients.

A useful debugging sequence is to validate each layer separately: simulation clock and sensor topics, controller output and odometry, TF connectivity, localization, then Nav2 lifecycle and goal execution.

## Verification checklist

Record the exact date, OS image, ROS package versions, command and observed result for every check.

- [ ] Clone repository and initialize all submodules.
- [ ] Install dependencies with rosdep.
- [ ] Build with colcon.
- [ ] Start Gazebo and confirm `/clock`.
- [ ] Confirm robot state and controller topics.
- [ ] Confirm TF chain and timestamps.
- [ ] Confirm localization output.
- [ ] Start Nav2 and inspect lifecycle state.
- [ ] Send one RViz 2D navigation goal.
- [ ] Record success/failure and relevant logs.
- [ ] Repeat multi-robot launch and inspect namespaces.

Do not mark a check complete solely because a launch command returns without an immediate error. Capture evidence from the running system.

## Change log

This fork currently documents the upstream system and setup. Any future code/configuration changes should be recorded here with a reason, validation steps and a link to the corresponding commit or issue.


## Independent contribution: LaserScan safety monitor

A new package, `smart_diffbot_safety`, has been added in this fork. It contains a ROS-independent front-sector LaserScan analysis helper, a ROS 2 node that publishes nearest-front-range / scan-valid / obstacle-threshold telemetry, and unit tests for filtering and angle handling. This is a monitoring-only component; it does not command the robot or replace a certified safety system.

The upstream robot model currently has no LiDAR sensor definition and the existing Nav2 costmaps do not configure a LaserScan obstacle layer. Consequently, this package is not yet connected to a live simulated scan. Sensor modelling, Gazebo-to-ROS bridging, Nav2 costmap integration and runtime validation are follow-on tasks. The tests have not yet been run in ROS 2 Humble.

### Change log

- Added `smart_diffbot_safety` as an independent ROS 2 Python package for front-sector scan monitoring.
- Added pure-Python scan analysis tests covering nearest valid return, invalid measurements, empty sectors, angle wraparound and invalid metadata.
- Runtime build and simulation validation remain pending.
