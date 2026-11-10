"""ROS 2 node that reports front-sector scan proximity; it does not stop the robot."""

import math

import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Bool, Float32

from smart_diffbot_safety.scan_analysis import front_sector_min_range


class ScanSafetyMonitor(Node):
    """Publish front-sector range, scan validity, and threshold state."""

    def __init__(self):
        super().__init__('scan_safety_monitor')
        self.declare_parameter('scan_topic', 'scan')
        self.declare_parameter('front_sector_half_angle', math.radians(30.0))
        self.declare_parameter('obstacle_distance', 0.65)

        self.scan_topic = self.get_parameter('scan_topic').value
        self.half_angle = float(self.get_parameter('front_sector_half_angle').value)
        self.obstacle_distance = float(self.get_parameter('obstacle_distance').value)

        if not 0.0 < self.half_angle <= math.pi:
            raise ValueError('front_sector_half_angle must be in (0, pi]')
        if not math.isfinite(self.obstacle_distance) or self.obstacle_distance <= 0.0:
            raise ValueError('obstacle_distance must be a finite positive value')

        self.range_pub = self.create_publisher(Float32, 'safety/front_min_range', 10)
        self.valid_pub = self.create_publisher(Bool, 'safety/scan_valid', 10)
        self.obstacle_pub = self.create_publisher(Bool, 'safety/obstacle_detected', 10)
        self.scan_sub = self.create_subscription(
            LaserScan, self.scan_topic, self.scan_callback, qos_profile_sensor_data
        )

        self.get_logger().info(
            f'Monitoring {self.scan_topic}; front sector +/-'
            f'{math.degrees(self.half_angle):.1f} deg; threshold '
            f'{self.obstacle_distance:.2f} m'
        )
        self.get_logger().warning(
            'Monitoring only: this node does not command, brake, or stop the robot.'
        )

    def scan_callback(self, scan: LaserScan):
        try:
            nearest = front_sector_min_range(
                scan.ranges, scan.angle_min, scan.angle_increment,
                scan.range_min, scan.range_max, self.half_angle
            )
        except ValueError as error:
            self.get_logger().error(f'Invalid LaserScan metadata: {error}')
            nearest = None

        valid_msg = Bool()
        valid_msg.data = nearest is not None
        self.valid_pub.publish(valid_msg)

        obstacle_msg = Bool()
        obstacle_msg.data = nearest is not None and nearest <= self.obstacle_distance
        self.obstacle_pub.publish(obstacle_msg)

        range_msg = Float32()
        range_msg.data = float(nearest) if nearest is not None else float('nan')
        self.range_pub.publish(range_msg)


def main(args=None):
    rclpy.init(args=args)
    node = ScanSafetyMonitor()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
