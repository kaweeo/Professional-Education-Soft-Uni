from abc import ABC, abstractmethod
from typing import List

from project.food import Food


class Animal(ABC):
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @property
    @abstractmethod
    def food_that_eats(self):
        ...

    @property
    @abstractmethod
    def gained_weight(self) -> float:
        ...

    @staticmethod
    @abstractmethod
    def make_sound() -> str:
        ...

    def feed(self, food: Food) -> str or None:
        if type(food) not in self.food_that_eats:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += self.gained_weight * food.quantity
        self.food_eaten += food.quantity


class Bird(Animal, ABC):
    def __init__(self, name, weight, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    # def make_sound(self):         # It should be inherited and no need to def again because it is abstract class
    #     pass

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):
    def __init__(self, name, weight, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    # def make_sound(self):         # It should be inherited and no need to def again because it is abstract class
    #     pass

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
