def move(direction: str, position: list):
    x, y = directions[direction]
    new_position = [int(position[0]) + x, position[1] + y]
    return new_position


size = int(input())
field = []
teabags_quantity = 0

for row in range(size):
    field.append(input().split())
    if 'A' in field[row]:
        alice_pos = [row, field[row].index('A')]
        field[row][alice_pos[1]] = '*'

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}


while teabags_quantity < 10:
    command = input()

    new_position = move(command, alice_pos)
    alice_pos = new_position

    if not (0 <= alice_pos[0] < size and 0 <= alice_pos[1] < size):
        break

    alice_step = field[alice_pos[0]][alice_pos[1]]
    if alice_step == "R":
        field[alice_pos[0]][alice_pos[1]] = "*"
        break
    elif alice_step.isdigit():
        teabags_quantity += int(alice_step)
        field[alice_pos[0]][alice_pos[1]] = "*"

    field[alice_pos[0]][alice_pos[1]] = "*"

if teabags_quantity < 10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

[print(*row) for row in field]