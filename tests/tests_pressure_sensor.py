"""
Tests for pressure sensor.
"""
import pytest
from sensors.pressure_sensor import PressureSensor


class PressureSensorRange:
    MIN_PRESSURE = 0.1
    MAX_PRESSURE = 1.0


class PressureSensorUnit:
    UNIT_BAR = "bar"
    UNIT_NOT_BAR = "mm"


class PressureSensorNames:
    SENSOR_S1 = "S1"
    SENSOR_S2 = "S2"

class TestPressureSensor():
    """
    Class for testing pressure sensors.
    """
    def test_pressure_sensor_in_range(self):
        valid_midle_range_pressure = 0.5
        sensor = PressureSensor(PressureSensorNames.SENSOR_S1,
                                PressureSensorRange.MIN_PRESSURE,
                                PressureSensorRange.MAX_PRESSURE,
                                valid_midle_range_pressure,
                                PressureSensorUnit.UNIT_BAR)
        assert sensor.validate()

    def test_pressure_sensor_min(self):
        valid_min_range_pressure = 0.1
        sensor = PressureSensor(PressureSensorNames.SENSOR_S2,
                                PressureSensorRange.MIN_PRESSURE,
                                PressureSensorRange.MAX_PRESSURE,
                                valid_min_range_pressure,
                                PressureSensorUnit.UNIT_BAR)
        assert sensor.validate()

    def test_pressure_sensor_max(self):
        valid_max_range_pressure = 1.0
        sensor = PressureSensor(PressureSensorNames.SENSOR_S1,
                                PressureSensorRange.MIN_PRESSURE,
                                PressureSensorRange.MAX_PRESSURE,
                                valid_max_range_pressure,
                                PressureSensorUnit.UNIT_BAR)
        assert sensor.validate()

    def test_pressure_sensor_unit(self):
        valid_midle_range_pressure = 0.5
        PressureSensor(PressureSensorNames.SENSOR_S1,
                       PressureSensorRange.MIN_PRESSURE,
                       PressureSensorRange.MAX_PRESSURE,
                       valid_midle_range_pressure,
                       PressureSensorUnit.UNIT_NOT_BAR)
        raise ValueError("The unit should be in bar.")

    def test_pressure_sensor_less(self):
        unvalid_under_min_pressure = 0
        PressureSensor(PressureSensorNames.SENSOR_S2,
                       PressureSensorRange.MIN_PRESSURE,
                       PressureSensorRange.MAX_PRESSURE,
                       unvalid_under_min_pressure,
                       PressureSensorUnit.UNIT_BAR)
        raise ValueError("The value is below the limit.")

    def test_pressure_sensor_more(self):
        unvalid_over_max_pressure = 1.1
        PressureSensor(PressureSensorNames.SENSOR_S1,
                       PressureSensorRange.MIN_PRESSURE,
                       PressureSensorRange.MAX_PRESSURE,
                       unvalid_over_max_pressure,
                       PressureSensorUnit.UNIT_BAR)
        raise ValueError("The value is over the limit.")

if __name__ == '__main__':
    pytest.main()
