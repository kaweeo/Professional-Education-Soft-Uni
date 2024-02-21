def shopping_cart(*meal_data):
    result = ""
    meals_count_dict = {
        "Soup": [],
        "Pizza": [],
        "Dessert": [],
    }

    for arg in meal_data:
        if not len(arg) == 2 and arg == "Stop":
            is_empty = all(not meal_list for meal_list in meals_count_dict.values())
            if is_empty:
                return "No products in the cart!"
            break
        else:
            meal, product = arg
            if product in meals_count_dict[meal]:
                continue
            else:
                if meal == "Soup":
                    if len(meals_count_dict[meal]) < 3:
                        meals_count_dict[meal].append(product)
                elif meal == "Pizza":
                    if len(meals_count_dict[meal]) < 4:
                        meals_count_dict[meal].append(product)
                elif meal == "Dessert":
                    if len(meals_count_dict[meal]) < 2:
                        meals_count_dict[meal].append(product)

    is_empty = all(not meal_list for meal_list in meals_count_dict.values())
    if is_empty:
        return "No products in the cart!"

    for value in meals_count_dict.values():
        value.sort()

    sorted_meal_count_dict = dict(sorted(meals_count_dict.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])))

    for key, value in sorted_meal_count_dict.items():
        result += f"{key}:\n"
       # if value: TODO CARE
        for sub_value in value:
            result += f" - {sub_value}\n"

    return result

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))