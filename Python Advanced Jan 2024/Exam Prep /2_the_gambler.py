
size = int(input())

gambler_pos = []
board = []
money_balance = 100

for row in range(size):
    board.append(list(input()))
    if 'G' in board[row]:
        gambler_pos = [row, board[row].index('G')]
        board[row][gambler_pos[1]] = '-'

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

command = input()
flag = False
row, col = gambler_pos

while command != "end":
    board[row][col] = "-"
    row += directions[command][0]
    col += directions[command][1]

    if not (0 <= row < size and 0 <= col < size):
        print("Game over! You lost everything!")
        flag = True
        break  # Gambler leaves

    if board[row][col] == "W":
        money_balance += 100
    elif board[row][col] == "P":
        money_balance -= 200
        if money_balance <= 0:
            print("Game over! You lost everything!")
            board[row][col] = "G"  # TODO CARE HERE
            flag = True
            break
    elif board[row][col] == "J":
        flag = True
        money_balance += 100000
        board[row][col] = "G"
        if 0 <= row < 2:
            print(f"You win the Jackpot!\nEnd of the game. Total amount: {money_balance}$")
        break

    board[row][col] = "G" # TODO CARE HERE
    command = input()

if not flag:
    print(f"End of the game. Total amount: {money_balance}$")

if money_balance > 0:
    [print(''.join(el for el in row)) for row in board]



# Function to handle the current position of the gambler
def handle_current_position(position, board, sum_val, jackpot):
    current_char = board[position[0]][position[1]]

    if current_char == 'J':
        sum_val += 100000
        jackpot = True
    elif current_char == 'W':
        sum_val += 100
    elif current_char == 'P':
        sum_val -= 200

    board[position[0]][position[1]] = 'G'

    return sum_val, jackpot


# Function to check if the total amount becomes zero or negative
def zero_amount(sum_val):
    return sum_val <= 0


# Function to print the game over message
def game_over():
    print("Game over! You lost everything!")


# Function to move the gambler on the board based on the command
def move_gambler(command, position, board):
    row, col = position
    board[row][col] = '-'
    if command == "up":
        position[0] -= 1
    elif command == "down":
        position[0] += 1
    elif command == "left":
        position[1] -= 1
    elif command == "right":
        position[1] += 1

    return position


# Function to check if the gambler is out of bounds
def is_out_of_bounds(position, size):
    return position[0] < 0 or position[0] >= size or position[1] < 0 or position[1] >= size


# Function to find the starting position of the gambler
def find_start_position(size, fishing_area):
    for i in range(size):
        for j in range(size):
            if fishing_area[i][j] == 'G':
                return [i, j]
    return None


# Function to fill the board with input data
def fill_board(size):
    board = []
    for _ in range(size):
        board.append(list(input()))
    return board


size = int(input())
board = fill_board(size)
current_position = find_start_position(size, board)
sum_val = 100
jackpot = False

while True:
    if jackpot:
        print("You win the Jackpot!")
        break
    command = input()

    if current_position:
        current_position = move_gambler(command, current_position, board)

    if is_out_of_bounds(current_position, size) or zero_amount(sum_val):
        game_over()
        break
    else:
        sum_val, jackpot = handle_current_position(current_position, board, sum_val, jackpot)

    if command == "end":
        break

if not (is_out_of_bounds(current_position, size) or zero_amount(sum_val)):
    print(f"End of the game. Total amount: {sum_val}$")
    for row in board:
        print(''.join(row))
