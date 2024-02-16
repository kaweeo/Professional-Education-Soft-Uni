N = int(input())
racing_number = input()
starting_pos = [0, 0]
race_matrix = []
tunel_indices = []
all_tunel_index = []  # [[1, 2], [9, 7]]
kilometers = 0

for track_row in range(N):
    row = input().split()
    tunel_indices = [index for index, value in enumerate(row) if value == 'T']
    for tunel_index in tunel_indices:
        all_tunel_index.append([track_row, tunel_index])
    race_matrix.append(row)

race_matrix[0][0] = "C"

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

row, col = starting_pos
while True:
    direction = input()
    if direction == "End":
        print(f"Racing car {racing_number} DNF.")
        break

    next_row = row + directions[direction][0]
    next_col = col + directions[direction][1]

    if race_matrix[next_row][next_col] == "T":
        kilometers += 30
        race_matrix[next_row][next_col] = "."
        if [next_row, next_col] == all_tunel_index[0]:
            next_row = all_tunel_index[1][0]
            next_col = all_tunel_index[1][1]
        else:
            next_row = all_tunel_index[0][0]
            next_col = all_tunel_index[0][1]

    if race_matrix[next_row][next_col] == ".":
        kilometers += 10

    if race_matrix[next_row][next_col] == "F":
        kilometers += 10
        race_matrix[row][col] = "."
        race_matrix[next_row][next_col] = "C"
        print(f"Racing car {racing_number} finished the stage!")
        break

    race_matrix[next_row][next_col] = "C"
    race_matrix[row][col] = "."
    row, col = next_row, next_col

print(f"Distance covered {kilometers} km.")
for row in race_matrix:
    print(''.join(row))
