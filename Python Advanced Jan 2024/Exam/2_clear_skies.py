
n = int(input())
armor = 300
enemy_planes = 4
airspace = []
starting_pos = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for skyline in range(n):
    row = list(input())
    if "J" in row:
        starting_pos = [skyline, row.index("J")]
    airspace.append(row)

row, col = starting_pos
while armor and enemy_planes:   # TODO care here. while True option

    direction = input()
    next_row = row + directions[direction][0]
    next_col = col + directions[direction][1]

    if airspace[next_row][next_col] == "-":
        airspace[row][col] = "-"
        airspace[next_row][next_col] = "J"

    if airspace[next_row][next_col] == "E":
        airspace[next_row][next_col] = "-"
        enemy_planes -= 1
        if enemy_planes == 0:
            airspace[row][col] = "-"
            airspace[next_row][next_col] = "J"
            print("Mission accomplished, you neutralized the aerial threat!")  #TODO CARE HERE POSITION !!!!
            break
        else:
            armor -= 100
            if armor == 0:
                airspace[row][col] = "-"
                airspace[next_row][next_col] = "J"
                print(f"Mission failed, your jetfighter was shot down! Last coordinates [{next_row}, {next_col}]!") #TODO CARE HERE POSITION !!!!
                break

    if airspace[next_row][next_col] == "R":
        armor = 300
        airspace[next_row][next_col] = "-"

    row, col = next_row, next_col

[print("".join(row)) for row in airspace]
