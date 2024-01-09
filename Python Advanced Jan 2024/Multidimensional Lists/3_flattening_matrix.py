
rows = int(input())
matrix = []
for row in range(rows):
    row = list(map(int, input().split(", ")))
    matrix.append(row)
# rows_count = int(input())
# matrix = [map(int, input().split(', ')) for _ in range(rows_count)]
flattened = [num for sublist in matrix for num in sublist]
print(flattened)