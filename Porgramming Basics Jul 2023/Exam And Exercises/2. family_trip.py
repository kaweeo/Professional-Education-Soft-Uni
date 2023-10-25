drink = input()
shugar = input()
drinks_count = int(input())

if drink == "Espresso":
    if shugar == "Without":
        price = 0.9 * 0.65
    elif shugar == "Normal":
        price = 1
    elif shugar == "Extra":
        price = 1
elif drink == "Cappuccino":
    if shugar == "Without":
        price = 1 * 0.65
    elif shugar == "Normal":
        price = 1.2
    elif shugar == "Extra":
        price = 1.6
elif drink == "Tea":
    if shugar == "Without":
        price = 0.5 * 0.65
    elif shugar == "Normal":
        price = 0.6
    elif shugar == "Extra":
        price = 0.7

tot = drinks_count * price
if drinks_count >= 5 and drink == "Espresso":
    tot = tot * 0.75
if tot > 15:
    tot = tot * 0.8
print(f"You bought {drinks_count} cups of {drink} for {tot:.2f} lv.")

