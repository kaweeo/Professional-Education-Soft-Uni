rows, cols = [int(x) for x in input().split(", ")]

matrix = []
matrix_sum = 0

for row in range(rows):
    lines = [int(x) for x in input().split(", ")]
    matrix.append(lines)
for row in matrix:
    for element in row:
        matrix_sum += element

print(matrix_sum)
print(matrix)

