

def starting_position(matrix: list, length):
    row_idx = 0
    col_idx = 0
    for i in range(length):
        for j in range(length):
            if matrix[i][j] == 'S':
                row_idx, col_idx = i, j
    return row_idx, col_idx


def count_nice_kids(matrix, length):
    counter = 0
    for idx in range(length):
        for col_idx in range(length):
            if matrix[idx][col_idx] == 'V':
                counter += 1
    return counter


def santa_move(matrix, action, row, col, presents, kids, kids_presents):
    matrix[row][col] = '-'
    row += directions[action][0]
    col += directions[action][1]

    if matrix[row][col] == 'V':
        kids -= 1
        presents -= 1
        kids_presents += 1
        matrix[row][col] = 'S'
    elif matrix[row][col] == 'X':
        matrix[row][col] = 'S'
    elif matrix[row][col] == 'C':
        matrix[row][col] = 'S'
        for key in directions.keys():
            current_r = 0
            current_c = 0
            current_r = row + directions[key][0]
            current_c = col + directions[key][1]

            if matrix[current_r][current_c] == 'X':
                matrix[current_r][current_c] = '-'
                presents -= 1
            elif matrix[current_r][current_c] == 'V':
                matrix[current_r][current_c] = '-'
                presents -= 1
                kids -= 1
                kids_presents += 1

            if presents == 0:
                break

    return matrix, row, col, presents, kids, kids_presents


number_presents = int(input())
size = int(input())
town = [[el for el in input().split()] for _ in range(size)]

directions = {
    'left': [0, -1],
    'right': [0, +1],
    'up': [-1, 0],
    'down': [+1, 0],
}

santa_row, santa_col = starting_position(town, size)
number_nice_kids = count_nice_kids(town, size)
nice_kids_with_presents = 0

while number_presents > 0:
    command = input()
    if command == 'Christmas morning':
        break
    town, santa_row, santa_col, number_presents, number_nice_kids, nice_kids_with_presents = \
        santa_move(town, command, santa_row, santa_col, number_presents, number_nice_kids, nice_kids_with_presents)
    if number_presents == 0 and number_nice_kids > 0:
        print("Santa ran out of presents!")
        break

[print(*row) for row in town]
if number_nice_kids == 0:
    print(f"Good job, Santa! {nice_kids_with_presents} happy nice kid/s.")
else:
    print(f"No presents for {number_nice_kids} nice kid/s.")

#
#
# def move(current_pos_row, current_pos_col, direction, neighborhood):
#     new_pos_row = current_pos_row + directions[direction][0]
#     new_pos_col = current_pos_col + directions[direction][1]
#     if 0 <= new_pos_row < size and 0 <= new_pos_col < size:
#         neighborhood[current_pos_row][current_pos_col] = "-"  # Update old position
#         return new_pos_row, new_pos_col
#
# def coockie_eaten(current_pos_row, current_pos_col, presents, nice_kids):
#     for direction in directions.keys():
#         new_pos_row = current_pos_row + directions[direction][0]
#         new_pos_col = current_pos_col + directions[direction][1]
#         if presents == 0:
#             break
#         if 0 <= new_pos_row < size and 0 <= new_pos_col < size:
#             cell_value = neighborhood[new_pos_row][new_pos_col]
#
#             if cell_value == "V" and presents >= 1:
#                 presents -= 1
#                 nice_kids += 1
#             elif cell_value == "X" and presents >= 1:
#                 presents -= 1
#
#             neighborhood[new_pos_row][new_pos_col] = "-"
#
#     return presents, nice_kids
#
#
# number_presents = int(input())
# size = int(input())
#
# neighborhood = []
# count_nice_kids = 0
# nice_kids_with_presents = 0
# santa_pos = []
#
# directions = {
#     "up": (-1, 0),
#     "down": (1, 0),
#     "left": (0, -1),
#     "right": (0, 1),
# }
#
# for row in range(size):
#     neighborhood.append(input().split())
#     if 'S' in neighborhood[row]:
#         santa_pos = [row, neighborhood[row].index('S')]
#         neighborhood[row][santa_pos[1]] = '-'
#
#     count_nice_kids += neighborhood[row].count("V")
#
# row, col = santa_pos
# command = input().strip()
#
# while not (command == "Christmas morning" or number_presents == 0):
#     row, col = move(row, col, command, neighborhood)
#     if neighborhood[row][col] == "V":   # nice kid
#         nice_kids_with_presents += 1
#         number_presents -= 1
#     elif neighborhood[row][col] == "C":  # coockie
#         number_presents, nice_kids_with_presents = coockie_eaten(row, col, number_presents, nice_kids_with_presents)
#
#     neighborhood[row][col] = "S"
#
#     if number_presents == 0:
#         break
#     command = input().strip()
#
# if number_presents <= 0:
#     print("Santa ran out of presents!")
#
# #[print(*row) for row in neighborhood]
# print(*[' '.join(line) for line in neighborhood], sep='\n')
#
# if count_nice_kids == nice_kids_with_presents:
#     print(f"Good job, Santa! {count_nice_kids} happy nice kid/s.")
# else:
#     print(f"No presents for {count_nice_kids - nice_kids_with_presents} nice kid/s.")
#
