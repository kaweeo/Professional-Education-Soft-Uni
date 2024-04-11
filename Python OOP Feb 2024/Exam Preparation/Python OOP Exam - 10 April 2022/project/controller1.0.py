from typing import List, Union

from project.player import Player
from project.supply.drink import Drink
from project.supply.food import Food


class Controller:
    VALID_SUSTENANCE = ["Food", "Drink"]

    def __init__(self):
        self.players: List[Player] = []
        self.supplies: List[Union[Food, Drink]] = []

    def add_player(self, *players):
        successfully_added_player_names = []

        for player in players:
            if player not in self.players:
                successfully_added_player_names.append(player.name)
                self.players.append(player)

        return f"Successfully added: {', '.join(successfully_added_player_names)}"

    def add_supply(self, *supplies):
        [self.supplies.append(s) for s in supplies]

    def sustain(self, player_name: str, sustenance_type: str):
        player = next((player for player in self.players if player_name == player.name), None)
        if not player:
            return
        if not player.need_sustenance:
            return f"{player_name} have enough stamina."
        if sustenance_type not in Controller.VALID_SUSTENANCE:
            return
        needed_supplies = [supply for supply in self.supplies if sustenance_type == supply.__class__.__name__]
        if not needed_supplies:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")
        supply = needed_supplies.pop()
        reversed_supps = list(reversed(self.supplies))
        reversed_supps.remove(supply)
        self.supplies = list(reversed(reversed_supps))
        player.stamina += supply.energy
        if player.stamina > 100:
            player.stamina = 100
        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = [p for p in self.players if p.name == first_player_name][0]
        second_player = [p for p in self.players if p.name == second_player_name][0]

        if first_player.stamina == 0:
            return f"Player {first_player_name} does not have enough stamina."

        if second_player.stamina == 0:
            return f"Player {second_player_name} does not have enough stamina."

        if first_player.stamina < second_player.stamina:
            second_player.stamina -= first_player.stamina * 0.5
            if second_player.stamina <= 0:
                second_player.stamina = 0
                return f"Winner: {first_player_name}"
            first_player.stamina -= second_player.stamina * 0.5
            if first_player.stamina <= 0:
                first_player.stamina = 0
                return f"Winner: {second_player_name}"
        else:
            first_player.stamina -= second_player.stamina * 0.5
            if first_player.stamina <= 0:
                first_player.stamina = 0
                return f"Winner: {second_player_name}"
            second_player.stamina -= first_player.stamina * 0.5
            if second_player.stamina <= 0:
                second_player.stamina = 0
                return f"Winner: {first_player_name}"

        if first_player.stamina > second_player.stamina:
            return f"Winner: {first_player_name}"

        return f"Winner: {second_player_name}"

    # def duel(self, first_player_name: str, second_player_name: str):
    #     first_player = next((p for p in self.players if p.name == first_player_name), None)
    #     second_player = next((p for p in self.players if p.name == second_player_name), None)
    #
    #     if not first_player:
    #         return f"Player {first_player_name} not found."
    #     if not second_player:
    #         return f"Player {second_player_name} not found."
    #
    #     if first_player.stamina == 0:
    #         return f"Player {first_player_name} does not have enough stamina."
    #     if second_player.stamina == 0:
    #         return f"Player {second_player_name} does not have enough stamina."
    #
    #     damage = min(first_player.stamina, second_player.stamina) * 0.5
    #     first_player.stamina -= damage
    #     second_player.stamina -= damage
    #
    #     if first_player.stamina <= 0:
    #         first_player.stamina = 0
    #         return f"Winner: {second_player_name}"
    #     elif second_player.stamina <= 0:
    #         second_player.stamina = 0
    #         return f"Winner: {first_player_name}"

    def next_day(self):
        for player in self.players:
            player.stamina -= player.age * 2
            if player.stamina < 0:
                player.stamina = 0
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = ""
        for player in self.players:
            result += f"{player.__str__()}\n"
        for supply in self.supplies:
            result += f"{supply.details()}\n"

        return result
