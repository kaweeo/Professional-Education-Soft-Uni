def check_indices_valid(indices):  # row1=1 col1=2 row2=0 col2=2
    return {indices[0], indices[2]}.issubset(valid_rows) and {indices[1], indices[3]}.issubset(valid_cols)

def swap_elements(command, indices):
    if len(indices) == 4 and check_indices_valid(indices) and command == "swap":
        row1, col1, row2, col2 = indices  # [2, 5, 3, 4]
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

        [print(*row) for row in matrix]  # row => [1, 2, 3, 4] =>
    else:
        print("Invalid input!")


rows, cols = [int(x) for x in input().split()]  # row = 3, col = 4
matrix = [input().split() for _ in range(rows)]

valid_rows = range(rows)  # [0, 1, 2]
valid_cols = range(cols)  # [0, 1, 2, 3]

while True:
    command_type, *coordinates = [int(x) if x.isdigit() else x for x in input().split()]  # ["swap", 2, 3, 5, 4]

    if command_type == "END":
        break

    swap_elements(command_type, coordinates)

# Solution 2
# rows, cols = (int(x) for x in input().split())
# matrix = [[int(x) for x in input().split()] for _ in range(rows)]
#
# command = input().split()
# while command[0] != 'END':
#     if len(command) == 5 and 0 <= int(command[1]) < rows and 0 <= int(command[2]) < cols \
#             and 0 <= int(command[3]) < rows and 0 <= int(command[4]) < cols:
#         first_value = matrix[int(command[1])][int(command[2])]
#         second_value = matrix[int(command[3])][int(command[4])]
#         matrix[int(command[3])][int(command[4])] = first_value
#         matrix[int(command[1])][int(command[2])] = second_value
#         for list in matrix:
#             print(*list)
#     else:
#         print('Invalid input!')
#     command = input().split()

# Solution 3
# def command_validator(list: list) -> bool or str:
#     """ Checks is command valid or not """
#
#     if list[0] == "swap" and len(list) == 5:
#         is_valid = True
#     else:
#         is_valid = False
#
#     for el in list[1:5]:
#         if int(el) < 0:
#             is_valid = False
#         elif int(list[1]) >= rows or int(list[3]) >= rows:
#             is_valid = False
#         elif int(list[2]) >= cols or int(list[4]) >= cols:
#             is_valid = False
#
#     if is_valid:
#         return True
#     else:
#         print("Invalid input!")
#
#
# def value_swapper(row, col, row_1, col_1, swapping_matrix) -> list:
#     """ Swaps values in matrix """
#
#     swapping_matrix[row][col], swapping_matrix[row_1][col_1] = swapping_matrix[row_1][col_1], swapping_matrix[row][col]
#     return swapping_matrix
#
#
# rows, cols = [int(x) for x in input().split()]
#
# matrix = [[int(x) for x in input().split()] for _ in range(rows)]
#
# command_list = input().split()
# while command_list[0] != "END":
#
#     if command_validator(command_list):
#         row1, col1, row2, col2 = [int(x) for x in command_list[1:5]]
#         result = value_swapper(row1, col1, row2, col2, matrix)
#         [print(*row) for row in result]
#
#     command_list = input().split()
#
