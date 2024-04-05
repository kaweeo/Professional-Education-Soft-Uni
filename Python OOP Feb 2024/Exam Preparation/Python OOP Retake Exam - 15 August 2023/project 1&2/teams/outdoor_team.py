from typing import List

from project.equipment.base_equipment import BaseEquipment
from project.teams.base_team import BaseTeam


class OutdoorTeam(BaseTeam):
    INIT_BUDGET = 1000.0

    def __init__(self, name: str, country: str, advantage: int):  # TODO: CARE HERE
        super().__init__(name, country, advantage, self.INIT_BUDGET)
        self.wins = 0
        self.equipment: List[BaseEquipment] = []

    def win(self):
        self.advantage += 115
        self.wins += 1
