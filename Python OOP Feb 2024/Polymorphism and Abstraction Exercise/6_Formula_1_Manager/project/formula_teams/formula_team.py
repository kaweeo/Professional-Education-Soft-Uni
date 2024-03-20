from abc import ABC, abstractmethod
from typing import Dict


class FormulaTeam(ABC):
    MIN_BUDGET: int = 1_000_000

    def __init__(self, budget: int):
        self.budget = budget

    @property
    @abstractmethod
    def sponsors(self):
        ...

    @property
    @abstractmethod
    def expenses_for_one_race(self) -> int:
        ...

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < FormulaTeam.MIN_BUDGET:
            raise ValueError("F1 is an expensive sport, find more sponsors!")

        self.__budget = value

    def calculate_revenue_after_race(self, race_pos: int):
        race_income = 0

        for sponsor in self.sponsors.keys():
            for k, v in self.sponsors[sponsor].items():
                if race_pos <= k:
                    race_income += v
                    break

        revenue = race_income - self.expenses_for_one_race
        self.budget += revenue

        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
