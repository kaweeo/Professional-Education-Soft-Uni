
rows_count, columns_count = [int(x) for x in input().split(', ')]
# print(rows_count)
# print(columns_count)
matrix = []
for _ in range(rows_count):
    row = [int(x) for x in input().split(", ")]
    matrix.append(row)

max_sub_matrix_sum = 0
max_sum_elements = []
for col_index in range(columns_count - 1):
    for row_index in range(rows_count - 1):
        sub_matrix_sum = (
                matrix[row_index][col_index] +
                matrix[row_index][col_index + 1] +
                matrix[row_index + 1][col_index] +
                matrix[row_index + 1][col_index + 1]
        )
        if sub_matrix_sum > max_sub_matrix_sum:
            max_sub_matrix_sum = sub_matrix_sum
            max_sum_elements.append(matrix[row_index][col_index])
            max_sum_elements.append(matrix[row_index][col_index + 1])
            max_sum_elements.append(matrix[row_index + 1][col_index])
            max_sum_elements.append(matrix[row_index + 1][col_index + 1])
            max_top_left_coords = (row_index, col_index)

for i in range(2):
    for j in range(2):
        print(matrix[max_top_left_coords[0] + i][max_top_left_coords[1] + j], end=" ")
    print()
print(max_sub_matrix_sum)