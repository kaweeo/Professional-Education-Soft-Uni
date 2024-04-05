from abc import ABC, abstractmethod
from typing import List


class BaseTeam(ABC):

    def __init__(self, name: str, country: str, advantage: int, budget: float):
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget = budget
        self.wins = 0
        self.equipment: List = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value or value.isspace():
            raise ValueError("Team name cannot be empty!")

        self.__name = value

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        if len(value.strip()) < 2:
            raise ValueError("Team country should be at least 2 symbols long!")

        self.__country = value

    @property
    def advantage(self):
        return self.__advantage

    @advantage.setter
    def advantage(self, value):
        if value <= 0:
            raise ValueError("Advantage must be greater than zero!")

        self.__advantage = value

    @abstractmethod
    def win(self):
        pass

    def get_statistics(self):
        string_budget = f"{self.budget:.2f}"
        total_equipment_price = 0
        total_protection = 0

        for equipment in self.equipment:
            total_equipment_price += equipment.price
            total_protection += equipment.protection

        total_equipment_price_str = f"{sum(equipment.price for equipment in self.equipment):.2f}"
        average_protection = 0
        if self.equipment:
            average_protection = str(int(total_protection / len(self.equipment)))

        result = ("Name: " + self.name + "\n" +
                  "Country: " + self.country + "\n" +
                  "Advantage: " + str(self.advantage) + " points\n" +
                  "Budget: " + string_budget + "EUR\n" +
                  "Wins: " + str(self.wins) + "\n" +
                  "Total Equipment Price: " + total_equipment_price_str + "\n" +
                  "Average Protection: " + str(average_protection)
                  )

        return result





# from abc import ABC, abstractmethod
# from typing import List
# from math import floor
# from project 1&2.equipment.base_equipment import BaseEquipment
#
#
# class BaseTeam(ABC):
#
#     def __init__(self, name: str, country: str, advantage: int, budget: float):
#         self.name = name
#         self.country = country
#         self.advantage = advantage
#         self.budget = budget
#         self.wins = 0
#         self.equipment: List[BaseEquipment] = []
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         if not value or value.isspace():
#             raise ValueError("Team name cannot be empty!")
#
#         self.__name = value
#
#     @property
#     def country(self):
#         return self.__country
#
#     @country.setter
#     def country(self, value):
#         if len(value.strip()) < 2:
#             raise ValueError("Team country should be at least 2 symbols long!")
#
#         self.__country = value
#
#     @property
#     def advantage(self):
#         return self.__advantage
#
#     @advantage.setter
#     def advantage(self, value):
#         if value <= 0:
#             raise ValueError("Advantage must be greater than zero!")
#
#         self.__advantage = value
#
#     @abstractmethod
#     def win(self):
#         ...
#
#     def get_statistics(self):
#         total_price_of_team_equipment = sum([x.price for x in self.equipment])
#         if self.equipment:
#             avg_team_protection = sum([x.protection for x in self.equipment]) / len(self.equipment)
#         else:
#             avg_team_protection = 0
#         result = (f"Name: {self.name}\n"
#                   f"Country: {self.country}\n"
#                   f"Advantage: {self.advantage} points\n"
#                   f"Budget: {self.budget:.2f}EUR\n"
#                   f"Wins: {self.wins}\n"
#                   f"Total Equipment Price: {total_price_of_team_equipment:.2f}\n"
#                   f"Average Protection: {int(avg_team_protection)}")
#
#         return result
