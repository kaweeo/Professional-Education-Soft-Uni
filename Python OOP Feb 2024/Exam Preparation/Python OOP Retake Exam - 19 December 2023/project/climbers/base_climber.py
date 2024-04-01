from abc import ABC, abstractmethod

from peaks.base_peak import BasePeak


class BaseClimber(ABC):
    STRENGTH_ICNREASEMENT_WHEN_REST = 15

    def __init__(self, name, strength):
        self.name = name
        self.strength = strength
        self.conquered_peaks = []
        self.is_prepared = True

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":  # TODO: Care here
            raise ValueError("Climber name cannot be null or empty!")

        self.__name = value

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, value):
        if self.strength <= 0:
            raise ValueError("A climber cannot have negative strength or strength equal to 0!")

        self.__strength = value

    @abstractmethod
    def can_climb(self):
        ...  # TODO: Care will be overwrite

    @abstractmethod
    def climb(peak: BasePeak):
        ...  # TODO: Care will be overwrite

    @abstractmethod
    def rest(self):
        self.strength += BaseClimber.STRENGTH_ICNREASEMENT_WHEN_REST

    def __str__(self):
        return f"{self.__class__}: /// Climber name: {self.name} * Left strength: {self.strength} * Conquered peaks: {', '.join(self.conquered_peaks)} ///"  # TODO: CARE HERE
