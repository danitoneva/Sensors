"""
Tests for pressure sensor.
"""
import pytest
from sensors.pressure_sensor import PressureSensor

class TestPressureSensor():
    """
    Class for testing pressure sensors.
    """
    def test_pressure_sensor_in_range(self):
        sensor = PressureSensor("S1", 0.1, 1.0, 0.2, "bar")
        assert sensor.validate()

    def test_pressure_sensor_min(self):
        sensor = PressureSensor("S2", 0.1, 1.0, 0.1, "bar")
        assert sensor.validate()

    def test_pressure_sensor_max(self):
        sensor = PressureSensor("S3", 0.1, 1.0, 1.0, "bar")
        assert sensor.validate()

    def test_pressure_sensor_unit(self):
        PressureSensor("S4", 0.1, 1.0, 0.2, "mm")
        raise ValueError("The unit should be in bar.")

    def test_pressure_sensor_less(self):
        PressureSensor("S5", 0.1, 1.0, 0, "bar")
        raise ValueError("Тhe value is below the limit.")

    def test_pressure_sensor_more(self):
        PressureSensor("S6", 0.1, 1.0, 1.1, "bar")
        raise ValueError("Тhe value is over the limit.")

if __name__ == '__main__':
    pytest.main()
