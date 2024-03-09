from project.player import Player


class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players: list[Player] = []  # [Player1, Player2]

    def add_player(self, player: Player):
        if player in self.__players:
            return f"Player {player.name} has already joined"

        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name: str):
        try:
            searched_player = next(filter(lambda p: player_name == p.name, self.__players))
        except StopIteration:
            return f"Player {player_name} not found"

        self.__players.remove(searched_player)
        return searched_player
