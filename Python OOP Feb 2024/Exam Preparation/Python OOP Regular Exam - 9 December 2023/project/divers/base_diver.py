from abc import ABC, abstractmethod
from typing import List

from project.fish.base_fish import BaseFish


class BaseDiver(ABC):

    def __init__(self, name: str, oxygen_level: float):
        self.name = name
        self.oxygen_level = oxygen_level  # diver's oxygen level remaining, in seconds.
        self.catch: List[BaseFish] = []  # a sequence of fish, caught by a specific diver
        self._competition_points: float = 0.0  # total points accumulated by a diver
        self.has_health_issue: bool = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Diver name cannot be null or empty!")
        self.__name = value

    @property
    def oxygen_level(self):
        return self.__oxygen_level

    @oxygen_level.setter
    def oxygen_level(self, value):
        if value < 0:
            raise ValueError("Cannot create diver with negative oxygen level!")
        self.__oxygen_level = value

    @property
    def competition_points(self):
        return round(float(self._competition_points), 1)

    @abstractmethod
    def miss(self, time_to_catch: int):
        # Decreases the diver's oxygen_level property.
        # When the method is invoked the diver's oxygen_level is decreased by a certain value,
        # that will depend on the fish that is chased.
        ...

    @abstractmethod
    def renew_oxy(self):
        # The diver's oxygen_level should be fully replenished to its original value.
        # This would mean setting the oxygen_level back to its starting value depending on the diver’s type.
        ...

    def hit(self, fish: BaseFish):
        if self.oxygen_level - fish.time_to_catch < 0:
            self.oxygen_level = 0

        else:
            self.oxygen_level -= fish.time_to_catch
            self.catch.append(fish)
            self._competition_points += fish.points

    def update_health_status(self):
        self.has_health_issue = not self.has_health_issue

    def __str__(self):
        return f"{self.__class__.__name__}: [Name: {self.name}, Oxygen level left: {int(self.oxygen_level)}, " \
               f"Fish caught: {len(self.catch)}, Points earned: {self.competition_points}]"
