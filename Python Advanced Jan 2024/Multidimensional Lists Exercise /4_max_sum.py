min_size = float("-inf")

rows, cols = input().split()

matrix = [[int(el) for el in input().split()] for row in range(int(rows))]

max_sum_submatrix = min_size
for row in range(int(rows) - 2):
    for col in range(int(cols) - 2):
        sum_sub_matrix = 0
        sub_matrix = [row[col:col+3] for row in matrix[row:row+3]]
        sum_sub_matrix += sum(sum(row) for row in sub_matrix)
        if sum_sub_matrix > max_sum_submatrix:
            max_sum_submatrix = sum_sub_matrix
            max_sub_matrix = sub_matrix

print(f"Sum = {max_sum_submatrix}")
print('\n'.join([' '.join(map(str, line)) for line in max_sub_matrix]))  # [print(*row) for row in biggest_matrix]