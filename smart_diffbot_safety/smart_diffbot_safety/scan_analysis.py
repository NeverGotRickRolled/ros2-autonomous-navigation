"""Pure LaserScan analysis helpers (no ROS imports)."""

import math
from typing import Optional, Sequence


def front_sector_min_range(
    ranges: Sequence[float],
    angle_min: float,
    angle_increment: float,
    range_min: float,
    range_max: float,
    half_angle: float = math.radians(30.0),
) -> Optional[float]:
    """Return the nearest valid return in a forward angular sector."""
    if not all(math.isfinite(v) for v in (
        angle_min, angle_increment, range_min, range_max, half_angle
    )):
        raise ValueError("Scan geometry and limits must be finite")
    if angle_increment == 0.0:
        raise ValueError("angle_increment must be non-zero")
    if range_min < 0.0 or range_max <= range_min:
        raise ValueError("Invalid LaserScan range limits")
    if not 0.0 < half_angle <= math.pi:
        raise ValueError("half_angle must be in (0, pi]")

    nearest = None
    for index, measured_range in enumerate(ranges):
        angle = angle_min + index * angle_increment
        normalized_angle = math.atan2(math.sin(angle), math.cos(angle))
        if abs(normalized_angle) > half_angle:
            continue
        if not math.isfinite(measured_range):
            continue
        if measured_range < range_min or measured_range > range_max:
            continue
        if nearest is None or measured_range < nearest:
            nearest = measured_range

    return nearest
