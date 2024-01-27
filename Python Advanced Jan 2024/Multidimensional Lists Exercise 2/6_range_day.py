
SIZE = 5
field = []
targets_count = 0
hit_target_positions = []
hit_targets = 0
current_pos = []

for row in range(SIZE):
    field.append(input().split())
    if "A" in field[row]:
        current_pos = [row, field[row].index("A")]
        field[current_pos[0]][current_pos[1]] = "."
    if "x" in field[row]:
        targets_count += field[row].count("x")

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}


number_commands = int(input())

for _ in range(number_commands):
    command = input().split()
    row, col = current_pos

    if command[0] == "move":
        direction = command[1]
        steps = int(command[2])
        x = row + directions[direction][0] * steps
        y = col + directions[direction][1] * steps
        if 0 <= x < SIZE and 0 <= y < SIZE:
            if field[x][y] == ".":
                current_pos = [x, y]

    elif command[0] == "shoot":
        direction = command[1]
        x = row + directions[direction][0]
        y = col + directions[direction][1]

        while 0 <= x < SIZE and 0 <= y < SIZE:
            if field[x][y] == "x":
                hit_targets += 1
                hit_target_positions.append([x, y])
                field[x][y] = "."
                break

            x += directions[direction][0]
            y += directions[direction][1]

    if hit_targets == targets_count:
        break

if hit_targets >= targets_count:
    print(f"Training completed! All {targets_count} targets hit.")
else:
    print(f"Training not completed! {targets_count - hit_targets} targets left.")

if hit_target_positions:
    [print(position) for position in hit_target_positions]


