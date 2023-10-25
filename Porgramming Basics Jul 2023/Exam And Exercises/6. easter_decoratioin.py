
basket = 1.5
wreath = 3.8
choco_bunny = 7
clients_count = int(input())
spent_total = 0

for client in range(1, clients_count + 1):
    order_total = 0
    order_count = 0
    while True:
        order = input()
        if order == "Finish":

            break
        order_count += 1
        if order == "basket":
            order_total += basket
        elif order == "wreath":
            order_total += wreath
        elif order == "chocolate bunny":
            order_total += choco_bunny
    if order_count % 2 == 0:
        order_total = order_total * 0.8
    spent_total += order_total
    print(f"You purchased {order_count} items for {order_total:.2f} leva.")
avg_spent = spent_total / clients_count
print(f"Average bill per client is: {avg_spent:.2f} leva.")
