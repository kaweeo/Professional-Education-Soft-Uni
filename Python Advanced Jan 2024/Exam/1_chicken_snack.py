from collections import deque

money_stack = [int(x) for x in input().split()]
prices_deque = deque([int(x) for x in input().split()])

food_counter = 0

while money_stack and prices_deque:

    last_money = money_stack.pop()
    first_price = prices_deque.popleft()

    if last_money == first_price:
        food_counter += 1

    elif last_money > first_price:
        food_counter += 1
        change = last_money - first_price
        if len(money_stack) > 0:
            money_stack[-1] += change
        else:
            money_stack.append(change)
    elif first_price < last_money:
        pass

if food_counter >= 4:
    print(f"Gluttony of the day! Henry ate {food_counter} foods.")
if food_counter == 0:
    print("Henry remained hungry. He will try next weekend again.")
if food_counter == 1:
    print(f"Henry ate: {food_counter} food.")
if food_counter > 1 and food_counter < 4:
    print(f"Henry ate: {food_counter} foods.")
