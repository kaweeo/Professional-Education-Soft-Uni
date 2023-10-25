
days_count = int(input())
tot_food = float(input())

eated_by_dog = 0
eated_by_cat = 0
total_buiscuits = 0

for day in range(1, days_count + 1):
    eated_by_dot_today = int(input())
    eated_by_dog += eated_by_dot_today
    eated_by_cat_today = int(input())
    eated_by_cat += eated_by_cat_today
    if day % 3 == 0:
        tot_today = eated_by_dot_today + eated_by_cat_today
        buiscuits = tot_today * 0.1
        total_buiscuits += buiscuits

total_eated = eated_by_dog + eated_by_cat
total_eated_pro = (total_eated / tot_food) * 100

total_eated_pro_dog = (eated_by_dog / total_eated) * 100
total_eated_pro_cat = (eated_by_cat / total_eated) * 100

print(f"Total eaten biscuits: {int(total_buiscuits)}gr.")
print(f"{total_eated_pro:.2f}% of the food has been eaten.")
print(f"{total_eated_pro_dog:.2f}% eaten from the dog.")
print(f"{total_eated_pro_cat:.2f}% eaten from the cat.")