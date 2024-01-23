from collections import deque


def matrix_stamper(str, matrix, row, col):
    current_symbol = str.popleft()
    matrix[row][col] = current_symbol
    str.append(current_symbol)


rows, cols = map(int, input().split())
string = deque(input())

matrix = [[''] * cols for _ in range(rows)]

for row in range(rows):
    if row == 0 or row % 2 == 0:
        for col in range(cols):
            matrix_stamper(string, matrix, row, col)
    else:
         for col in range(cols - 1, -1, -1):
             matrix_stamper(string, matrix, row, col)

for row in matrix:
    print("".join(map(str, row)))


# solution 2

# from collections import deque
#
# rows, cols = [int(x) for x in input().split()]
# word = list(input())
#
# word_copy = deque(word)
# multiplier = 1
#
# for row in range(rows):
#     while len(word_copy) < cols:
#         word_copy.extend(word)
#
#     print(*[word_copy.popleft() for _ in range(cols)][::multiplier], sep="")
#     multiplier *= -1
