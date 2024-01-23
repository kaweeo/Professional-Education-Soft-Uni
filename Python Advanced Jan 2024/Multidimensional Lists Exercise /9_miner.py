n = int(input())
commands = input().split()

matrix = []
miner_pos = []  # [miner_row, miner_col]
collected_coal, total_coal = 0, 0

directions = {  # 5 3 -> 5 + (-1), 3 + 0 => 4, 3
    "up": [-1, 0],
    "down": [1, 0],  # [row, col]
    "left": [0, -1],
    "right": [0, 1],
}

for row in range(n):
    matrix.append(input().split())

    if "s" in matrix[row]:
        miner_pos = [row, matrix[row].index("s")]
        matrix[miner_pos[0]][miner_pos[1]] = "*"

    total_coal += matrix[row].count("c")

for command in commands:  # command => down
    r, c = miner_pos[0] + directions[command][0], miner_pos[1] + directions[command][1]

    if not (0 <= r < n and 0 <= c < n):
        continue

    miner_pos = [r, c]

    if matrix[r][c] == "c":
        collected_coal += 1

        if collected_coal == total_coal:
            print(f"You collected all coal! ({r}, {c})")
            break

    elif matrix[r][c] == "e":
        print(f"Game over! ({r}, {c})")
        break

    matrix[r][c] = "*"
else:
    print(f"{total_coal - collected_coal} pieces of coal left. ({miner_pos[0]}, {miner_pos[1]})")

# IMPORTANT:  if not (0 <= r < n and 0 <= c < n):
#
#
# def mover(some_posistion, direction):
#     if 0 <= some_posistion[0] + directions[direction][0] < size and 0 <= some_posistion[1] + directions[direction][1] < size:
#         new_position = (some_posistion[0] + directions[direction][0], some_posistion[1] + directions[direction][1])
#         return new_position
#     else:
#         return some_posistion
#
#
# def finder(some_matrix, target_element):
#     appearances = 0
#
#     for row_index, row in enumerate(some_matrix):
#         for col_index, element in enumerate(row):
#             if element == target_element:
#                 if element == "c":
#                     appearances += 1
#                 else:
#                     return row_index, col_index
#
#     return appearances
#
# size = int(input())
# commands = input().split()
# matrix = [input().split() for row in range(size)]
#
# directions = {
#     "up": (-1, 0),    # up
#     "down": (1, 0),     # down
#     "left": (0, -1),    # left
#     "right": (0, 1),     # right
# }
#
# start_coordinates = finder(matrix, "s")
# start_row, start_col = start_coordinates
#
# end_coordinates = finder(matrix, "e")
# end_row, end_col = end_coordinates
#
# all_coal = finder(matrix, "c")
#
# is_over = False
# coal_counter = 0
# current_position = start_coordinates
# for command in commands:
#     current_position = mover(current_position, command)
#     row, col = current_position
#
#     if matrix[row][col] == "c":
#         coal_counter += 1
#         matrix[row][col] = "*"
#         if coal_counter == all_coal:
#             is_over = True
#             print(f"You collected all coal! ({row}, {col})")
#             break
#     elif matrix[row][col] == "e":
#         is_over = True
#         print(f"Game over! ({row}, {col})")
#         break
#
# if not is_over:
#     print(f"{all_coal - coal_counter} pieces of coal left. ({row}, {col})")