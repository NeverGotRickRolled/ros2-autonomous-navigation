# ROS 2 Autonomous Navigation — SMART diffbot

[![ROS 2](https://img.shields.io/badge/ROS_2-Humble-22314E?logo=ros)](https://docs.ros.org/en/humble/)
[![Gazebo](https://img.shields.io/badge/Gazebo-Fortress-orange)](https://gazebosim.org/)
[![License](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](LICENSE)
[![Upstream](https://img.shields.io/badge/Upstream-SaxionMechatronics%2Fsmart__diffbot-informational)](https://github.com/SaxionMechatronics/smart_diffbot)

A ROS 2 mobile-robot simulation and navigation workspace based on **SMART diffbot**, an open-source differential-drive robot developed by the SMART Research Group at Saxion University of Applied Sciences.

This fork is being used as a learning and engineering portfolio project focused on understanding, configuring and documenting a ROS 2 navigation stack. The upstream implementation is retained; changes and experiments in this fork will be documented separately.

> **Status:** Source fork and documentation review complete. Runtime build, simulation and navigation tests have **not yet been performed in this environment**. Results will be added after testing on Ubuntu with ROS 2.

## Upstream project and attribution

- **Original project:** [SaxionMechatronics/smart_diffbot](https://github.com/SaxionMechatronics/smart_diffbot)
- **Original authors:** SMART Research Group, Saxion University of Applied Sciences
- **Original purpose:** Differential-drive robot simulation for outdoor GNSS-based navigation using Nav2
- **Original project licence:** Apache License 2.0
- **This repository:** A fork of the upstream repository. The upstream source files and their history are preserved.

Please consult the upstream project for original design decisions and canonical documentation. This repository does not claim authorship of the upstream robot, packages or navigation implementation.

## What the upstream project contains

The upstream README and source tree describe the following capabilities and packages:

- Differential-drive robot model and Gazebo simulation
- ROS 2 control integration
- Localization using GNSS-related data and `robot_localization`
- Nav2 navigation launch/configuration
- RViz visualization
- Single-robot and namespaced multi-robot simulation examples
- Example docking and line-following action clients
- Dummy hardware interface example

These are **upstream-documented capabilities**, not yet independently verified by this fork's maintainer.

## Target software environment

The upstream project documents and was tested with:

| Component | Target |
|---|---|
| Operating system | Ubuntu 22.04 |
| ROS distribution | ROS 2 Humble |
| Simulator | Gazebo Fortress (Ignition Fortress) |
| Build tool | colcon |
| Navigation | Navigation2 |
| Robot control | ros2_control / ros2_controllers |
| Localization | robot_localization |

This repository targets the versions above. Compatibility should be rechecked before using a different ROS distribution or Gazebo release.

## Repository layout

The workspace contains the upstream ROS 2 packages, including:

- `smart_diffbot_bringup/` — simulation worlds and bringup launch files
- `smart_diffbot_control/` — robot control package
- `smart_diffbot_localization/` — localization launch/configuration
- `smart_diffbot_navigation/` — navigation launch/configuration
- `smart_diffbot_clients/` — example ROS 2 clients
- `gz_ros2_control/`, `ros2_aruco/`, `rviz_satellite/` — Git submodules

The exact package contents and launch files are maintained in the source tree. Use `git submodule update --init --recursive` to retrieve the pinned submodule revisions.

## Build and run (Ubuntu + ROS 2 Humble)

Windows is fine for browsing and editing this repository, but the documented ROS 2 / Gazebo runtime workflow is intended for Ubuntu. The commands below reproduce the upstream setup; they have not yet been executed as part of this fork's verification.

### 1. Install dependencies

```bash
sudo apt update
sudo apt install \
  ros-humble-xacro \
  ros-humble-joint-state-publisher \
  ros-humble-joint-state-publisher-gui \
  ignition-fortress \
  ros-humble-ros-gz \
  ros-humble-ros2-control \
  ros-humble-ros2-controllers \
  ros-humble-tf-transformations \
  ros-humble-robot-localization \
  ros-humble-navigation2
```

The upstream project also documents Python dependencies for ArUco functionality:

```bash
pip3 install transforms3d opencv-contrib-python==4.6.0.66
```

### 2. Clone and retrieve submodules

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
git clone https://github.com/NeverGotRickRolled/ros2-autonomous-navigation.git
cd ros2-autonomous-navigation
git submodule update --init --recursive
```

### 3. Build the workspace

```bash
cd ~/ros2_ws
source /opt/ros/humble/setup.bash
rosdep install --from-paths src --ignore-src -r -y
colcon build --symlink-install
source install/setup.bash
```

### 4. Launch the example simulation

```bash
ros2 launch smart_diffbot_bringup single_robot_sim_example.launch.py
```

### 5. Explore navigation in RViz

In another terminal, source the workspace and launch the upstream RViz configuration:

```bash
source /opt/ros/humble/setup.bash
source ~/ros2_ws/install/setup.bash
ros2 launch smart_diffbot_navigation rviz.launch.py
```

Use the **2D Goal Pose** tool in RViz to set a navigation goal. Refer to the upstream README and launch files for the complete bringup sequence and other examples.

### Multi-robot simulation

The upstream source also provides a two-robot example:

```bash
ros2 launch smart_diffbot_bringup multi_robot_sim_example.launch.py
```

## Engineering review and planned workflow

This fork is intentionally keeping code changes minimal. The planned work is:

1. Reproduce the documented Humble + Fortress build.
2. Launch the single-robot world and inspect the ROS graph and TF tree.
3. Verify localization topics and transforms.
4. Send a navigation goal in RViz and record the outcome.
5. Reproduce the multi-robot example if the single-robot workflow is stable.
6. Document any fixes, configuration changes, test evidence and upstream issues.

### Verification log

| Check | Status |
|---|---|
| Fork and source attribution | Complete |
| Upstream README and package structure reviewed | Complete |
| ROS 2 Humble / Gazebo Fortress target identified | Documented upstream |
| Dependencies installed | Not yet tested |
| Colcon build | Not yet tested |
| Gazebo launch | Not yet tested |
| RViz navigation goal | Not yet tested |
| Multi-robot example | Not yet tested |

Test results will be updated with the machine/software versions, exact commands, observed outputs and screenshots. No successful runtime result is claimed until it has been reproduced.

## Licensing and third-party dependencies

The upstream repository declares **Apache License 2.0**. The upstream licence file is retained in this fork. When redistributing the project or modified source, retain applicable copyright, patent, trademark and attribution notices, include a copy of the licence, and clearly mark modified files as required by Apache-2.0.

The repository uses Git submodules. Each dependency has its own source repository and may have its own licence and notices. Review those terms independently before redistributing a combined package.

- [gz_ros2_control](https://github.com/ros-controls/gz_ros2_control)
- [ros2_aruco](https://github.com/JMU-ROBOTICS-VIVA/ros2_aruco)
- [rviz_satellite](https://github.com/blacksoul000/rviz_satellite)

This README is project documentation, not legal advice.

## References

- [SMART diffbot — upstream repository](https://github.com/SaxionMechatronics/smart_diffbot)
- [ROS 2 Humble documentation](https://docs.ros.org/en/humble/)
- [Navigation2 documentation](https://navigation.ros.org/)
- [Gazebo documentation](https://gazebosim.org/docs/)

---

Maintained as a robotics learning and portfolio project by [Manthan](https://github.com/NeverGotRickRolled). Upstream authorship remains with the original SMART diffbot contributors.
