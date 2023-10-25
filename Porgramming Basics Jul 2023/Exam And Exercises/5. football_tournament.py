
team_name = input()
games = int(input())

points = 0
w_counter = 0
d_counter = 0
l_counter = 0

if games == 0:
    print(f"{team_name} hasn't played any games during this season.")
else:
    for game in range(1, games + 1):
        result = input()
        if result == "W":
            points += 3
            w_counter += 1
        elif result == "D":
            points += 1
            d_counter += 1
        elif result == "L":
            l_counter +=1
    procent_won = w_counter / games * 100
    print(f"{team_name} has won {points} points during this season.")
    print(f"Total stats:")
    print(f"## W: {w_counter}")
    print(f"## D: {d_counter}")
    print(f"## L: {l_counter}")
    print(f"Win rate: {procent_won:.2f}%")