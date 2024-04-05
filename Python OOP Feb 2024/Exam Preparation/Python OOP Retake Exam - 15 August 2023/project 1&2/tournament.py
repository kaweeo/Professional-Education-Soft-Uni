from typing import List

from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    VALID_EQUIPMENT_TYPES = ['ElbowPad', 'KneePad']
    VALID_TEAM_TYPES = ['IndoorTeam', 'OutdoorTeam']

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[KneePad: BaseEquipment, ElbowPad: BaseEquipment] = []
        self.teams: List[IndoorTeam: BaseTeam, OutdoorTeam: BaseTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")

        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.VALID_EQUIPMENT_TYPES:
            raise ValueError("Invalid equipment type!")

        equipment_object = globals()[equipment_type]
        equipment = equipment_object()
        self.equipment.append(equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.VALID_TEAM_TYPES:
            raise ValueError("Invalid team type!")

        if len(self.teams) == self.capacity:
            return "Not enough tournament capacity."

        team_object = globals()[team_type]
        team = team_object(team_name, country, advantage)
        self.teams.append(team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):

        filter_eq_by_type = [eq for eq in self.equipment if eq.__class__.__name__ == equipment_type]
        equipment = filter_eq_by_type[-1]
        team = next(filter(lambda t: t.name == team_name, self.teams))

        if team.budget < equipment.price:
            raise Exception("Budget is not enough!")

        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):

        try:
            team = next(filter(lambda t: t.name == team_name, self.teams))
        except StopIteration:
            raise Exception("No such team!")

        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):

        counter = 0

        for equipment in self.equipment:
            if equipment.__class__.__name__ == equipment_type:
                equipment.increase_price()
                counter += 1

        return f"Successfully changed {counter}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team_1 = next(filter(lambda team: team.name == team_name1, self.teams))
        team_2 = next(filter(lambda team: team.name == team_name2, self.teams))

        if team_1.__class__.__name__ != team_2.__class__.__name__:
            raise Exception(f"Game cannot start! Team types mismatch!")

        team_1_protection = sum([equipment.protection for equipment in team_1.equipment])
        team_2_protection = sum([equipment.protection for equipment in team_2.equipment])

        team_1_result = team_1.advantage + team_1_protection
        team_2_result = team_2.advantage + team_2_protection

        if team_1_result == team_2_result:
            return "No winner in this game."

        if team_1_result > team_2_result:
            team_1.win()
            return f"The winner is {team_1.name}."

        if team_1_result < team_2_result:
            team_2.win()
            return f"The winner is {team_2.name}."

    def get_statistics(self):

        sorted_teams = sorted(self.teams, key=lambda team: -team.wins)

        result = [f"Tournament: {self.name}", f"Number of Teams: {len(self.teams)}", "Teams:"]
        [result.append(t.get_statistics()) for t in sorted_teams]
        return '\n'.join(result)

# from typing import List
#
# from project 1&2.equipment.base_equipment import BaseEquipment
# from project 1&2.equipment.elbow_pad import ElbowPad
# from project 1&2.equipment.knee_pad import KneePad
# from project 1&2.teams.base_team import BaseTeam
# from project 1&2.teams.indoor_team import IndoorTeam
# from project 1&2.teams.outdoor_team import OutdoorTeam
#
#
# class Tournament:
#     valid_equipments = {
#         "KneePad": KneePad,
#         "ElbowPad": ElbowPad,
#     }
#     valid_teams = {
#         "OutdoorTeam": OutdoorTeam,
#         "IndoorTeam": IndoorTeam,
#
#     }
#
#     def __init__(self, name: str, capacity: int):
#         self.name = name
#         self.capacity = capacity
#         self.equipment: List[KneePad: BaseEquipment, ElbowPad: BaseEquipment] = []
#         self.teams: List[IndoorTeam: BaseTeam, OutdoorTeam: BaseTeam] = []
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         if not value.isalnum():
#             raise ValueError("Tournament name should contain letters and digits only!")
#
#         self.__name = value
#
#     def add_equipment(self, equipment_type: str):
#         if equipment_type not in self.valid_equipments.keys():
#             raise Exception("Invalid equipment type!")
#
#         new_valid_equipment = self.valid_equipments[equipment_type]()
#         self.equipment.append(new_valid_equipment)
#         return f"{equipment_type} was successfully added."
#
#     def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
#         if team_type not in self.valid_teams.keys():
#             raise Exception("Invalid team type!")
#
#         if self.capacity <= len(self.teams):
#             return "Not enough tournament capacity."
#
#         new_valid_team = self.valid_teams[team_type](team_name, country, advantage)
#         self.teams.append(new_valid_team)
#         return f"{team_type} was successfully added."
#
#     def sell_equipment(self, equipment_type: str, team_name: str):
#         team = next(filter(lambda n: n.name == team_name, self.teams))
#         # equipment = next(filter(lambda e: e == equipment_type, self.equipment))
#         equipment = [e for e in self.equipment if e.__class__.__name__ == equipment_type][-1]
#         if team.budget < equipment.price:
#             raise Exception("Budget is not enough!")
#
#         self.equipment.remove(equipment)
#         team.equipment.append(equipment)
#         team.budget -= equipment.price
#         return f"Successfully sold {equipment_type} to {team_name}."
#
#     def remove_team(self, team_name: str):
#         team = next(filter(lambda n: n.name == team_name, self.teams), None)
#         if not team:
#             raise Exception("No such team!")
#
#         if team.wins > 0:
#             raise Exception(f"The team has {team.wins} wins! Removal is impossible!")
#
#         self.teams.remove(team)
#         return f"Successfully removed {team_name}."
#
#     # def increase_equipment_price(self, equipment_type: str):
#     #
#     #     changed_equipments = [e.increase_price() for e in self.equipment if
#     #                           e.__class__.__name__ == equipment_type]  # TODO: CARE HERE A LOT
#     #     return f"Successfully changed {len(changed_equipments)}pcs of equipment."
#     def increase_equipment_price(self, equipment_type: str):
#         count = 0
#         for item in self.equipment:
#             if item.__class__.__name__ == equipment_type:
#                 item.increase_price()
#                 count += 1
#         return f"Successfully changed {count}pcs of equipment."
#
#     def play(self, team_name1: str, team_name2: str):
#         team_1 = next(filter(lambda t: t.name == team_name1, self.teams))
#         team_2 = next(filter(lambda t: t.name == team_name2, self.teams))
#
#         if team_1.__class__.__name__ != team_2.__class__.__name__:
#             raise Exception("Game cannot start! Team types mismatch!")
#
#         protections_team_1 = [eq.protection for eq in team_1.equipment]
#         protections_team_2 = [eq.protection for eq in team_2.equipment]
#         team_1_result = team_1.advantage + sum(protections_team_1)
#         team_2_result = team_2.advantage + sum(protections_team_2)
#
#         if team_1_result > team_2_result:
#             team_1.win()
#             return f"The winner is {team_1.name}."
#
#         elif team_2_result > team_1_result:
#             team_2.win()
#             return f"The winner is {team_2.name}."
#
#         else:
#             return "No winner in this game."
#
#     # def get_statistics(self):
#     #     sorted_teams = list(sorted(self.teams, key=lambda team: -team.wins))
#     #     result = f"Tournament: {self.name}\nNumber of Teams: {len(self.teams)}\nTeams:\n"
#     #     result += "\n".join(str(e) for e in sorted_teams)
#     #     return result
#
#     def get_statistics(self):
#         sorted_teams = list(sorted(self.teams, key=lambda team: -team.wins))
#         num_teams = len(self.teams)
#         teams_info = "\n".join(team.get_statistics() for team in sorted_teams)
#         return f"Tournament: {self.name}\nNumber of Teams: {num_teams}\nTeams:\n{teams_info}"
