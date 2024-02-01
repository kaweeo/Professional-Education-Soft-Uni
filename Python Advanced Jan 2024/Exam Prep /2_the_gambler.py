
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
jackpot = False
while command != "end":
    row, col = gambler_pos[0] + directions[command][0], gambler_pos[1] + directions[command][1]
    gambler_pos = board[row][col]

    if not (0 <= row < size and 0 <= col < size):
        print("Game over! You lost everything!")
        break  # Gambler leaves

    elif gambler_pos == "W":
        money_balance += 100
    elif gambler_pos == "P":
        money_balance -= 200
        if money_balance <= 0:
            print("Game over! You lost everything!")
            board[row][col] = "G"  # TODO CARE HERE
            break
    elif gambler_pos == "J":
        flag = True
        money_balance += 100000
        board[row][col] = "G"
        if 0 <= row < 2:
            print(f"You win the Jackpot!\nEnd of the game. Total amount: {money_balance}$")
        break

    gambler_pos = "-" # TODO CARE HERE
    command = input()

if not jackpot:
    print(f"End of the game. Total amount: {money_balance}$")
