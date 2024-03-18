from abc import ABC
from project.animals.animal import Bird


class Owl(Bird):
    # def __init__(self):           will be inherited
    #     super().__init__()

    @staticmethod
    def make_sound(self) -> str:
        return "Hoot Hoot"


class Hen(Bird):
    @staticmethod
    def make_sound() -> str:
        return "Cluck"
