n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]
coordinates = ((int(x) for x in c.split(",")) for c in input().split()) # 1,2  3,4  5,6 => ["1,2", "3,4", "5, 6"] => ((1, 2), (3, 4), (5, 6))

directions = (
    (-1, 0),    # up
    (1, 0),     # down
    (0, -1),    # left
    (0, 1),     # right
    (-1, 1),    # top-right
    (-1, -1),   # top-left
    (1, -1),    # bottom-left
    (1, 1),     # bottom-right
    (0, 0),     # current -> !important to be last
)

for row, col in coordinates:
    if matrix[row][col] <= 0:
        continue

    for x, y in directions:
        r, c = row + x, col + y

        if 0 <= r < n and 0 <= c < n:
            matrix[r][c] -= matrix[row][col] if matrix[r][c] > 0 else 0

alive_cells = [num for row in range(n) for num in matrix[row] if num > 0]

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")

[print(*row) for row in matrix]


# n = int(input())
#
# matrix = [[int(x) for x in input().split()] for row in range(n)]
#
# bombs = input().split()
# for bomb in bombs:
#     bomb_coordinates = [int(x) for x in bomb.split(",")]
#     bomb_row, bomb_col = bomb_coordinates
#     bomb = matrix[bomb_row][bomb_col]
#     if bomb_row - 1 >= 0 and matrix[bomb_row - 1][bomb_col] > 0:
#         matrix[bomb_row - 1][bomb_col] = matrix[bomb_row - 1][bomb_col] - bomb
#     if bomb_row - 1 >= 0 and bomb_col + 1 < n and matrix[bomb_row - 1][bomb_col + 1] > 0:
#         matrix[bomb_row - 1][bomb_col + 1] = matrix[bomb_row - 1][bomb_col + 1] - bomb
#     if bomb_col + 1 < n and matrix[bomb_row][bomb_col + 1] > 0:
#         matrix[bomb_row][bomb_col + 1] = matrix[bomb_row][bomb_col + 1] - bomb
#     if bomb_row + 1 < n and bomb_col + 1 < n and matrix[bomb_row + 1][bomb_col + 1] > 0:
#         matrix[bomb_row + 1][bomb_col + 1] = matrix[bomb_row + 1][bomb_col + 1] - bomb
#     if bomb_row + 1 < n and matrix[bomb_row + 1][bomb_col] > 0:
#         matrix[bomb_row + 1][bomb_col] = matrix[bomb_row + 1][bomb_col] - bomb
#     if bomb_row + 1 < n and bomb_col - 1 >= 0 and matrix[bomb_row + 1][bomb_col - 1] > 0:
#         matrix[bomb_row + 1][bomb_col - 1] = matrix[bomb_row + 1][bomb_col - 1] - bomb
#     if bomb_col - 1 >= 0 and matrix[bomb_row][bomb_col - 1] > 0:
#         matrix[bomb_row][bomb_col - 1] = matrix[bomb_row][bomb_col - 1] - bomb
#     if bomb_row - 1 >= 0 and bomb_col - 1 >= 0 and matrix[bomb_row - 1][bomb_col - 1] > 0:
#         matrix[bomb_row - 1][bomb_col - 1] = matrix[bomb_row - 1][bomb_col - 1] - bomb
#
#     matrix[bomb_row][bomb_col] = 0
#
# active_sells = 0
# sum = 0
# for row in matrix:
#     for el in row:
#         if el > 0:
#             active_sells += 1
#             sum += el
#
# print(f"Alive cells: {active_sells}")
# print(f"Sum: {sum}")
# for row in matrix:
#     print(" ".join(map(str, row)))