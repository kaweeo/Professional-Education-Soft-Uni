N, M = [int(x) for x in input().split()]
playgroung_mtx = []
starting_pos = []
moves = 0
touched_opponents = 0

for matrix_row in range(N):
    current_row = input().split()
    if "B" in current_row:
        starting_pos = [matrix_row, current_row.index("B")]
    playgroung_mtx.append(current_row)

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

row, col = starting_pos
direction = input()
while direction != "Finish":
    next_row = row + directions[direction][0]
    next_col = col + directions[direction][1]

    if not (0 <= next_row < N and 0 <= next_col < M):
        next_row = row
        next_col = col
    elif playgroung_mtx[next_row][next_col] == "O":
        next_row = row
        next_col = col
    elif playgroung_mtx[next_row][next_col] == "P":
        moves += 1
        touched_opponents += 1
        playgroung_mtx[next_row][next_col] = "-"
        if touched_opponents == 3:
            break # TODO CARE HERE
    elif playgroung_mtx[next_row][next_col] == "-":
        moves += 1

    playgroung_mtx[row][col] = "-"
    row = next_row
    col = next_col

    direction = input()

print("Game over!")
print(f"Touched opponents: {touched_opponents} Moves made: {moves}")
