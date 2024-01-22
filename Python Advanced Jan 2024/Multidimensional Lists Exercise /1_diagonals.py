
matrix = []

matrix = ([[int(el) for el in input().split(", ")] for row in range(int(input()))])

prim_diagonal = []
socond_diagonal = []
for row in range(len(matrix)):
    prim_diagonal.append(matrix[row][row])
    socond_diagonal.append(matrix[row][len(matrix) - 1 - row])

print(f"Primary diagonal: {', '.join(str(el) for el in prim_diagonal)}. Sum: {sum(prim_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(el) for el in socond_diagonal)}. Sum: {sum(socond_diagonal)}")

# n = int(input())
#
# matrix = [[int(el) for el in input().split(", ")] for _ in range(n)]
# primary = [matrix[r][r] for r in range(n)]
# second = [matrix[r][n - r - 1] for r in range(n)]
#
# print(f"Primary diagonal: {', '.join(str(x) for x in primary)}. Sum: {sum(primary)}")
# print(f"Secondary diagonal: {', '.join(str(x) for x in second)}. Sum: {sum(second)}")