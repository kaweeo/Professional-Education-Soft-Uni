size = 5

matrix = []

target_total = 0
dead_target = []
my_pos = []

directions = {
    "right": (0, 1),
    "left": (0, -1),
    "up": (-1, 0),
    "down": (1, 0)
}

for row_i in range(size):
    matrix.append(input().split())
    if "x" in matrix[row_i]:
        target_total += matrix[row_i].count("x")
    if "A" in matrix[row_i]:
        my_pos = [row_i, matrix[row_i].index("A")]

num_comm = int(input())

for comm in range(num_comm):
    command = input().split()
    action = command[0]
    direction = command[1]
    if action == "shoot":

        pos_row = directions[direction][0] + my_pos[0]
        pos_col = directions[direction][1] + my_pos[1]
        while 0 <= pos_row < 5 and 0 <= pos_col < 5:
            if matrix[pos_row][pos_col] == "x":
                target_total -= 1
                dead_target.append([pos_row, pos_col])

                matrix[pos_row][pos_col] = "."
            pos_row += directions[direction][0]
            pos_col += directions[direction][1]

    elif action == "move":
        steps = int(command[2])

        pos_row = my_pos[0] + (directions[direction][0] * steps)
        pos_col = my_pos[1] + (directions[direction][1] * steps)

        if 0 <= pos_row < 5 and 0 <= pos_col < 5:
            if matrix[pos_row][pos_col] == ".":
                my_pos = [pos_row, pos_col]

if target_total > 0:
    print(f"Training not completed! {target_total} targets left.")
    print(*dead_target, sep='\n')

else:
    print(f"Training completed! All {len(dead_target)} targets hit.")
    print(*dead_target, sep='\n')