"""This module is for a pressure sensor."""
from sensors.sensors_base import Sensors


class PressureSensor(Sensors):
    """
    Pressure sensor class
    """

    EXPECTED_UNIT = "bar"
    def __init__(self, name: str,  min_pressure: float,
                 max_pressure: float, current_pressure: float, unit: str):
        """
        Creates the object  inductive sensor.
        """
        super().__init__(name)
        self.min_pressure = min_pressure
        self.max_pressure = max_pressure
        self.current_pressure = current_pressure
        self.unit = unit

    def read_value(self) -> float:
        """
        Returns the value of the current pressure.

        :return: number
        """
        return self.current_pressure

    def validate_distance(self) -> bool:
        """
        Checks whether the current pressure falls within the range.

        :return: True/False
        """
        return self.min_pressure <= self.current_pressure <= self.max_pressure

    def validate_unit(self) -> bool:
        """
        Checks if it is in the correct unit.

        :return: True/False
        """
        return self.unit == self.EXPECTED_UNIT

    def validate(self):
        """
        Returns True when the sensor works within the range of the parameters given to it.

        :return: True/False
        """
        return self.validate_unit() and self.validate_distance()
