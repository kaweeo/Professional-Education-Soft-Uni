# size = int(input())
#
# matrix = [[0] * size for row in range(0, size)]
#
# for x in range(0, size):
#     line = list(map(int, input().split()))
#     for y in range(0, size):
#         matrix[x][y] = line[y]
# sum_diagonal = sum(matrix[size - i - 1][size - i - 1] for i in range(size))
# print(sum_diagonal)

row = int(input())

matrix = []

for _ in range(row):
    matrix.append([int(el) for el in input().split()])

diagonal_sum = 0
for row_index in range(row):
    diagonal_sum += matrix[row_index][row_index]
print(diagonal_sum)