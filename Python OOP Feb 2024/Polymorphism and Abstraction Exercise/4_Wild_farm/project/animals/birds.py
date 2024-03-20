from abc import ABC
from typing import List, Type

from project.animals.animal import Bird
from project.food import Food, Meat, Fruit, Vegetable, Seed


class Owl(Bird):
    # def __init__(self):           will be inherited
    #     super().__init__()
    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def gained_weight(self) -> float:
        return 0.25

    @staticmethod
    def make_sound() -> str:
        return "Hoot Hoot"


class Hen(Bird):
    @property
    def food_that_eats(self):
        return [Meat, Fruit, Vegetable, Seed]

    @property
    def gained_weight(self) -> float:
        return 0.35

    @staticmethod
    def make_sound() -> str:
        return "Cluck"
