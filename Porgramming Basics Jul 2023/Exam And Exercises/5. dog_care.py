tot_food_kg = int(input())
tot_food_gr = tot_food_kg * 1000

eaten_food = 0
flag = True
while flag:
    food_or_adopted = input()
    if food_or_adopted == "Adopted":
        flag = False
        break
    food_or_adopted = int(food_or_adopted)
    eaten_food += food_or_adopted

if eaten_food <= tot_food_gr:
    leftover = tot_food_gr - eaten_food
    print(f"Food is enough! Leftovers: {leftover} grams.")
if eaten_food > tot_food_gr:
    needs = abs(eaten_food - tot_food_gr)
    print(f"Food is not enough. You need {needs} grams more.")