"""This module is for an inductive sensor."""
from sensors.sensors_base import Sensors


class InductiveSensor(Sensors):
    """
    Inductive sensor class
    """

    EXPECTED_MATERIALS = ['iron', 'steel', 'aluminium', 'copper']
    def __init__(self, name: str,  min_distance_mm: float,
                max_distance_mm: float, current_distance_mm: float, material: str):
        """
        Creates the object  inductive sensor.
        """
        super().__init__(name)
        self.min_distance_mm = min_distance_mm
        self.max_distance_mm = max_distance_mm
        self.current_distance_mm = current_distance_mm
        self.material = material

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

    def validate_material(self) -> bool:
        """
        Checks wheter the material is metal or not.

        :return: True/False
        """
        return self.material in self.EXPECTED_MATERIALS

    def validate(self):
        """
        Returns true when a metal object is detected within the set range.

        :return: True/False
        """
        return self.validate_material() and self.validate_distance()
