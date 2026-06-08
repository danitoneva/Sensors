"""
In this module, a class for sensors has been created.
"""
from abc import ABC, abstractmethod


class Sensors(ABC):
    """Base class for sensors."""

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def read_value(self) -> float:
        """
        This function reads the value.

        :return: float
        """
        pass

    @abstractmethod
    def validate(self) -> bool:
        """
        This function validate the data.

        :return: True/False
        """
        pass
