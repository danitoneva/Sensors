"""
Tests for inductive sensor.
"""
import pytest
from sensors.inductive_sensor import InductiveSensor


class TestInductiveSensor():
    """
    Class for testing inductive sensors.
    """
    def test_inductive_sensor_in_range(self):
        sensor = InductiveSensor("S1", 5.0, 7.0, 6.0, "aluminium")
        assert sensor.validate()

    def test_inductive_sensor_min(self):
        sensor = InductiveSensor("S2", 5.0, 7.0, 5.0, "iron")
        assert sensor.validate()

    def test_inductive_sensor_max(self):
        sensor = InductiveSensor("S3", 5.0, 7.0, 7.0, "copper")
        assert sensor.validate()

    def test_inductive_sensor_material(self):
        InductiveSensor("S4", 5.0, 7.0, 7.0, "wood")
        raise ValueError("The material is not metal.")

    def test_inductive_sensor_less(self):
        InductiveSensor("S5", 5.0, 7.0, 4.0, "aluminium")
        raise ValueError("Тhe value is below the limit.")

    def test_inductive_sensor_more(self):
        InductiveSensor("S6", 5.0, 7.0, 8.0, "aluminium")
        raise ValueError("Тhe value is over the limit.")

if __name__ == '__main__':
    pytest.main()
