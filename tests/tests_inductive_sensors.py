"""
Tests for inductive sensor.
"""
import pytest
from sensors.inductive_sensor import InductiveSensor


class InductiveSensorRange:
    """This class is for range variables."""
    MIN_DISTANCE_NM = 5.0
    MAX_DISTANCE_NM = 7.0


class InductiveSensorMaterial:
    """This class is for material."""
    METAL_ALUMINIUM = "aluminium"
    METAL_COPPER = "copper"
    METAL_IRON = "iron"
    MATERIAL_WOOD = "wood"


class InductiveSensorNames:
    """This class is for the name of the sensors."""
    SENSOR_S1 = "S1"
    SENSOR_S2 = "S2"

class TestInductiveSensor():
    """
    Class for testing inductive sensors.
    """
    def test_inductive_sensor_in_range(self):
        valid_midle_range_distance = 6.0
        sensor = InductiveSensor(InductiveSensorNames.SENSOR_S1,
                                InductiveSensorRange.MIN_DISTANCE_NM,
                                InductiveSensorRange.MAX_DISTANCE_NM,
                                valid_midle_range_distance,
                                InductiveSensorMaterial.METAL_ALUMINIUM)
        assert sensor.validate()

    def test_inductive_sensor_min(self):
        valid_min_range_distance = 5.0
        sensor = InductiveSensor(InductiveSensorNames.SENSOR_S2,
                                InductiveSensorRange.MIN_DISTANCE_NM,
                                InductiveSensorRange.MAX_DISTANCE_NM,
                                valid_min_range_distance,
                                InductiveSensorMaterial.METAL_IRON)
        assert sensor.validate()

    def test_inductive_sensor_max(self):
        valid_max_range_distance = 7.0
        sensor = InductiveSensor(InductiveSensorNames.SENSOR_S1,
                                InductiveSensorRange.MIN_DISTANCE_NM,
                                InductiveSensorRange.MAX_DISTANCE_NM,
                                valid_max_range_distance,
                                InductiveSensorMaterial.METAL_COPPER)
        assert sensor.validate()

    def test_inductive_sensor_material(self):
        valid_midle_range_distance = 6.0
        InductiveSensor(InductiveSensorNames.SENSOR_S2,
                        InductiveSensorRange.MIN_DISTANCE_NM,
                        InductiveSensorRange.MAX_DISTANCE_NM,
                        valid_midle_range_distance,
                        InductiveSensorMaterial.MATERIAL_WOOD)
        raise ValueError("The material is not metal.")

    def test_inductive_sensor_less(self):
        unvalid_under_min_distance = 4.0
        InductiveSensor(InductiveSensorNames.SENSOR_S1,
                        InductiveSensorRange.MIN_DISTANCE_NM,
                        InductiveSensorRange.MAX_DISTANCE_NM,
                        unvalid_under_min_distance,
                        InductiveSensorMaterial.METAL_ALUMINIUM)
        raise ValueError("The value is below the limit.")

    def test_inductive_sensor_more(self):
        unvalid_over_max_distance = 8.0
        InductiveSensor(InductiveSensorNames.SENSOR_S2,
                        InductiveSensorRange.MIN_DISTANCE_NM,
                        InductiveSensorRange.MAX_DISTANCE_NM,
                        unvalid_over_max_distance,
                        InductiveSensorMaterial.METAL_ALUMINIUM)
        raise ValueError("The value is over the limit.")

if __name__ == '__main__':
    pytest.main()
