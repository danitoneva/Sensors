"""
Tests for photoelectric sensor.
"""
import pytest
from sensors.photoelectric_sensor import PhotoelectricSensor


class PhotoelectricSensorRange:
    MIN_DISTANCE_NM = 0.1
    MAX_DISTANCE_NM = 30


class PhotoelectricSensorMode:
    MODE_TRUE = True
    MODE_FALSE = False


class PhotoelectricSensorNames:
    SENSOR_S1 = "S1"
    SENSOR_S2 = "S2"

class TestPhotoelectricSensorS1():
    """
    Class for testing photoelectric sensors.
    """
    def test_photoelectric_sensor_in_range(self):
        valid_midle_range_distance = 15
        sensor = PhotoelectricSensor(PhotoelectricSensorNames.SENSOR_S1,
                                    PhotoelectricSensorRange.MIN_DISTANCE_NM,
                                    PhotoelectricSensorRange.MAX_DISTANCE_NM, 
                                    valid_midle_range_distance, 
                                    PhotoelectricSensorMode.MODE_TRUE)
        assert sensor.validate()

    def test_photoelectric_sensor_min(self):
        valid_min_range_distance = 0.1
        sensor = PhotoelectricSensor(PhotoelectricSensorNames.SENSOR_S2,
                                    PhotoelectricSensorRange.MIN_DISTANCE_NM,
                                    PhotoelectricSensorRange.MAX_DISTANCE_NM, 
                                    valid_min_range_distance, 
                                    PhotoelectricSensorMode.MODE_TRUE)
        assert sensor.validate()

    def test_photoelectric_sensor_max(self):
        valid_max_range_distance = 30
        sensor = PhotoelectricSensor(PhotoelectricSensorNames.SENSOR_S1,
                                    PhotoelectricSensorRange.MIN_DISTANCE_NM,
                                    PhotoelectricSensorRange.MAX_DISTANCE_NM, 
                                    valid_max_range_distance, 
                                    PhotoelectricSensorMode.MODE_TRUE)
        assert sensor.validate()

    def test_photoelectric_sensor_mode(self):
        valid_midle_range_distance = 15
        PhotoelectricSensor(PhotoelectricSensorNames.SENSOR_S2,
                            PhotoelectricSensorRange.MIN_DISTANCE_NM,
                            PhotoelectricSensorRange.MAX_DISTANCE_NM, 
                            valid_midle_range_distance, 
                            PhotoelectricSensorMode.MODE_FALSE)
        raise ValueError("The sensor must be in the on state.")

    def test_photoelectric_sensor_less(self):
        unvalid_under_min_distance = 0
        PhotoelectricSensor(PhotoelectricSensorNames.SENSOR_S1,
                            PhotoelectricSensorRange.MIN_DISTANCE_NM,
                            PhotoelectricSensorRange.MAX_DISTANCE_NM, 
                            unvalid_under_min_distance, 
                            PhotoelectricSensorMode.MODE_TRUE)
        raise ValueError("The value is below the limit.")

    def test_photoelectric_sensor_more(self):
        unvalid_over_min_distance = 31
        PhotoelectricSensor(PhotoelectricSensorNames.SENSOR_S2,
                            PhotoelectricSensorRange.MIN_DISTANCE_NM,
                            PhotoelectricSensorRange.MAX_DISTANCE_NM, 
                            unvalid_over_min_distance, 
                            PhotoelectricSensorMode.MODE_TRUE)
        raise ValueError("The value is over the limit.")

if __name__ == '__main__':
    pytest.main()
