
def move(coordinates, direction):
    r = coordinates[0]
    c = coordinates[1]
    dir_r = directions[direction][0]
    dir_c = directions[direction][1]
    if 0 <= r + dir_r < size and 0 <= c + dir_c < size:
        new_position_coordinates = [r + dir_r, c + dir_c]
        return new_position_coordinates
    return None


directions = {
    "up": (-1, 0),    # up
    "down": (1, 0),     # down
    "left": (0, -1),    # left
    "right": (0, 1),     # right
}

size = int(input())
field = []
for row in range(size):
    field.append(input().split())

    if "B" in field[row]:
        bunny_initial_coordinates = [row, field[row].index("B")]

the_best_direction = None
max_eggs = float('-inf')
most_eggs_path = []
for path in directions.keys():
    flag = False
    path_track = []
    path_eggs = 0
    bunny_coordinates = bunny_initial_coordinates

    while not flag:
        new_bunny_position = move(bunny_coordinates, path)
        if new_bunny_position is None:
            flag = True
        elif field[new_bunny_position[0]][new_bunny_position[1]] == "X":
            flag = True
        else:
            path_eggs += int(field[new_bunny_position[0]][new_bunny_position[1]])
            path_track.append(new_bunny_position)
            bunny_coordinates = new_bunny_position

    if max_eggs <= path_eggs:
        max_eggs = path_eggs
        most_eggs_path = path_track
        the_best_direction = path

if most_eggs_path:
    print(the_best_direction)
    print(*most_eggs_path, sep="\n")
    print(max_eggs)




## Solution #2
# size = int(input())
#
# matrix = []
# bunny_pos = []  # [row, col]
# best_path = []
#
# best_direction = None
# max_collected_eggs = float("-inf")
#
# directions = {
#     "up": (-1, 0),
#     "down": (1, 0),
#     "left": (0, -1),
#     "right": (0, 1),
# }
#
# for row in range(size):
#     matrix.append(input().split())
#
#     if 'B' in matrix[row]:
#         bunny_pos = [row, matrix[row].index('B')]
#
# for direction, positions in directions.items():
#     row, col = [
#         bunny_pos[0] + positions[0],
#         bunny_pos[1] + positions[1]
#     ]
#
#     path = []
#     collected_eggs = 0
#
#     while 0 <= row < size and 0 <= col < size:
#         if matrix[row][col] == "X":
#             break
#
#         collected_eggs += int(matrix[row][col])
#         path.append([row, col])
#
#         row += positions[0]
#         col += positions[1]
#
#     if collected_eggs >= max_collected_eggs:
#         max_collected_eggs = collected_eggs
#         best_direction = direction
#         best_path = path
#
# print(best_direction)
# print(*best_path, sep="\n")  # [[1, 2], [3, 4], ...]
# print(max_collected_eggs)