# SMART diffbot safety monitor

A small, independently added ROS 2 package that analyses the forward sector of a
LaserScan stream and publishes proximity status.

## Outputs

For the default relative input topic `scan` (resolved to `/scan` for a single robot or `/<robot_name>/scan` in a namespaced launch), the node publishes:

| Topic | Type | Meaning |
|---|---|---|
| safety/front_min_range | std_msgs/msg/Float32 | Nearest valid forward range, in metres |
| safety/scan_valid | std_msgs/msg/Bool | Whether a valid forward measurement was available |
| safety/obstacle_detected | std_msgs/msg/Bool | True when the nearest valid forward measurement is at or below the configured threshold |

The default forward sector is +/- 30 degrees and the default threshold is
0.65 m. Both are configurable.

## Run

After building the workspace and sourcing its install setup:

```bash
ros2 run smart_diffbot_safety scan_safety_monitor
```

Override the input topic and threshold:

```bash
ros2 run smart_diffbot_safety scan_safety_monitor --ros-args \
  -p scan_topic:=scan \
  -p obstacle_distance:=0.65 \
  -p front_sector_half_angle:=0.523599
```

Inspect the outputs:

```bash
ros2 topic echo /safety/front_min_range
ros2 topic echo /safety/scan_valid
ros2 topic echo /safety/obstacle_detected
```

## Design notes and limitations

- The analysis helper is ROS-independent so its geometry and filtering logic can
  be unit-tested without a running robot.
- Non-finite and out-of-range returns are ignored.
- Scan angles are normalized, including scans crossing the +/- pi boundary.
- scan_valid=false means no valid return was available in the forward sector;
  consumers must not interpret that state as a clear path.
- This is a monitoring and telemetry component only. It does not publish
  velocity commands, override Nav2, implement an emergency stop, or provide a
  certified protective safety function.
- The fork now adds an optional Gazebo Fortress GPU LiDAR and bridges its scan
  to ROS 2. Runtime topic names and sensor output still need to be verified on
  the target Ubuntu / ROS 2 Humble environment.

## Validation status

Unit tests are provided in test/. They have not yet been executed in a ROS 2
Humble environment. Runtime integration with Gazebo and a real /scan topic
remains pending.
