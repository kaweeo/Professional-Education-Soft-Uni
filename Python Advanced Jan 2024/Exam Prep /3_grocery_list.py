def shop_from_grocery_list(budget:int, shopping_list: list, *buying_products_with_prices):
    bought_products = []
    result = ""

    for product, price in buying_products_with_prices:
        if product not in shopping_list:
            continue
        if product in bought_products:
            continue
        if price > budget:
            break
        else:
            bought_products.append(product)
            budget -= price
    bought_products_sorted = sorted(bought_products)
    shopping_list_sorted = sorted(shopping_list)

    if bought_products_sorted == shopping_list_sorted:
        result += f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        result += f"You did not buy all the products. Missing products: {', '.join(el for el in shopping_list_sorted if el not in bought_products_sorted)}."

    return result

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))