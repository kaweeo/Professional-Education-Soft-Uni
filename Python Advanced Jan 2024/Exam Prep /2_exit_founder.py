
player_1, player_2 = input().split(", ")
players = [player_1, player_2]
maze = []

for line in range(6):
    row_line = input().split()
    maze.append(row_line)

coordinates_input_count = 0
flagged_player = []

while True:
    coordinates = input()
    coordinates_input_count += 1

    if coordinates_input_count % 2 != 0:
        player = player_1
    else:
        player = player_2

    if player in flagged_player:
        flagged_player.remove(player)
        continue

    row = int(coordinates[1])
    col = int(coordinates[4])

    if maze[row][col] == "E":
        print(f"{player} found the Exit and wins the game!")
        break
    elif maze[row][col] == "T":
        if player == player_1:
            winner = player_2
        else:
            winner = player_1
        print(f"{player} is out of the game! The winner is {winner}.")
        break
    elif maze[row][col] == "W":
        print(f"{player} hits a wall and needs to rest.")
        flagged_player.append(player)

