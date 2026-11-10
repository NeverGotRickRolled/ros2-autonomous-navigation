import math

import pytest

from smart_diffbot_safety.scan_analysis import front_sector_min_range


def test_returns_nearest_valid_front_measurement():
    result = front_sector_min_range(
        [2.0, 0.8, 0.4, 0.2], -0.3, 0.2, 0.1, 10.0, 0.25
    )
    assert result == pytest.approx(0.4)


def test_ignores_invalid_and_out_of_range_values():
    result = front_sector_min_range(
        [float('nan'), float('inf'), 0.05, 12.0, 1.4],
        -0.2, 0.1, 0.1, 10.0, 0.25
    )
    assert result == pytest.approx(1.4)


def test_returns_none_when_front_sector_has_no_valid_returns():
    result = front_sector_min_range(
        [1.0, 2.0], 1.0, 0.1, 0.1, 10.0, 0.2
    )
    assert result is None


def test_handles_angle_wraparound():
    result = front_sector_min_range(
        [0.3, 0.7, 2.0], 2.0 * math.pi - 0.1, 0.1,
        0.1, 10.0, 0.2
    )
    assert result == pytest.approx(0.3)


@pytest.mark.parametrize(
    'kwargs',
    [
        {'angle_increment': 0.0},
        {'range_min': -1.0},
        {'range_min': 2.0, 'range_max': 1.0},
        {'half_angle': 0.0},
        {'half_angle': math.pi + 0.1},
    ],
)
def test_rejects_invalid_scan_metadata(kwargs):
    params = {
        'ranges': [1.0], 'angle_min': 0.0, 'angle_increment': 0.1,
        'range_min': 0.1, 'range_max': 10.0, 'half_angle': 0.5,
    }
    params.update(kwargs)
    with pytest.raises(ValueError):
        front_sector_min_range(**params)
