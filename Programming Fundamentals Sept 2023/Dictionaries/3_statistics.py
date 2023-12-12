
products = {}
while True:
    product_w_quantity = input()
    if product_w_quantity == "statistics":
        break
    else:
        product_w_quantity = product_w_quantity.split(": ")
        product = product_w_quantity[0]
        quantity = int(product_w_quantity[1])
        if product in products:
            products[product] += quantity
        else:
            products[product] = quantity

print("Products in stock:")
for key, value in products.items():
    print(f'- {key}: {value}')
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")