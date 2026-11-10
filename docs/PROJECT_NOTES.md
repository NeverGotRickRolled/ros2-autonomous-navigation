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
