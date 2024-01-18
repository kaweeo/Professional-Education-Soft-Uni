from collections import deque

chocolates = [int(x) for x in input().split(", ")]
cups_milk = deque([int(x) for x in input().split(", ")])

choco_milk_shakes = 0

while choco_milk_shakes < 5 or chocolates or cups_milk:

    last_choco = chocolates.pop()
    first_cup_milk = cups_milk.popleft()

    if last_choco <= 0 or first_cup_milk <= 0:
        continue

    if last_choco == first_cup_milk:
        choco_milk_shakes += 1
    else:
        cups_milk.append(first_cup_milk)
        chocolates.append(last_choco - 5)

if choco_milk_shakes >= 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join(map(str, chocolates))}")
else:
    print("Chocolate: empty")

if cups_milk:
    print(f"Milk: {', '.join(map(str, cups_milk))}")
else:
    print("Milk: empty")