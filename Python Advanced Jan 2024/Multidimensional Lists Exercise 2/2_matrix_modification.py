matrix = [[int(x) for x in input().split()] for row in range(int(input()))]

command = input().split()
while command[0] != "END":
    operation = command[0]
    row = int(command[1])
    col = int(command[2])
    number = int(command[3])
    if not (row in range(0, len(matrix)- 1) and col in range(0, len(matrix)- 1)):
        print("Invalid coordinates")
    elif operation == "Add":
        matrix[row][col] += number
    elif operation == "Subtract":
        matrix[row][col] -= number

    command = input().split()

[print(*row) for row in matrix]