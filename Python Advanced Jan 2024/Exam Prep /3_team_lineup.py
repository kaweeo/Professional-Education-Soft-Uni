
def team_lineup(*args):

    players_nationality = {}

    for arg in args:
        player, nationality = arg
        if not nationality in players_nationality.keys():
            players_nationality[nationality] = []
        players_nationality[nationality].append(player)

    players_nationality_sorted = dict(sorted(players_nationality.items(), key=lambda x: (-len(x[1]), x[0])))

    result = ""
    for nationality, players in players_nationality_sorted.items():
        result += f"{nationality}:\n"
        for player in players:
            result += f"  -{player}\n"

    return result


print(team_lineup(  ("Lionel Messi", "Argentina"),   ("Neymar", "Brazil"),   ("Cristiano Ronaldo", "Portugal"),   ("Harry Kane", "England"),   ("Kylian Mbappe", "France"),   ("Raheem Sterling", "England")))