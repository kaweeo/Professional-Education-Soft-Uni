def make_a_move(row_, col_, matrix):
    found_hazelnuts = 0
    if not (0 <= row_ < len(matrix) and 0 <= col_ < len(matrix)):
        print("The squirrel is out of the field.")
        return
    if matrix[row_][col_] == 't':
        print("Unfortunately, the squirrel stepped on a trap...")
        return
    if matrix[row_][col_] == 'h':
        found_hazelnuts += 1
    matrix[row_][col_] = '*'
    return found_hazelnuts, matrix


rows = int(input())
commands = input().split(", ")
field = []
hazelnuts = 0
die = False

for _ in range(rows):
    field.append(list(input()))

squirrel_position = []
for row in range(rows):
    for col in range(rows):
        if field[row][col] == 's':
            squirrel_position = [row, col]

field[squirrel_position[0]][squirrel_position[1]] = "*"

for command in commands:
    if command == 'left':
        squirrel_position[1] -= 1
    elif command == 'right':
        squirrel_position[1] += 1
    elif command == 'down':
        squirrel_position[0] += 1
    elif command == 'up':
        squirrel_position[0] -= 1
    result = make_a_move(squirrel_position[0], squirrel_position[1], field)
    if not result:
        die = True
        break
    count_hazelnuts, field = result[0], result[1]
    hazelnuts += count_hazelnuts
    if hazelnuts == 3:
        print("Good job! You have collected all hazelnuts!")
        break

if not die and hazelnuts < 3:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts}")


# # SOLUTION 2
# SIZE = int(input())
# HAZELNUTS_TARGET = 3
#
# directions = input().split(", ")
# matrix = []
# starting_pos = []
# hazelnut_count = 0
#
# directions_mapper = {
#     "up": (-1, 0),
#     "down": (1, 0),
#     "left": (0, -1),
#     "right": (0, 1),
# }
#
# for matrix_row in range(SIZE):
#     row = list(input())
#     if "s" in row:
#         starting_pos = [matrix_row, row.index("s")]
#     matrix.append(row)
#
# game_ended = False
# row, col = starting_pos
#
# for direction in directions:
#     next_row = row + directions_mapper[direction][0]
#     next_col = col + directions_mapper[direction][1]
#
#     if not (0 <= next_row < SIZE and 0 <= next_col < SIZE):
#         print("The squirrel is out of the field.")
#         game_ended = True
#         break
#     elif matrix[next_row][next_col] == "t":
#         print("Unfortunately, the squirrel stepped on a trap...")
#         game_ended = True
#         break
#     elif matrix[next_row][next_col] == "h":
#         hazelnut_count += 1
#         matrix[next_row][next_col] = "*"
#         if hazelnut_count == HAZELNUTS_TARGET:
#             print("Good job! You have collected all hazelnuts!")
#             game_ended = True
#             break
#     row = next_row
#     col = next_col
#
# if not game_ended:
#     print("There are more hazelnuts to collect.")
# print(f"Hazelnuts collected: {hazelnut_count}")
