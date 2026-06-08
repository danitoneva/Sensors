"""
Tests for photoelectric sensor.
"""
import pytest
from sensors.photoelectric_sensor import PhotoelectricSensor

class TestPhotoelectricSensor():
    """
    Class for testing photoelectric sensors.
    """
    def test_photoelectric_sensor_in_range(self):
        sensor = PhotoelectricSensor("S1", 0.1, 30, 15, True)
        assert sensor.validate()

    def test_photoelectric_sensor_min(self):
        sensor = PhotoelectricSensor("S2", 0.1, 30, 0.1, True)
        assert sensor.validate()

    def test_photoelectric_sensor_max(self):
        sensor = PhotoelectricSensor("S3", 0.1, 30, 30, True)
        assert sensor.validate()

    def test_photoelectric_sensor_mode(self):
        PhotoelectricSensor("S4", 0.1, 30, 15, False)
        raise ValueError("The sensor must be in the on state.")

    def test_photoelectric_sensor_less(self):
        PhotoelectricSensor("S5", 0.1, 30, 0, True)
        raise ValueError("Тhe value is below the limit.")

    def test_photoelectric_sensor_more(self):
        PhotoelectricSensor("S6", 0.1, 30, 31, True)
        raise ValueError("Тhe value is over the limit.")

if __name__ == '__main__':
    pytest.main()
