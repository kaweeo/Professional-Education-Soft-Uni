#Clothes->43.30|Shoes->25.25|Clothes->36.52|Clothes->20.90|Accessories->15.60

ticket_cost = 150
string_input = input()
budget = int(input())

bought_items_new_prices = []
profit = 0
my_list = string_input.split("|")

for element in my_list:
    lot = element.split("->")
    item = lot[0]
    price = float(lot[1])
    if budget <= price:
        continue
    if item == "Clothes" and price > 50:
        continue
    elif item == "Shoes" and price > 35:
        continue
    elif item == "Accessories" and price > 20.50:
        continue
    else:
        budget -= price
        new_price = price * 0.4 + price
        # budget += new_price
        item_profit = new_price - price
        profit += item_profit
        bought_items_new_prices.append(new_price)

for price in bought_items_new_prices:
    budget += price

# formatted_prices = [f"{price:.2f}" for price in bought_items_new_prices]
# # Join the formatted prices with a space separator
# price_string = " ".join(formatted_prices)
# # Print the resulting string
# print(price_string)

for price in bought_items_new_prices:
    print(f"{price:.2f}", end=" ")

print()
print(f"Profit: {profit:.2f}")

if budget >= ticket_cost:
    print("Hello, France!")
else:
    print("Not enough money.")





