
n = int(input())
sea = []
starting_pos = []
LIFE = 3
destroyed_ships = 0

for sea_row in range(n):
    row = list(input())
    if "S" in row:
        starting_pos = [sea_row, row.index("S")]
    sea.append(row)

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

row, col = starting_pos
while True:
    directon = input()

    next_row = row + directions[directon][0]
    next_col = col + directions[directon][1]

    if sea[next_row][next_col] == "-":
        pass
    elif sea[next_row][next_col] == "*":
        sea[row][col] = "-"
        sea[next_row][next_col] = "S"
        LIFE -= 1
        if LIFE == 0:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{next_row}, {next_col}]!")
            break
    elif sea[next_row][next_col] == "C":
        sea[row][col] = "-"
        sea[next_row][next_col] = "S"
        destroyed_ships += 1
        if destroyed_ships == 3:
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break
    sea[row][col] = "-"
    sea[next_row][next_col] = "S"
    row, col = next_row, next_col

for row in sea:
    print(''.join(row))