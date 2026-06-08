"""This module is for an photoelectric sensor."""
from sensors.sensors_base import Sensors


class PhotoelectricSensor(Sensors):
    """
    Photoelectric sensor class
    """

    def __init__(self, name: str,  min_distance_mm: float,
                 max_distance_mm: float, current_distance_mm: float, mode: bool):
        """
        Creates the object  photoelectric sensor.
        """
        super().__init__(name)
        self.min_distance_mm = min_distance_mm
        self.max_distance_mm = max_distance_mm
        self.current_distance_mm = current_distance_mm
        self.mode = mode

    def read_value(self) -> float:
        """
        Returns the value of the current distance.

        :return: number
        """
        return self.current_distance_mm

    def validate_distance(self) -> bool:
        """
        Checks whether the current distance falls within the range.

        :return: True/False
        """
        return self.min_distance_mm <= self.current_distance_mm <= self.max_distance_mm

    def validate_mode(self) -> bool:
        """
        Checks what mode the sensor is in.

        :return: True/False
        """
        return self.mode

    def validate(self):
        """
        Checks whether the sensor operates according to its set parameters.

        :return: True/False
        """
        return self.validate_mode() and self.validate_distance()
