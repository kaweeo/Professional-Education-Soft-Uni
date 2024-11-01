rows, cols = (int(x) for x in input().split())
matrix = [["" for _ in range(cols)] for _ in range(rows)]

for row in range(rows):
    for col in range(cols):
        current_palindrome = chr(row + 97) + chr(row + col + 97) + chr(row + 97)
        matrix[row][col] = current_palindrome

for list in matrix:
    print(*list)


# rows, cols = [int(x) for x in input().split()]
#
# start = ord('a')
#
# for row in range(start, start + rows):
#     for col in range(row, row + cols):
#         print(chr(row), chr(col), chr(row), sep="", end=" ")
#
#     print()
