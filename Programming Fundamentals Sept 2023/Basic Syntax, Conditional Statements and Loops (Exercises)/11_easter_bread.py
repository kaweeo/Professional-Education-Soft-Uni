
budget = float(input())
price_per_kg_fl = float(input())

spent_tot = 0
loaves_of_bread_count = 0
colored_eggs_count = 0

price_1pack_eggs = 0.75 * price_per_kg_fl
price_1l_milk = 1.25 * price_per_kg_fl

usage_one_loaf = price_1pack_eggs + price_per_kg_fl + 0.25 * price_1l_milk


while True:
    spent_tot += usage_one_loaf
    loaves_of_bread_count += 1
    colored_eggs_count += 3
    if loaves_of_bread_count % 3 == 0:
        colored_eggs_count = colored_eggs_count - (loaves_of_bread_count - 2)
    if (budget - spent_tot) < usage_one_loaf:
        break

money_left = budget - spent_tot
print(f"You made {loaves_of_bread_count} loaves of Easter bread! Now you have {colored_eggs_count} eggs and {money_left:.2f}BGN left.")