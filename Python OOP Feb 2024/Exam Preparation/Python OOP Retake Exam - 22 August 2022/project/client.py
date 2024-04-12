from typing import List

from project.meals.meal import Meal


class Client:

    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart: List[Meal] = []
        self.bill: float = 0.0

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        if len(value) == 10 and [e.isdigit() for e in value] and value[0] == "0":
            self.__phone_number = value
        else:
            raise ValueError("Invalid phone number!")
