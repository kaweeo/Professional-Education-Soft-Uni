N, M = [int(x) for x in input().split(',')]

cheese_count = 0
cupboard_matrix = []
starting_pos = []

for _ in range(N):
    row = list(input())
    if "M" in row:
        starting_pos = [_, row.index("M")]
    cheese_count += row.count("C")
    cupboard_matrix.append(row)

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

row, col = starting_pos


while True:
    command = input()

    if command == "danger":
        print("Mouse will come back later!")
        break

    next_row = row + directions[command][0]
    next_col = col + directions[command][1]

    if not (0 <= next_row < N and 0 <= next_col < M):
        print("No more cheese for tonight!")
        break
    elif cupboard_matrix[next_row][next_col] == "*":
        cupboard_matrix[row][col] = "*"
        cupboard_matrix[next_row][next_col] = "M"
    elif cupboard_matrix[next_row][next_col] == "C":
        cheese_count -= 1
        cupboard_matrix[next_row][next_col] = "M"
        cupboard_matrix[row][col] = "*"
        if cheese_count == 0:
            print("Happy mouse! All the cheese is eaten, good night!")
            break
    elif cupboard_matrix[next_row][next_col] == "@":
        next_row = row
        next_col = col
        continue
    elif cupboard_matrix[next_row][next_col] == "T":
        cupboard_matrix[row][col] = "*"
        cupboard_matrix[next_row][next_col] = "M"
        print("Mouse is trapped!")
        break
    row = next_row
    col = next_col

[print("".join(row)) for row in cupboard_matrix]



# # SOLUTION 2
# def is_valid(value, max_value):
#     return 0 <= value < max_value
#
#
# def next_move(command, current_row, current_col):
#     if command == 'up' and is_valid(current_row-1, rows):
#         return current_row-1, current_col
#     if command == 'down' and is_valid(current_row+1, rows):
#         return current_row+1, current_col
#     if command == 'left' and is_valid(current_col-1, cols):
#         return current_row, current_col-1
#     if command == 'right' and is_valid(current_col+1, cols):
#         return current_row, current_col+1
#     return None, None
#
#
# rows, cols = [int(x) for x in input().split(',')]
# field = []
# mouse_row, mouse_col = None, None
# cheese_cnt = 0
# line = ''
#
# for r in range(rows):
#     row = list(input())
#     field.append(row)
#     if 'M' in row:
#         mouse_row = r
#         mouse_col = row.index('M')
#     if 'C' in row:
#         cheese_cnt += row.count('C')
#
#
# while cheese_cnt != 0:
#     line = input()
#     if line == 'danger':
#         break
#     next_row, next_col = next_move(line, mouse_row, mouse_col)
#     if next_row is None or next_col is None:
#         print('No more cheese for tonight!')
#         break
#     if field[next_row][next_col] == '@':
#         continue
#     if field[next_row][next_col] == 'T':
#         field[mouse_row][mouse_col] = '*'
#         mouse_row, mouse_col = next_row, next_col
#         field[mouse_row][mouse_col] = 'M'
#         print("Mouse is trapped!")
#         break
#     if field[next_row][next_col] == '*':
#         field[mouse_row][mouse_col] = '*'
#         mouse_row, mouse_col = next_row, next_col
#         field[mouse_row][mouse_col] = 'M'
#         continue
#     if field[next_row][next_col] == 'C':
#         cheese_cnt -= 1
#         field[mouse_row][mouse_col] = '*'
#         mouse_row, mouse_col = next_row, next_col
#         field[mouse_row][mouse_col] = 'M'
#
# else:
#     print("Happy mouse! All the cheese is eaten, good night!")
#
# if cheese_cnt and line == 'danger':
#     print("Mouse will come back later!")
#
# for row in field:
#     print(''.join(row))
