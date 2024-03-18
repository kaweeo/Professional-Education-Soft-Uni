from abc import ABC, abstractmethod
from project.animals.animal import Mammal


class Mouse(Mammal):
    @staticmethod
    def make_sound(self) -> str:
        return "Squeak"


class Dog(Mammal):
    @staticmethod
    def make_sound(self) -> str:
        return "Woof"


class Cat(Mammal):
    @staticmethod
    def make_sound(self) -> str:
        return "Meow"


class Tiger(Mammal):
    @staticmethod
    def make_sound(self) -> str:
        return "ROAR!!!"
