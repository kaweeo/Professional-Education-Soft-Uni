
rows_count, columns_count = [int(x) for x in input().split(', ')]
# print(rows_count)
# print(columns_count)
matrix = []
for _ in range(rows_count):
    row = [int(x) for x in input().split(", ")]
    matrix.append(row)
print(matrix)