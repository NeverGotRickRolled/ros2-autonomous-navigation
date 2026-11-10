# Upstream and license notes

## Main project

- Repository: [SaxionMechatronics/smart_diffbot](https://github.com/SaxionMechatronics/smart_diffbot)
- Fork: [NeverGotRickRolled/ros2-autonomous-navigation](https://github.com/NeverGotRickRolled/ros2-autonomous-navigation)
- Main project licence reported by GitHub: Apache-2.0
- The upstream LICENSE file is retained in this fork.

The project was developed by the SMART Research Group of Saxion University of Applied Sciences. This fork does not claim authorship of the upstream software, robot model, worlds or navigation implementation.

## Git submodules

The upstream .gitmodules file references:

| Component | Upstream |
|---|---|
| gz_ros2_control | https://github.com/ros-controls/gz_ros2_control |
| ros2_aruco | https://github.com/JMU-ROBOTICS-VIVA/ros2_aruco |
| rviz_satellite | https://github.com/blacksoul000/rviz_satellite |

These are separate projects. Check the licence and NOTICE files at the exact pinned submodule revision before redistributing them or producing a combined release. Do not assume that the main repository's licence automatically applies to submodules.

## Attribution and modifications

When distributing copies or derivative works under Apache-2.0, follow the licence conditions. In particular, retain applicable notices, include the licence, and add prominent notices to modified files. Keep upstream copyright notices intact.

## Maintainer contribution

The intended contribution in this fork is reproducible setup documentation, independent testing, and clearly identified configuration or troubleshooting notes. Any new contribution should be distinguishable from inherited upstream code.
